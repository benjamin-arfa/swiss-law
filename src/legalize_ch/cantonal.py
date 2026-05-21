"""Fetch cantonal law from LexWork (direct) with LexFind fallback."""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import date

import requests

from .cantonal_transformer import transform_cantonal_html
from .transformer import html_to_markdown, build_frontmatter

logger = logging.getLogger(__name__)

# Retry configuration
MAX_RETRIES = 4
INITIAL_BACKOFF = 2.0
BACKOFF_FACTOR = 2.0
RETRYABLE_HTTP_CODES = {429, 500, 502, 503, 504}

# ─── LexFind API (new Angular backend, live as of 2026-05) ──────────────────────
#
# The legacy ``/fe/api/search`` endpoint is dead (returns the SPA shell). LexFind
# now exposes a JSON API under ``/api/fe/{lang}/`` which we use as the *catalog*
# source for every canton — it enumerates law systematic numbers. The actual law
# *text* still comes from each canton's LexWork portal (clean XHTML).
LEXFIND_API = "https://www.lexfind.ch/api/fe"

# Catalogs are enumerated by a content full-text search for a near-universal
# stopword, filtered to one canton (entity). One stopword per content language.
CATALOG_STOPWORDS = {"de": "der", "fr": "de", "it": "di", "rm": "e"}

# Page size for paginating LexFind search results.
LEXFIND_PAGE_SIZE = 100

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
    "ai", "ge", "ju", "ne", "nw", "ow", "sh", "sz", "ti", "ur", "vd",
]

# Cantons with dedicated fetchers (not LexWork, not generic LexFind)
DEDICATED_FETCHER_CANTONS = ["zh"]

ALL_CANTONS = sorted(
    list(LEXWORK_CANTONS.keys()) + LEXFIND_ONLY_CANTONS + DEDICATED_FETCHER_CANTONS
)


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
    lexfind_id: str = ""  # LexFind TOL ID for fallback


@dataclass
class CantonalLawVersion:
    """A specific version of a cantonal law."""
    canton: str
    systematic_number: str
    version_id: int | str
    title: str
    date_in_force: date | None = None
    abbreviation: str = ""


@dataclass
class CantonalLawText:
    """Full text of a cantonal law version."""
    canton: str
    systematic_number: str
    title: str
    html_content: str = ""
    language: str = "de"
    version_date: date | None = None
    abbreviation: str = ""


# ─── Fetcher ───────────────────────────────────────────────────────────────────

class CantonalFetcher:
    """Fetches cantonal law from LexWork portals with LexFind fallback."""

    def __init__(self, rate_limit: float = 1.0):
        self.rate_limit = rate_limit
        self._last_request = 0.0
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "legalize-ch/0.1 (swiss-law pipeline)"
        # canton abbreviation -> LexFind entity id, populated lazily per language
        self._entity_ids: dict[str, dict[str, int]] = {}

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

    def fetch_lexwork_catalog(self, canton: str, lang: str = "de") -> list[CantonalLawEntry]:
        """Fetch full catalog from a canton via its best available source."""
        # Zürich: dedicated ZHLex API
        if canton == "zh":
            from .zurich_fetcher import ZurichFetcher
            zh_fetcher = ZurichFetcher(rate_limit=self.rate_limit)
            return zh_fetcher.fetch_catalog(lang)

        # LexWork doesn't have a clean catalog API, but we can paginate through search
        # For now, use LexFind as the catalog source even for LexWork cantons
        return self.fetch_lexfind_catalog(canton, lang)

    # ─── LexFind API (catalog source for every canton) ─────────────────────────

    def _lexfind_entity_id(self, canton: str, lang: str = "de") -> int | None:
        """Resolve a canton abbreviation to its LexFind entity id.

        LexFind keys laws by numeric "entity" ids (cantons + the Confederation +
        communes). ``/api/fe/{lang}/entities`` maps abbreviations to ids; the
        result is cached per language for the lifetime of the fetcher.
        """
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

    def fetch_lexfind_catalog(self, canton: str, lang: str = "de") -> list[CantonalLawEntry]:
        """Enumerate a canton's laws via the LexFind full-text search API.

        LexFind has no plain "list every law" endpoint, but a content search for
        a near-universal stopword (e.g. "der") scoped to one canton returns the
        whole corpus. We create a search resource, then page through its results.
        """
        entity_id = self._lexfind_entity_id(canton, lang)
        if entity_id is None:
            logger.warning("Canton %s has no LexFind entity for lang=%s", canton.upper(), lang)
            return []

        stopword = CATALOG_STOPWORDS.get(lang, CATALOG_STOPWORDS["de"])
        body = {
            "search_text": stopword,
            "active_only": False,
            "search_in_systematic_number": False,
            "search_in_title": False,
            "search_in_keywords": False,
            "search_in_content": True,
            "use_global_systematics": False,
            "entity_filter": [entity_id],
            "systematic_filter": [],
            "category_filter": [],
            "direct_search": False,
        }
        created = self._post_json(f"{LEXFIND_API}/{lang}/fulltext-search", body)
        if not isinstance(created, dict) or "id" not in created:
            logger.warning("LexFind search creation failed for %s: %r", canton.upper(), created)
            return []

        search_id = created["id"]
        session_id = created.get("session_id", "")
        entries: dict[str, CantonalLawEntry] = {}  # keyed by tol id, deduplicated
        page = 1
        while True:
            url = (
                f"{LEXFIND_API}/{lang}/fulltext-search/{search_id}"
                f"?session_id={session_id}&page_no={page}&results_per_page={LEXFIND_PAGE_SIZE}"
            )
            data = self._get_json(url)
            if not isinstance(data, dict):
                break
            matches = data.get("texts_of_law_with_matches", [])
            for item in matches:
                entry = self._lexfind_entry(canton, item)
                if entry:
                    entries.setdefault(entry.lexfind_id or entry.systematic_number, entry)
            total_pages = data.get("number_of_pages", 0) or 0
            if page >= total_pages or not matches:
                break
            page += 1

        logger.info("LexFind catalog for %s: %d laws", canton.upper(), len(entries))
        return list(entries.values())

    @staticmethod
    def _lexfind_entry(canton: str, item: dict) -> CantonalLawEntry | None:
        """Build a CantonalLawEntry from a LexFind search-result row."""
        sr = str(item.get("systematic_number", "")).strip()
        if not sr:
            return None
        tol_id = str(item.get("id", ""))
        # The newest version's metadata sits in the first `matches` element.
        match = (item.get("matches") or [{}])[0]
        title = str(match.get("title", "")).strip()
        enactment = None
        for key in ("version_active_since", "family_active_since"):
            raw = match.get(key)
            if raw:
                try:
                    d, m, y = raw.split(".")
                    enactment = date(int(y), int(m), int(d))
                    break
                except (ValueError, AttributeError):
                    pass
        return CantonalLawEntry(
            canton=canton,
            systematic_number=sr,
            title=title,
            enactment_date=enactment,
            is_active=bool(item.get("is_active", True)),
            lexfind_id=tol_id,
        )

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
        # Dedicated fetcher (Zürich)
        if canton == "zh":
            return self._fetch_from_zurich(number, lang, erlass_id=lexfind_id)

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
            import re
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
        )

    def _fetch_from_lexfind(self, canton: str, number: str,
                            tol_id: str, lang: str = "de") -> CantonalLawText | None:
        """Fetch law text for a LexFind-only canton.

        LexFind serves the document itself only as a PDF (``/tol/{id}/{lang}``),
        not as HTML. Until PDF text extraction is wired in, LexFind-only cantons
        (AI, GE, JU, NE, NW, OW, SH, SZ, TI, UR, VD) yield a catalog but no text.
        The 14 LexWork cantons and ZH are unaffected — they have structured text.
        """
        logger.info(
            "Canton %s law %s: text only available as PDF on LexFind — skipping "
            "(LexFind-only cantons need PDF extraction; not yet supported)",
            canton.upper(), number,
        )
        return None

    def _fetch_from_zurich(self, number: str, lang: str = "de",
                           erlass_id: str = "") -> CantonalLawText | None:
        """Fetch law text from the ZHLex API (Zürich dedicated fetcher)."""
        from .zurich_fetcher import ZurichFetcher
        zh_fetcher = ZurichFetcher(rate_limit=self.rate_limit)
        return zh_fetcher.fetch_law_text(number, lang, erlass_id=erlass_id)

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
            versions.append(CantonalLawVersion(
                canton=canton,
                systematic_number=number,
                version_id=cv.get("id", 0),
                title=cv.get("title", tol.get("title", "")),
                abbreviation=cv.get("abbreviation", ""),
            ))

        # Old versions
        for ov in tol.get("old_versions", []):
            import re
            vid = ov.get("id", 0)
            title = ov.get("title", "")
            # Parse date from version_dates_str
            vds = ov.get("version_dates_str", "")
            d = None
            m = re.search(r"seit:\s*(\d{2})\.(\d{2})\.(\d{4})", vds)
            if m:
                try:
                    d = date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
                except ValueError:
                    pass
            versions.append(CantonalLawVersion(
                canton=canton,
                systematic_number=number,
                version_id=vid,
                title=title,
                date_in_force=d,
                abbreviation=ov.get("abbreviation", ""),
            ))

        return versions

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

        import re
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
        )


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


def cantonal_law_to_markdown(text: CantonalLawText) -> str:
    """Convert cantonal law text to Markdown with frontmatter.

    Uses the cantonal transformer which handles source-specific HTML formats:
    - LexWork XHTML: converts single-row tables to lists, formats § headings
    - LexFind HTML: extracts body from full-page HTML, strips navigation
    - ZHLex HTML: handles Zürich's semantic HTML structure
    """
    source = (
        "zhlex" if text.canton == "zh"
        else "lexwork" if text.canton in LEXWORK_CANTONS
        else "lexfind"
    )
    meta = {
        "canton": text.canton.upper(),
        "systematic_number": text.systematic_number,
        "title": text.title,
        "language": text.language,
        "source": (
            "ZHLex" if source == "zhlex"
            else "LexWork" if source == "lexwork"
            else "LexFind"
        ),
    }
    if text.version_date:
        meta["version_date"] = text.version_date.isoformat()
    if text.abbreviation:
        meta["abbreviation"] = text.abbreviation

    import yaml
    frontmatter = "---\n" + yaml.dump(meta, allow_unicode=True, default_flow_style=False).strip() + "\n---"

    body = transform_cantonal_html(text.html_content, source=source) if text.html_content else ""
    if not body:
        body = f"# {text.title}\n\n*No text content available.*"

    return frontmatter + "\n\n" + body + "\n"
