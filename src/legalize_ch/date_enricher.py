"""Enactment-date enrichment — laws are (law, version) pairs.

Each law file's ``version_date`` is only the CURRENT consolidated version's
entry into force. This module back-fills the missing dimension:

- ``enactment_date`` (+ ``enactment_date_source``): the original act's date —
  parsed from the stored text ("vom 25. Juni 1980" / "du 25 juin 1980" /
  "del 25 giugno 1980"), from git history (federal: every consolidation
  revision is a dated commit), or from the LexWork API
  (``date_of_decision``, authoritative).
- ``version_dates`` (+ ``version_dates_source``): all known version
  in-force dates (git history for federal, LexWork/ZHLex APIs for cantons).

Source fields are never overwritten; passes are idempotent.
"""
from __future__ import annotations

import json
import logging
import re
import subprocess
from collections import defaultdict
from datetime import date
from pathlib import Path

from .cantonal import (
    _DE_MONTHS,
    _FR_MONTHS,
    _IT_MONTHS,
    LEXWORK_CANTONS,
    CantonalFetcher,
)
from .category_enricher import _parse_frontmatter, _write_frontmatter

logger = logging.getLogger(__name__)

DATE_STATE_DIR = "data/state"


# ─── Enactment parsing from stored text ───────────────────────────────────────

_MONTHS_BY_LANG = {"de": _DE_MONTHS, "fr": _FR_MONTHS, "it": _IT_MONTHS}

# "vom 25. Juni 1980" / "du 25 juin 1980" / "del 25 giugno 1980" / "dal 1° ..."
_SPELLED_RE = re.compile(
    r"\b(?:vom|du|del|dal|dals?)\s+(\d{1,2})(?:\.|er|°)?\s+([A-Za-zäöüéûîè]+)\s+(\d{4})",
    re.IGNORECASE,
)
# "vom 25.06.1980"
_NUMERIC_RE = re.compile(r"\b(?:vom|du|del|dal)\s+(\d{1,2})\.(\d{1,2})\.(\d{4})")
# "(Stand am 1. Januar 2024)" / "(état le ...)" / "(stato ...)" — NOT enactment
_STAND_RE = re.compile(r"\((?:Stand|état|stato|Fassung)[^)]*\)", re.IGNORECASE)


def parse_enactment(body: str, title: str = "", lang: str = "de") -> date | None:
    """Extract the original enactment date from a law's title/body text."""
    months = _MONTHS_BY_LANG.get(lang, _DE_MONTHS)
    all_months = {**_DE_MONTHS, **_FR_MONTHS, **_IT_MONTHS}

    for text in (title, _STAND_RE.sub("", body[:3000])):
        if not text:
            continue
        m = _SPELLED_RE.search(text)
        if m:
            month = months.get(m.group(2).lower()) or all_months.get(m.group(2).lower())
            if month:
                try:
                    return date(int(m.group(3)), month, int(m.group(1)))
                except ValueError:
                    pass
        m = _NUMERIC_RE.search(text)
        if m:
            try:
                return date(int(m.group(3)), int(m.group(2)), int(m.group(1)))
            except ValueError:
                pass
    return None


# ─── Federal version history from git ─────────────────────────────────────────

def federal_dates_from_git(repo_path: str | Path) -> dict[str, list[str]]:
    """One git-log walk → {relative_path: sorted ISO date list} for ch/ files.

    Every federal consolidation revision is a commit author-dated with the
    version's entry-into-force date, so per-file commit dates ARE the
    version history.
    """
    result = subprocess.run(
        ["git", "-C", str(repo_path), "log", "--name-only",
         "--format=%x00%ad", "--date=short", "--", "ch/"],
        capture_output=True, text=True, timeout=600,
    )
    dates_by_path: dict[str, set[str]] = defaultdict(set)
    current = None
    for line in result.stdout.splitlines():
        if line.startswith("\x00"):
            current = line[1:].strip()
        elif line.strip() and current:
            dates_by_path[line.strip()].add(current)
    return {p: sorted(ds) for p, ds in dates_by_path.items()}


# ─── Frontmatter update ───────────────────────────────────────────────────────

def _clamped(enactment: date, fm: dict) -> bool:
    """Enactment must not postdate the current version."""
    vd = str(fm.get("version_date", ""))
    if len(vd) >= 10:
        try:
            return enactment <= date.fromisoformat(vd[:10])
        except ValueError:
            return True
    return True


# Provenance ranking: higher wins. Authoritative API data upgrades
# weaker parses; equal or weaker provenance never overwrites.
# lexfind_family = the family's ORIGINAL date from LexFind's frontend API
# (the exact "earliest known existence" concept) — outranks LexWork's
# date_of_decision, which can be a canton's accession decision.
_SOURCE_RANK = {"lexfind_family": 4, "lexwork_api": 3, "fedlex": 3,
                "sibling": 2, "git_history": 1, "text": 1, "title": 1, "": 0}


def _rank(source: str) -> int:
    return _SOURCE_RANK.get(str(source).split(":")[0], 0)


def update_file_dates(path: Path, enactment: date | None, enactment_source: str,
                      version_dates: list[str] | None = None,
                      version_dates_source: str = "") -> bool:
    """Inject date fields into a law file. Idempotent; fills missing values
    and upgrades values whose provenance ranks strictly lower."""
    text = path.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)
    if fm is None:
        return False

    changed = False
    existing_src = str(fm.get("enactment_date_source", ""))
    if enactment and _clamped(enactment, fm) and (
            not fm.get("enactment_date") or _rank(enactment_source) > _rank(existing_src)):
        if str(fm.get("enactment_date", "")) != enactment.isoformat() \
                or existing_src != enactment_source:
            fm["enactment_date"] = enactment.isoformat()
            fm["enactment_date_source"] = enactment_source
            changed = True
    existing_vsrc = str(fm.get("version_dates_source", ""))
    if version_dates and len(version_dates) > 1 and (
            not fm.get("version_dates") or _rank(version_dates_source) > _rank(existing_vsrc)):
        new_vd = sorted(set(version_dates))
        if fm.get("version_dates") != new_vd or existing_vsrc != version_dates_source:
            fm["version_dates"] = new_vd
            fm["version_dates_source"] = version_dates_source
            changed = True

    if not changed:
        return False
    path.write_text(_write_frontmatter(fm, body), encoding="utf-8")
    return True


# ─── Local passes (no API calls) ──────────────────────────────────────────────

def enrich_dates_local(repo_path: str | Path, limit: int | None = None,
                       dry_run: bool = False) -> dict:
    """Cheap local pass: text-parse enactment for every law; git history
    version dates for federal files. No network."""
    repo = Path(repo_path)
    logger.info("Walking git history for federal version dates...")
    git_dates = federal_dates_from_git(repo)

    stats = {"scanned": 0, "text": 0, "git_history": 0,
             "versions_git": 0, "unchanged": 0, "unparsed": 0}
    n = 0
    for md in sorted((repo / "ch").rglob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        if limit is not None and n >= limit:
            break
        text = md.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(text)
        if fm is None or not (fm.get("sr_number") or fm.get("systematic_number")):
            continue
        n += 1
        stats["scanned"] += 1
        if fm.get("enactment_date") and fm.get("version_dates"):
            stats["unchanged"] += 1
            continue

        rel = str(md.relative_to(repo))
        is_federal = not fm.get("canton")
        lang = str(fm.get("language", "de"))

        enactment = parse_enactment(body, str(fm.get("title", "")), lang)
        source = "text"
        vdates: list[str] = []
        vsource = ""
        if is_federal:
            vdates = git_dates.get(rel, [])
            vsource = "git_history"
            if not enactment and vdates:
                try:
                    enactment = date.fromisoformat(vdates[0])
                    source = "git_history"
                except ValueError:
                    enactment = None

        if not enactment and not (len(vdates) > 1):
            stats["unparsed"] += 1
            continue
        if dry_run:
            stats["text" if source == "text" else "git_history"] += 1
            continue
        if update_file_dates(md, enactment, source, vdates or None, vsource):
            stats["text" if source == "text" else "git_history"] += 1
            if len(vdates) > 1:
                stats["versions_git"] += 1
        else:
            stats["unchanged"] += 1

    logger.info("Local date pass: %s", stats)
    return stats


# ─── LexFind frontend/v1 family pass (all 26 cantons) ─────────────────────────

def enrich_dates_lexfind_families(repo_path: str | Path,
                                  cantons: list[str] | None = None,
                                  rate_limit: float = 0.1,
                                  limit: int | None = None,
                                  concordats_only: bool = False) -> dict:
    """Authoritative pass for ALL cantons via LexFind's frontend API:
    family_active_since (the act's original date) + full version dates.
    One catalog fetch per canton (systematic_number → tol id), then one
    with-version-groups call per law. Resumable via
    data/state/enrich_family_{canton}.json."""
    from .cantonal import ALL_CANTONS, CANTON_LANGUAGES
    from .categories import canonical_category_type
    from .lexfind_frontend import LexfindFrontend

    repo = Path(repo_path)
    cantons = [c.lower() for c in (cantons or ALL_CANTONS)]
    fetcher = CantonalFetcher(rate_limit=rate_limit)
    state_dir = repo / DATE_STATE_DIR
    state_dir.mkdir(parents=True, exist_ok=True)
    prefix = "enrich_family_conc" if concordats_only else "enrich_family"

    totals: dict[str, int] = defaultdict(int)
    for canton in cantons:
        lang = next((l for l in CANTON_LANGUAGES.get(canton, ["de"])
                     if l in ("de", "fr", "it")), "de")
        frontend = LexfindFrontend(rate_limit=rate_limit, lang=lang)
        state_file = state_dir / f"{prefix}_{canton}.json"
        done: set[str] = set(json.loads(state_file.read_text())) if state_file.exists() else set()

        # catalog: systematic_number -> tol id
        catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)
        tol_by_number = {e.systematic_number: e.lexfind_id for e in catalog if e.lexfind_id}

        canton_dir = repo / "ch" / canton
        files_by_number: dict[str, list[Path]] = defaultdict(list)
        for md in sorted(canton_dir.rglob("*.md")):
            fm, _ = _parse_frontmatter(md.read_text(encoding="utf-8"))
            if not fm or not fm.get("systematic_number"):
                continue
            if concordats_only and canonical_category_type(
                    str(fm.get("category_type", ""))) != "Interkantonale Vereinbarung" \
                    and str(fm.get("category_type_inferred", "")) != "Interkantonale Vereinbarung":
                continue
            files_by_number[str(fm["systematic_number"])].append(md)

        n = 0
        for number, paths in files_by_number.items():
            if number in done:
                continue
            if limit is not None and n >= limit:
                break
            tol_id = tol_by_number.get(number)
            done.add(number)
            if not tol_id:
                totals["no_tol_id"] += 1
                continue
            n += 1
            fam = frontend.fetch_family_dates(tol_id)
            if fam is None or (not fam.family_active_since and len(fam.version_dates) <= 1):
                totals["no_data"] += 1
            else:
                vdates = [d.isoformat() for d in fam.version_dates]
                for p in paths:
                    if update_file_dates(p, fam.family_active_since, "lexfind_family",
                                         vdates, "lexfind_family"):
                        totals["updated"] += 1
            if len(done) % 25 == 0:
                state_file.write_text(json.dumps(sorted(done)))
        state_file.write_text(json.dumps(sorted(done)))
        logger.info("%s: %d laws family-dated (state saved)", canton.upper(), n)

    return dict(totals)


# ─── LexFind repeal-date pass (inactive concordats) ───────────────────────────

def enrich_repeal_dates(repo_path: str | Path,
                        cantons: list[str] | None = None,
                        rate_limit: float = 0.1,
                        limit: int | None = None,
                        concordats_only: bool = False) -> dict:
    """Date the repeals: for every law LexFind marks inactive
    (``is_active: false``), fetch the family's version groups and write
    ``repealed_date`` (the last version's ``version_inactive_since``) +
    ``repealed_date_source: lexfind_family``. Without this date an act
    repealed in 1990 is indistinguishable from one repealed in 2015 —
    the chstat-2003 reconciliation needs the distinction. Resumable via
    data/state/enrich_repeal_{canton}.json."""
    from .cantonal import ALL_CANTONS, CANTON_LANGUAGES
    from .categories import canonical_category_type
    from .lexfind_frontend import LexfindFrontend

    repo = Path(repo_path)
    cantons = [c.lower() for c in (cantons or ALL_CANTONS)]
    fetcher = CantonalFetcher(rate_limit=rate_limit)
    state_dir = repo / DATE_STATE_DIR
    state_dir.mkdir(parents=True, exist_ok=True)

    totals: dict[str, int] = defaultdict(int)
    for canton in cantons:
        lang = next((l for l in CANTON_LANGUAGES.get(canton, ["de"])
                     if l in ("de", "fr", "it")), "de")
        frontend = LexfindFrontend(rate_limit=rate_limit, lang=lang)
        state_file = state_dir / f"enrich_repeal_{canton}.json"
        done: set[str] = set(json.loads(state_file.read_text())) if state_file.exists() else set()

        canton_dir = repo / "ch" / canton
        files_by_number: dict[str, list[Path]] = defaultdict(list)
        for md in sorted(canton_dir.rglob("*.md")):
            fm, _ = _parse_frontmatter(md.read_text(encoding="utf-8"))
            if not fm or not fm.get("systematic_number"):
                continue
            if fm.get("is_active") is not False or fm.get("repealed_date"):
                continue
            if concordats_only and canonical_category_type(
                    str(fm.get("category_type", ""))) != "Interkantonale Vereinbarung" \
                    and str(fm.get("category_type_inferred", "")) != "Interkantonale Vereinbarung":
                continue
            files_by_number[str(fm["systematic_number"])].append(md)
        if not files_by_number:
            continue

        catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)
        tol_by_number = {e.systematic_number: e.lexfind_id for e in catalog if e.lexfind_id}

        n = 0
        for number, paths in files_by_number.items():
            if number in done:
                continue
            if limit is not None and n >= limit:
                break
            tol_id = tol_by_number.get(number)
            done.add(number)
            if not tol_id:
                totals["no_tol_id"] += 1
                continue
            n += 1
            fam = frontend.fetch_family_dates(tol_id)
            if fam is None or not fam.inactive_since:
                totals["no_repeal_date"] += 1
            else:
                for p in paths:
                    text = p.read_text(encoding="utf-8")
                    fm, body = _parse_frontmatter(text)
                    if fm is None or fm.get("repealed_date"):
                        continue
                    fm["repealed_date"] = fam.inactive_since.isoformat()
                    fm["repealed_date_source"] = "lexfind_family"
                    p.write_text(_write_frontmatter(fm, body), encoding="utf-8")
                    totals["dated"] += 1
            if len(done) % 25 == 0:
                state_file.write_text(json.dumps(sorted(done)))
        state_file.write_text(json.dumps(sorted(done)))
        logger.info("%s: %d inactive laws repeal-dated (state saved)",
                    canton.upper(), n)

    return dict(totals)


# ─── Sibling date propagation (concordats) ────────────────────────────────────

def _normalize_title(title: str) -> str:
    import unicodedata
    t = unicodedata.normalize("NFKD", str(title).lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"\b(vom|du|del|dal)\b.*?\d{4}", "", t)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


_CONCORDAT_TYPES = {"Interkantonale Vereinbarung", "Accord intercantonal",
                    "Accordo intercantonale"}


def propagate_concordat_dates(repo_path: str | Path, dry_run: bool = False) -> dict:
    """Propagate authoritative enactment dates between member cantons.

    A concordat is the SAME act in every member canton, so its
    ``date_of_decision`` is identical everywhere. Groups concordat files
    by normalized title (per language); if ALL siblings with
    ``lexwork_api`` provenance agree on one date, that date is written to
    siblings with weaker (``text``/``sibling``) or missing dates as
    ``enactment_date_source: sibling:<CANTON>``. Authoritative fields are
    never overwritten. Run AFTER the LexWork API pass.
    """
    from .category_enricher import _parse_frontmatter, _write_frontmatter

    repo = Path(repo_path)
    groups: dict[tuple[str, str], list[tuple[Path, dict, str]]] = defaultdict(list)
    for md in sorted((repo / "ch").rglob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        text = md.read_text(encoding="utf-8")
        fm, body = _parse_frontmatter(text)
        if not fm or not fm.get("canton"):
            continue
        if fm.get("category_type") not in _CONCORDAT_TYPES:
            continue
        key = (str(fm.get("language", "de")), _normalize_title(fm.get("title", "")))
        if key[1]:
            groups[key].append((md, fm, body))

    stats = {"groups": 0, "authoritative_groups": 0, "propagated": 0,
             "conflicting_skipped": 0}
    for key, members in groups.items():
        cantons = {fm.get("canton") for _, fm, _ in members}
        if len(cantons) < 2:
            continue
        stats["groups"] += 1
        auth = {(str(fm.get("enactment_date")), str(fm.get("canton")))
                for _, fm, _ in members
                if fm.get("enactment_date_source") == "lexwork_api"
                and fm.get("enactment_date")}
        auth_dates = {d for d, _ in auth}
        if not auth_dates:
            continue
        if len(auth_dates) > 1:
            stats["conflicting_skipped"] += 1
            continue
        stats["authoritative_groups"] += 1
        the_date, source_canton = next(iter(auth))
        for md, fm, body in members:
            src = str(fm.get("enactment_date_source", ""))
            if src == "lexwork_api":
                continue
            if str(fm.get("enactment_date", "")) == the_date:
                continue
            stats["propagated"] += 1
            if not dry_run:
                fm["enactment_date"] = the_date
                fm["enactment_date_source"] = f"sibling:{source_canton}"
                md.write_text(_write_frontmatter(fm, body), encoding="utf-8")

    logger.info("Sibling propagation: %s", stats)
    return stats


# ─── LexWork API pass (long-running, resumable) ───────────────────────────────

def enrich_dates_lexwork(repo_path: str | Path, cantons: list[str] | None = None,
                         rate_limit: float = 0.1, limit: int | None = None,
                         concordats_only: bool = False) -> dict:
    """Authoritative pass for LexWork cantons: one API call per unique law →
    date_of_decision (enactment) + full version date list. Resumable via
    data/state/enrich_dates_{canton}.json.

    Rate limit defaults to 0.1s: the hosts declare no limits (no RateLimit
    headers, no robots Crawl-delay); the 429/5xx exponential backoff in the
    fetcher is the adaptive governor.
    """
    from .categories import canonical_category_type

    repo = Path(repo_path)
    cantons = [c.lower() for c in (cantons or sorted(LEXWORK_CANTONS))]
    fetcher = CantonalFetcher(rate_limit=rate_limit)
    state_dir = repo / DATE_STATE_DIR
    state_dir.mkdir(parents=True, exist_ok=True)
    state_prefix = "enrich_dates_conc" if concordats_only else "enrich_dates"

    totals: dict[str, int] = defaultdict(int)
    for canton in cantons:
        state_file = state_dir / f"{state_prefix}_{canton}.json"
        done: set[str] = set(json.loads(state_file.read_text())) if state_file.exists() else set()

        canton_dir = repo / "ch" / canton
        files_by_number: dict[str, list[Path]] = defaultdict(list)
        for md in sorted(canton_dir.rglob("*.md")):
            fm, _ = _parse_frontmatter(md.read_text(encoding="utf-8"))
            if not fm or not fm.get("systematic_number"):
                continue
            if concordats_only and canonical_category_type(
                    str(fm.get("category_type", ""))) != "Interkantonale Vereinbarung":
                continue
            files_by_number[str(fm["systematic_number"])].append(md)

        n = 0
        for number, paths in files_by_number.items():
            if number in done:
                continue
            if limit is not None and n >= limit:
                break
            n += 1
            ld = fetcher.fetch_law_dates(canton, number)
            done.add(number)
            if ld is None or (not ld.enactment_date and len(ld.version_dates) <= 1):
                totals["no_data"] += 1
            else:
                vdates = [d.isoformat() for d in ld.version_dates]
                for p in paths:
                    if update_file_dates(p, ld.enactment_date, "lexwork_api",
                                         vdates, "lexwork_api"):
                        totals["updated"] += 1
            if len(done) % 25 == 0:
                state_file.write_text(json.dumps(sorted(done)))
        state_file.write_text(json.dumps(sorted(done)))
        logger.info("%s: %d laws processed (state saved)", canton.upper(), len(done))

    return dict(totals)
