"""Fetch cantonal law: LexFind (primary) with LexWork/ZHLex text fallback."""
from __future__ import annotations

import logging
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass, field
from datetime import date

import requests

from .cantonal_transformer import transform_cantonal_html

logger = logging.getLogger(__name__)

# Retry configuration
MAX_RETRIES = 4
INITIAL_BACKOFF = 2.0
BACKOFF_FACTOR = 2.0
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}

# ─── LexFind API (primary source for catalog + metadata) ─────────────────────
#
# LexFind exposes a JSON API under ``/api/fe/{lang}/``.  The systematic category
# tree (``/entities/{id}/systematics``) is used to enumerate every canton's laws,
# replacing the old stopword-based fulltext search.  LexFind is authoritative for
# metadata (categories, is_active, dates).  Structured text still comes from
# LexWork / ZHLex as a fallback (LexFind serves PDFs only).
LEXFIND_API = "https://www.lexfind.ch/api/fe"

# Max leaf-node IDs per request for global systematics (URL length limit).
_GLOBAL_SYSTEMATICS_BATCH = 100

# ─── Canton Registry ───────────────────────────────────────────────────────────

LEXWORK_CANTONS: dict[str, str] = {
    "ag": "gesetzessammlungen.ag.ch",
    "ar": "ar.clex.ch",
    "be": "www.belex.sites.be.ch",
    "bl": "bl.clex.ch",
    "bs": "www.gesetzessammlung.bs.ch",
    "fr": "bdlf.fr.ch",
    "gl": "gesetze.gl.ch",
    "gr": "www.gr-lex.gr.ch",
    "lu": "srl.lu.ch",
    "sg": "www.gesetzessammlung.sg.ch",
    "so": "bgs.so.ch",
    "tg": "www.rechtsbuch.tg.ch",
    "vs": "lex.vs.ch",
    "zg": "bgs.zg.ch",
}

LEXFIND_ONLY_CANTONS = [
    "ai", "ju", "nw", "ow", "sh", "sz", "ti", "ur", "vd",
]

# Cantons with dedicated fetchers (not LexWork, not generic LexFind)
DEDICATED_FETCHER_CANTONS = ["zh", "ge", "ne"]

ALL_CANTONS = sorted(
    list(LEXWORK_CANTONS.keys()) + LEXFIND_ONLY_CANTONS + DEDICATED_FETCHER_CANTONS
)

# Official languages per canton.  Cantons not listed default to ["de"].
CANTON_LANGUAGES: dict[str, list[str]] = {
    "be": ["de", "fr"],
    "fr": ["de", "fr"],
    "vs": ["de", "fr"],
    "gr": ["de", "it", "rm"],
    "ge": ["fr"],
    "vd": ["fr"],
    "ne": ["fr"],
    "ju": ["fr"],
    "ti": ["it"],
}


# ─── Models ────────────────────────────────────────────────────────────────────

@dataclass
class CantonalLawEntry:
    """A cantonal law entry from catalog."""
    canton: str
    systematic_number: str
    title: str
    abbreviation: str = ""
    enactment_date: date | None = None
    is_active: bool = True
    lexfind_id: str = ""
    systematic_category: str = ""
    systematic_category_id: str = ""
    global_category: str = ""
    global_category_id: str = ""
    category_type: str = ""


@dataclass
class CantonalLawVersion:
    """A specific version of a cantonal law."""
    canton: str
    systematic_number: str
    version_id: int | str
    title: str
    date_in_force: date | None = None
    date_until: date | None = None
    abbreviation: str = ""


@dataclass
class LawDates:
    """Date facts for one law: original enactment + known version dates."""
    canton: str
    systematic_number: str
    enactment_date: date | None = None
    version_dates: list[date] = field(default_factory=list)  # sorted ascending


@dataclass
class CantonalLawText:
    """Full text of a cantonal law version.

    ``origin`` records which source actually produced the text
    ("lexwork", "lexfind_pdf", "zhlex", "lexfind") — it drives the
    transformer choice and the frontmatter ``source`` label, which
    matters when a LexWork canton is served by the LexFind fallback.
    """
    canton: str
    systematic_number: str
    title: str
    html_content: str = ""
    language: str = "de"
    version_date: date | None = None
    abbreviation: str = ""
    origin: str = ""


# ─── Fetcher ───────────────────────────────────────────────────────────────────

class CantonalFetcher:
    """Fetches cantonal law — LexFind primary, LexWork/ZHLex text fallback."""

    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit
        self._last_request = 0.0
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "legalize-ch/0.1 (swiss-law pipeline)"
        self._entity_ids: dict[str, dict[str, int]] = {}
        self._categories: dict[str, dict[int, str]] = {}
        self._global_leaves: list[int] | None = None

    def _throttle(self):
        elapsed = time.time() - self._last_request
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)
        self._last_request = time.time()

    def _get_json(self, url: str) -> dict | None:
        """Fetch JSON with retry and backoff."""
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, timeout=30)
                if resp.status_code == 404:
                    return None
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    logger.warning("HTTP %d from %s (attempt %d) — retrying in %.1fs",
                                   resp.status_code, url, attempt, backoff)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                return resp.json()
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    logger.warning("Failed %s (attempt %d): %s — retrying", url, attempt, e)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed %s after %d attempts: %s", url, MAX_RETRIES, e)
        return None

    def _post_json(self, url: str, body: dict) -> dict | list | None:
        """POST a JSON body and return the JSON response, with retry and backoff."""
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.post(url, json=body, timeout=30)
                if resp.status_code == 404:
                    return None
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    logger.warning("HTTP %d from %s (attempt %d) — retrying in %.1fs",
                                   resp.status_code, url, attempt, backoff)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                return resp.json()
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    logger.warning("Failed POST %s (attempt %d): %s — retrying", url, attempt, e)
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed POST %s after %d attempts: %s", url, MAX_RETRIES, e)
        return None

    def _get_html(self, url: str) -> str:
        """Fetch HTML content with retry."""
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, timeout=30)
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                return resp.text
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed %s: %s", url, e)
        return ""

    # ─── LexWork API ───────────────────────────────────────────────────────────

    def _lexwork_base(self, canton: str) -> str:
        """Get the LexWork API base URL for a canton."""
        host = LEXWORK_CANTONS[canton]
        return f"https://{host}/api"

    def fetch_lexwork_law(self, canton: str, number: str,
                          lang: str = "de") -> dict | None:
        """Fetch a law from LexWork API. Returns raw JSON response.

        The language-scoped path (``/api/{lang}/texts_of_law/{nr}``) matters for
        bilingual cantons (FR, GR, VS); it also works for monolingual ones.
        """
        base = self._lexwork_base(canton)
        url = f"{base}/{lang}/texts_of_law/{number}"
        return self._get_json(url)

    def fetch_lexwork_version(self, canton: str, number: str, version_id: int,
                              lang: str = "de") -> dict | None:
        """Fetch a specific version from LexWork."""
        base = self._lexwork_base(canton)
        url = f"{base}/{lang}/texts_of_law/{number}/versions/{version_id}"
        return self._get_json(url)

    def fetch_catalog(self, canton: str, lang: str = "de") -> list[CantonalLawEntry]:
        """Fetch full catalog for a canton — dispatches to dedicated fetchers first."""
        if canton == "zh":
            from .zurich_fetcher import ZurichFetcher
            return ZurichFetcher(rate_limit=self.rate_limit).fetch_catalog(lang)
        if canton == "ge":
            from .cantonal_scrapers import GeneveFetcher
            return GeneveFetcher(rate_limit=self.rate_limit).fetch_catalog(lang)
        if canton == "ne":
            from .cantonal_scrapers import NeuchatelFetcher
            return NeuchatelFetcher(rate_limit=self.rate_limit).fetch_catalog(lang)

        return self._fetch_lexfind_catalog_by_systematics(canton, lang)

    # ─── LexFind API (primary catalog + metadata source) ──────────────────────

    def _lexfind_entity_id(self, canton: str, lang: str = "de") -> int | None:
        """Resolve canton abbreviation → LexFind entity id (cached)."""
        if lang not in self._entity_ids:
            url = f"{LEXFIND_API}/{lang}/entities"
            data = self._get_json(url)
            mapping: dict[str, int] = {}
            if isinstance(data, list):
                for ent in data:
                    abbr = str(ent.get("abbreviation", "")).lower()
                    if abbr and isinstance(ent.get("id"), int):
                        mapping[abbr] = ent["id"]
            self._entity_ids[lang] = mapping
            if not mapping:
                logger.warning("LexFind entities returned no mapping for lang=%s", lang)
        return self._entity_ids[lang].get(canton.lower())

    def _fetch_categories(self, lang: str = "de") -> dict[int, str]:
        """Fetch instrument types (Gesetz, Verordnung, etc.) — cached."""
        if lang not in self._categories:
            url = f"{LEXFIND_API}/{lang}/categories"
            data = self._get_json(url)
            mapping: dict[int, str] = {}
            if isinstance(data, list):
                for cat in data:
                    if isinstance(cat.get("id"), int) and cat.get("name"):
                        mapping[cat["id"]] = cat["name"]
            self._categories[lang] = mapping
        return self._categories[lang]

    def _fetch_global_leaves(self, lang: str = "de") -> list[int]:
        """Get all leaf node IDs from the global systematics tree — cached."""
        if self._global_leaves is None:
            url = f"{LEXFIND_API}/{lang}/global/systematics"
            data = self._get_json(url)
            if not isinstance(data, dict):
                self._global_leaves = []
                return self._global_leaves
            self._global_leaves = sorted(
                int(k) for k, v in data.items()
                if k and not v.get("children")
            )
        return self._global_leaves

    def _fetch_global_category_map(
        self, entity_id: int, lang: str = "de",
    ) -> dict[int, tuple[str, str]]:
        """Build tol_id → (global_category_id, global_category_title) map.

        Fetches the global systematics ("domaine juridique") filtered to one
        canton, batching leaf node IDs to stay within URL length limits.
        """
        leaves = self._fetch_global_leaves(lang)
        if not leaves:
            return {}

        result: dict[int, tuple[str, str]] = {}
        for i in range(0, len(leaves), _GLOBAL_SYSTEMATICS_BATCH):
            batch = leaves[i:i + _GLOBAL_SYSTEMATICS_BATCH]
            params = "&".join(f"tols_for_systematics[]={lid}" for lid in batch)
            url = (
                f"{LEXFIND_API}/{lang}/global/systematics"
                f"?active_only=false&entity_filter[]={entity_id}&{params}"
            )
            data = self._get_json(url)
            if not isinstance(data, dict):
                continue
            for k, v in data.items():
                if not k:
                    continue
                for tol in v.get("tols", []):
                    tol_id = tol.get("id")
                    if tol_id is not None and tol_id not in result:
                        result[tol_id] = (
                            str(v.get("identifier", "")),
                            str(v.get("title", "")),
                        )
        return result

    def _fetch_lexfind_catalog_by_systematics(
        self, canton: str, lang: str = "de",
    ) -> list[CantonalLawEntry]:
        """Enumerate a canton's laws via the LexFind systematics tree.

        Walks the per-canton category tree, fetches all leaf-level texts of law
        in a single request, then enriches each entry with the global "domaine
        juridique" classification and instrument type.
        """
        entity_id = self._lexfind_entity_id(canton, lang)
        if entity_id is None:
            logger.warning("Canton %s has no LexFind entity for lang=%s", canton.upper(), lang)
            return []

        # 1. Fetch per-canton systematics tree (without tols) to find leaf nodes
        tree_url = f"{LEXFIND_API}/{lang}/entities/{entity_id}/systematics"
        tree = self._get_json(tree_url)
        if not isinstance(tree, dict):
            logger.warning("LexFind systematics tree unavailable for %s", canton.upper())
            return []

        leaf_ids = sorted(
            int(k) for k, v in tree.items()
            if k and not v.get("children")
        )
        if not leaf_ids:
            logger.warning("No leaf categories for %s", canton.upper())
            return []

        # 2. Re-fetch with tols_for_systematics[] for all leaves (batched)
        all_tols: dict[str, dict] = {}  # node_key → node data (merged across batches)
        for i in range(0, len(leaf_ids), _GLOBAL_SYSTEMATICS_BATCH):
            batch = leaf_ids[i:i + _GLOBAL_SYSTEMATICS_BATCH]
            params = "&".join(f"tols_for_systematics[]={lid}" for lid in batch)
            batch_url = f"{tree_url}?active_only=false&{params}"
            batch_data = self._get_json(batch_url)
            if not isinstance(batch_data, dict):
                continue
            for k, v in batch_data.items():
                if k and v.get("tols"):
                    all_tols[k] = v

        # Build tol_id → canton category mapping
        tol_canton_cat: dict[int, tuple[str, str]] = {}
        for k, v in all_tols.items():
            cat_id = str(v.get("identifier", ""))
            cat_title = str(v.get("title", ""))
            for tol in v.get("tols", []):
                tid = tol.get("id")
                if tid is not None:
                    tol_canton_cat[tid] = (cat_id, cat_title)

        # 3. Fetch global "domaine juridique" mapping
        tol_global_cat = self._fetch_global_category_map(entity_id, lang)

        # 4. Fetch instrument type names
        cat_types = self._fetch_categories(lang)

        # 5. Build entries, dedup by systematic_number
        entries: dict[str, CantonalLawEntry] = {}
        for k, v in all_tols.items():
            for tol in v.get("tols", []):
                sr = str(tol.get("systematic_number", "")).strip()
                if not sr or sr in entries:
                    continue
                tol_id = tol.get("id")
                canton_cat = tol_canton_cat.get(tol_id, ("", ""))
                global_cat = tol_global_cat.get(tol_id, ("", ""))
                cat_type_id = tol.get("category_id")
                entries[sr] = CantonalLawEntry(
                    canton=canton,
                    systematic_number=sr,
                    title=str(tol.get("title", "")).strip(),
                    abbreviation=str(tol.get("keywords", "") or ""),
                    is_active=bool(tol.get("is_active", True)),
                    lexfind_id=str(tol_id) if tol_id is not None else "",
                    systematic_category=f"{canton_cat[0]} {canton_cat[1]}".strip(),
                    systematic_category_id=canton_cat[0],
                    global_category=f"{global_cat[0]} {global_cat[1]}".strip(),
                    global_category_id=global_cat[0],
                    category_type=cat_types.get(cat_type_id, "") if cat_type_id else "",
                )

        logger.info("LexFind catalog for %s: %d laws (%d categories)",
                     canton.upper(), len(entries), len(leaf_ids))
        return list(entries.values())

    # ─── Unified fetch methods ─────────────────────────────────────────────────

    def fetch_law_text(self, canton: str, number: str,
                       lang: str = "de",
                       lexfind_id: str = "") -> CantonalLawText | None:
        """Fetch current law text: dedicated fetcher, LexWork, or LexFind fallback.

        Strategy:
        1. If canton has a dedicated fetcher (e.g. ZH) → use it
        2. If canton has LexWork portal → fetch from LexWork API
        3. Otherwise → fetch from LexFind
        """
        # Dedicated fetchers
        if canton == "zh":
            return self._fetch_from_zurich(number, lang, erlass_id=lexfind_id)
        if canton == "ge":
            return self._fetch_from_geneve(number, lang, filename=lexfind_id)
        if canton == "ne":
            return self._fetch_from_neuchatel(number, lang, filename=lexfind_id)

        # Try LexWork first
        if canton in LEXWORK_CANTONS:
            text = self._fetch_from_lexwork(canton, number, lang)
            if text:
                return text
            logger.debug("LexWork failed for %s/%s, trying LexFind", canton, number)

        # LexFind fallback
        if lexfind_id:
            text = self._fetch_from_lexfind(canton, number, lexfind_id, lang)
            if text:
                return text

        return None

    def _fetch_from_lexwork(self, canton: str, number: str,
                            lang: str = "de") -> CantonalLawText | None:
        """Fetch law text from LexWork API."""
        data = self.fetch_lexwork_law(canton, number, lang)
        if not data:
            return None

        tol = data.get("text_of_law", {})
        sv = tol.get("selected_version", {})
        xhtml = sv.get("xhtml_tol", "")
        if not xhtml:
            return None

        title = tol.get("title", "")
        abbr = tol.get("abbreviation", "")

        # publication_enactment = current version's effective date
        version_date = None
        pub_enact = tol.get("publication_enactment", "")
        if pub_enact:
            try:
                version_date = date.fromisoformat(pub_enact[:10])
            except ValueError:
                pass
        # Fallback: parse from version_dates_str
        if not version_date:
            vds = sv.get("version_dates_str", "")
            m = re.search(r"seit:\s*(\d{2})\.(\d{2})\.(\d{4})", vds)
            if m:
                try:
                    version_date = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
                except ValueError:
                    pass
        # Last fallback: enactment (original law date)
        if not version_date:
            enactment = tol.get("enactment", "")
            if enactment:
                try:
                    version_date = date.fromisoformat(enactment[:10])
                except ValueError:
                    pass

        return CantonalLawText(
            canton=canton,
            systematic_number=number,
            title=title,
            html_content=xhtml,
            language=lang,
            version_date=version_date,
            abbreviation=abbr,
            origin="lexwork",
        )

    def _fetch_from_lexfind(self, canton: str, number: str,
                            tol_id: str, lang: str = "de") -> CantonalLawText | None:
        """Fetch law text from LexFind PDF and extract via pdftotext."""
        if not tol_id:
            return None

        pdf_url = f"https://www.lexfind.ch/tol/{tol_id}/{lang}"
        pdf_bytes = self._get_pdf(pdf_url)
        if not pdf_bytes:
            return None

        text = _pdf_to_text(pdf_bytes)
        if not text or len(text) < 50:
            logger.warning("Canton %s law %s: PDF text too short", canton.upper(), number)
            return None

        title = ""
        lines = text.strip().split("\n")
        for line in lines:
            stripped = re.sub(r"\s+", " ", line).strip()
            if not stripped:
                continue
            if re.match(r"^[\d\s.]+$", stripped):
                continue
            if re.match(r"^(Kanton|Canton|Cantone|Gesetzessammlung|Raccolta|Recueil)\b", stripped):
                continue
            title = stripped
            break

        version_date = _parse_lexfind_date(text, lang)

        return CantonalLawText(
            canton=canton,
            systematic_number=number,
            title=title,
            html_content=text,
            language=lang,
            version_date=version_date,
            origin="lexfind_pdf",
        )

    def _get_pdf(self, url: str) -> bytes | None:
        """Download a PDF with retry and rate-limiting."""
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            self._throttle()
            try:
                resp = self.session.get(url, timeout=60)
                if resp.status_code == 404:
                    return None
                if resp.status_code in RETRYABLE_HTTP_CODES and attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                    continue
                resp.raise_for_status()
                ct = resp.headers.get("content-type", "")
                if "pdf" not in ct:
                    logger.warning("Expected PDF, got %s for %s", ct, url)
                    return None
                return resp.content
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= BACKOFF_FACTOR
                else:
                    logger.error("Failed to download PDF %s: %s", url, e)
        return None

    def _fetch_from_zurich(self, number: str, lang: str = "de",
                           erlass_id: str = "") -> CantonalLawText | None:
        from .zurich_fetcher import ZurichFetcher
        zh_fetcher = ZurichFetcher(rate_limit=self.rate_limit)
        text = zh_fetcher.fetch_law_text(number, lang, erlass_id=erlass_id)
        if text:
            text.origin = text.origin or "zhlex"
        return text

    def _fetch_from_geneve(self, number: str, lang: str = "fr",
                           filename: str = "") -> CantonalLawText | None:
        from .cantonal_scrapers import GeneveFetcher
        fetcher = GeneveFetcher(rate_limit=self.rate_limit)
        text = fetcher.fetch_law_text(number, lang, filename=filename)
        if text:
            text.origin = text.origin or "lexfind"
        return text

    def _fetch_from_neuchatel(self, number: str, lang: str = "fr",
                              filename: str = "") -> CantonalLawText | None:
        from .cantonal_scrapers import NeuchatelFetcher
        fetcher = NeuchatelFetcher(rate_limit=self.rate_limit)
        text = fetcher.fetch_law_text(number, lang, filename=filename)
        if text:
            text.origin = text.origin or "lexfind"
        return text

    def fetch_versions(self, canton: str, number: str) -> list[CantonalLawVersion]:
        """Fetch all available versions of a cantonal law."""
        # Zürich: dedicated fetcher
        if canton == "zh":
            from .zurich_fetcher import ZurichFetcher
            zh_fetcher = ZurichFetcher(rate_limit=self.rate_limit)
            return zh_fetcher.fetch_versions(number)

        if canton not in LEXWORK_CANTONS:
            return []

        data = self.fetch_lexwork_law(canton, number)
        if not data:
            return []

        tol = data.get("text_of_law", {})
        versions = []

        # Current version
        cv = tol.get("current_version", {})
        if cv:
            since, until = _parse_version_dates_str(cv.get("version_dates_str", "")
                                                    or tol.get("text_of_law_dates_str", ""))
            versions.append(CantonalLawVersion(
                canton=canton,
                systematic_number=number,
                version_id=cv.get("id", 0),
                title=cv.get("title", tol.get("title", "")),
                date_in_force=since,
                date_until=until,
                abbreviation=cv.get("abbreviation", ""),
            ))

        # Old versions
        for ov in tol.get("old_versions", []):
            since, until = _parse_version_dates_str(ov.get("version_dates_str", ""))
            versions.append(CantonalLawVersion(
                canton=canton,
                systematic_number=number,
                version_id=ov.get("id", 0),
                title=ov.get("title", ""),
                date_in_force=since,
                date_until=until,
                abbreviation=ov.get("abbreviation", ""),
            ))

        return versions

    def fetch_law_dates(self, canton: str, number: str) -> LawDates | None:
        """Fetch enactment date + all version dates for one LexWork law.

        One API call: the payload's ``text_of_law.date_of_decision`` is the
        original enactment (ISO); current + old versions carry their
        in-force dates in ``version_dates_str``.
        """
        if canton not in LEXWORK_CANTONS:
            return None
        data = self.fetch_lexwork_law(canton, number)
        if not data:
            return None
        tol = data.get("text_of_law", {})

        enactment = None
        dod = str(tol.get("date_of_decision") or "")[:10]
        if dod:
            try:
                enactment = date.fromisoformat(dod)
            except ValueError:
                pass
        if not enactment:
            m = re.search(r"vom\s+(\d{2})\.(\d{2})\.(\d{4})",
                          str(tol.get("text_of_law_dates_str", "")))
            if m:
                try:
                    enactment = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
                except ValueError:
                    pass

        version_dates: set[date] = set()
        for v in [tol.get("current_version") or {}] + list(tol.get("old_versions", [])):
            since, _ = _parse_version_dates_str(v.get("version_dates_str", ""))
            if since:
                version_dates.add(since)
        # The overall dates string carries the current version's in-force date
        since, _ = _parse_version_dates_str(str(tol.get("text_of_law_dates_str", "")))
        if since:
            version_dates.add(since)

        return LawDates(
            canton=canton,
            systematic_number=number,
            enactment_date=enactment,
            version_dates=sorted(version_dates),
        )

    def fetch_version_text(self, canton: str, number: str,
                           version_id: int, lang: str = "de") -> CantonalLawText | None:
        """Fetch a specific version's text from LexWork."""
        if canton not in LEXWORK_CANTONS:
            return None

        data = self.fetch_lexwork_version(canton, number, version_id)
        if not data:
            return None

        tol = data.get("text_of_law", {})
        sv = tol.get("selected_version", {})
        xhtml = sv.get("xhtml_tol", "")
        if not xhtml:
            return None

        version_date = None
        vds = sv.get("version_dates_str", "")
        m = re.search(r"seit:\s*(\d{2})\.(\d{2})\.(\d{4})", vds)
        if m:
            try:
                version_date = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            except ValueError:
                pass

        return CantonalLawText(
            canton=canton,
            systematic_number=number,
            title=sv.get("title", tol.get("title", "")),
            html_content=xhtml,
            language=lang,
            version_date=version_date,
            abbreviation=sv.get("abbreviation", ""),
            origin="lexwork",
        )


_DDMMYYYY = r"(\d{2})\.(\d{2})\.(\d{4})"


def _parse_version_dates_str(vds: str) -> tuple[date | None, date | None]:
    """Parse a LexWork version date string into (in_force_since, until).

    Handles the observed formats across de/fr portals:
    - "Version in Kraft seit: 01.05.2024"
    - "Version in Kraft von: 01.05.2024 bis: 29.06.2024"
    - "vom 25.06.1980, in Kraft seit: 01.01.1982"
    - "Version en vigueur depuis le: 01.01.2010" / "du: ... au: ..."
    """
    def _mk(m) -> date | None:
        try:
            return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
        except (ValueError, AttributeError):
            return None

    vds = str(vds or "")
    since = until = None
    m = re.search(rf"(?:seit|depuis(?:\s+le)?|dal)\s*:?\s*{_DDMMYYYY}", vds)
    if m:
        since = _mk(m)
    else:
        m = re.search(rf"(?:von|du)\s*:?\s*{_DDMMYYYY}", vds)
        if m:
            since = _mk(m)
    m = re.search(rf"(?:bis|au|al)\s*:?\s*{_DDMMYYYY}", vds)
    if m:
        until = _mk(m)
    return since, until


# ─── PDF extraction helpers ───────────────────────────────────────────────────

def _pdf_to_text(pdf_bytes: bytes) -> str:
    """Extract text from PDF bytes using pdftotext."""
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=True) as f:
        f.write(pdf_bytes)
        f.flush()
        try:
            result = subprocess.run(
                ["pdftotext", "-layout", f.name, "-"],
                capture_output=True, text=True, timeout=30,
            )
            if result.returncode != 0:
                logger.warning("pdftotext failed: %s", result.stderr.strip())
                return ""
            return result.stdout
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            logger.error("pdftotext error: %s", e)
            return ""


_DE_MONTHS = {
    "januar": 1, "februar": 2, "märz": 3, "april": 4,
    "mai": 5, "juni": 6, "juli": 7, "august": 8,
    "september": 9, "oktober": 10, "november": 11, "dezember": 12,
}

_FR_MONTHS = {
    "janvier": 1, "février": 2, "mars": 3, "avril": 4,
    "mai": 5, "juin": 6, "juillet": 7, "août": 8,
    "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12,
    "fevrier": 2, "aout": 8, "decembre": 12,
}

_IT_MONTHS = {
    "gennaio": 1, "febbraio": 2, "marzo": 3, "aprile": 4,
    "maggio": 5, "giugno": 6, "luglio": 7, "agosto": 8,
    "settembre": 9, "ottobre": 10, "novembre": 11, "dicembre": 12,
}


def _parse_lexfind_date(text: str, lang: str) -> date | None:
    """Parse version date from LexFind PDF text header.

    Looks for patterns like:
      - German: "vom 24. November 1872 (Stand 1. Mai 2022)" → extracts Stand date
      - French: "du 15 mars 2005 (état le 1er janvier 2023)" → extracts état date
      - Italian: "del 15 marzo 2005 (stato 1° gennaio 2023)" → extracts stato date
    Falls back to the enactment date if no Stand/état/stato found.
    """
    months = _DE_MONTHS if lang == "de" else _IT_MONTHS if lang == "it" else _FR_MONTHS

    # Try Stand/état/stato date first (most current version date)
    stand_patterns = [
        r"(?:Stand|état\s+le|stato)\s+(\d{1,2})\.?\s*(?:er|°)?\s*(\w+)\s+(\d{4})",
    ]
    for pat in stand_patterns:
        m = re.search(pat, text[:2000], re.IGNORECASE)
        if m:
            d = _month_date(m.group(1), m.group(2), m.group(3), months)
            if d:
                return d

    # Fallback: enactment date
    enact_patterns = [
        r"(?:vom|du|del)\s+(\d{1,2})\.?\s*(?:er|°)?\s*(\w+)\s+(\d{4})",
    ]
    for pat in enact_patterns:
        m = re.search(pat, text[:2000], re.IGNORECASE)
        if m:
            d = _month_date(m.group(1), m.group(2), m.group(3), months)
            if d:
                return d

    return None


def _month_date(day_s: str, month_s: str, year_s: str,
                months: dict[str, int]) -> date | None:
    m = months.get(month_s.lower())
    if not m:
        return None
    try:
        return date(int(year_s), m, int(day_s))
    except ValueError:
        return None


# ─── Path helpers ──────────────────────────────────────────────────────────────

def canton_to_path(canton: str, systematic_number: str, language: str) -> str:
    """Convert cantonal law identifiers to a file path.

    Structure: ch/{canton}/{lang}/{number}.md

    Examples:
        ch/bs/de/300.100.md
        ch/zh/de/131.1.md
        ch/ge/fr/A.2.05.md

    This mirrors the federal structure (ch/de/, ch/fr/, ch/it/) but scoped
    per canton, keeping language variants of the same law in separate dirs.
    """
    return f"ch/{canton}/{language}/{systematic_number}.md"


def cantonal_law_to_markdown(
    text: CantonalLawText,
    entry: CantonalLawEntry | None = None,
) -> str:
    """Convert cantonal law text to Markdown with frontmatter.

    Uses the cantonal transformer which handles source-specific HTML formats:
    - LexWork XHTML: converts single-row tables to lists, formats § headings
    - LexFind HTML: extracts body from full-page HTML, strips navigation
    - ZHLex HTML: handles Zürich's semantic HTML structure
    """
    # Prefer the recorded text origin; fall back to canton-based inference
    # for texts produced before the origin field existed.
    text_source = text.origin or (
        "zhlex" if text.canton == "zh"
        else "lexwork" if text.canton in LEXWORK_CANTONS
        else "lexfind_pdf" if text.canton in LEXFIND_ONLY_CANTONS
        else "lexfind"
    )
    source_label = {
        "zhlex": "LexFind+ZHLex",
        "lexwork": "LexFind+LexWork",
    }.get(text_source, "LexFind")

    meta: dict[str, object] = {
        "canton": text.canton.upper(),
        "systematic_number": text.systematic_number,
        "title": text.title,
        "language": text.language,
        "source": source_label,
    }
    if text.version_date:
        meta["version_date"] = text.version_date.isoformat()
    if text.abbreviation:
        meta["abbreviation"] = text.abbreviation
    if entry:
        if entry.systematic_category:
            meta["systematic_category"] = entry.systematic_category
        if entry.global_category:
            meta["global_category"] = entry.global_category
        if entry.category_type:
            meta["category_type"] = entry.category_type

    import yaml
    frontmatter = "---\n" + yaml.dump(meta, allow_unicode=True, default_flow_style=False).strip() + "\n---"

    body = transform_cantonal_html(text.html_content, source=text_source) if text.html_content else ""
    if not body:
        body = f"# {text.title}\n\n*No text content available.*"

    return frontmatter + "\n\n" + body + "\n"
