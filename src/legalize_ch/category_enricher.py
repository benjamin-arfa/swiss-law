"""Enrich cantonal law files with category metadata from LexFind.

LexFind provides three category fields for every canton's laws:
  - category_type:        Instrument type (Gesetz, Verordnung, Loi, …)
  - systematic_category:  Canton-specific topic tree node (e.g. "211 Zivilrecht")
  - global_category:      Cross-canton "domaine juridique" (e.g. "1.10.10 Verfassung")

9 cantons (AI, JU, NW, OW, SH, SZ, TI, UR, VD) already have these from
the LexFind PDF pipeline.  The other 16 (14 LexWork + ZH, GE, NE) were
bootstrapped without them.  This module back-fills the missing fields.

Fallback: when a law file can't be matched to a LexFind catalog entry,
a keyword classifier infers category_type from the title.
"""
from __future__ import annotations

import logging
import re
from pathlib import Path

import yaml

from .cantonal import (
    ALL_CANTONS,
    CANTON_LANGUAGES,
    LEXFIND_ONLY_CANTONS,
    CantonalFetcher,
    CantonalLawEntry,
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Title → category_type keyword classifier
#
# Ordered by specificity: longer / more specific patterns first.
# Each tuple: (regex pattern, category_type value).
# Matching is case-insensitive against the law title.
# ---------------------------------------------------------------------------

_TYPE_PATTERNS: list[tuple[str, str]] = [
    # German
    (r"\bVerfassung\b", "Verfassung"),
    (r"\bBundesgesetz\b", "Gesetz"),
    (r"\bGesetz\b", "Gesetz"),
    (r"\bParlamentsdekret\b", "Verordnung des Parlaments (Dekret)"),
    (r"\bDekret\b", "Verordnung des Parlaments (Dekret)"),
    (r"\bVerordnung\b", "Verordnung"),
    (r"\bReglement\b", "Reglement"),
    (r"\bBeschluss\b", "Anderes"),
    (r"\bKonkordat\b", "Interkantonale Vereinbarung"),
    (r"\bInterkantonale\b.*\b(?:Vereinbarung|Vertrag)\b", "Interkantonale Vereinbarung"),
    (r"\bStaatsvertrag\b", "Internationaler Vertrag"),
    # French
    (r"\bConstitution\b", "Constitution"),
    (r"\bLoi\b", "Loi"),
    (r"\bDécret\b", "Ordonnance parlementaire (décret)"),
    (r"\bOrdonnance\b", "Ordonnance"),
    (r"\bRèglement\b", "Règlement"),
    (r"\bArrêté\b", "Autre"),
    (r"\bConcordat\b", "Accord intercantonal"),
    (r"\bConvention\s+intercantonal", "Accord intercantonal"),
    (r"\bTraité\b", "Traité international"),
    # Italian
    (r"\bCostituzione\b", "Costituzione"),
    (r"\bLegge\b", "Legge"),
    (r"\bDecreto\s+legislativo\b", "Ordinanza parlamentaria (decreto legislativo)"),
    (r"\bDecreto\b", "Ordinanza parlamentaria (decreto legislativo)"),
    (r"\bOrdinanza\b", "Ordinanza"),
    (r"\bRegolamento\b", "Regolamento"),
    (r"\bRisoluzione\b", "Altro"),
    (r"\bConcordato\b", "Accordo intercantonale"),
    (r"\bTrattato\b", "Trattato internazionale"),
]

# Cantons that already have categories from the PDF pipeline
_ALREADY_ENRICHED = set(LEXFIND_ONLY_CANTONS)


def classify_type_from_title(title: str) -> str:
    """Infer category_type from a law's title using keyword matching.

    Returns the matched type string, or "Anderes"/"Autre"/"Altro" as default
    depending on detected language.
    """
    for pattern, cat_type in _TYPE_PATTERNS:
        if re.search(pattern, title, re.IGNORECASE):
            return cat_type
    return ""


def _detect_fallback_type(title: str, lang: str) -> str:
    """Classify with language-appropriate default."""
    result = classify_type_from_title(title)
    if result:
        return result
    defaults = {"fr": "Autre", "it": "Altro"}
    return defaults.get(lang, "Anderes")


# ---------------------------------------------------------------------------
# Frontmatter update
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict | None, str]:
    """Split a markdown file into (frontmatter_dict, body_after_frontmatter).

    Returns (None, full_text) if no valid frontmatter found.
    """
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm_str = text[4:end]
    body = text[end + 4:]  # skip \n---
    try:
        fm = yaml.safe_load(fm_str)
    except yaml.YAMLError:
        return None, text
    if not isinstance(fm, dict):
        return None, text
    return fm, body


def _write_frontmatter(fm: dict, body: str) -> str:
    """Re-serialize frontmatter + body into markdown."""
    fm_str = yaml.dump(fm, allow_unicode=True, default_flow_style=False).strip()
    return "---\n" + fm_str + "\n---" + body


def update_file_categories(
    path: Path,
    category_type: str,
    systematic_category: str,
    global_category: str,
) -> bool:
    """Inject category fields into an existing markdown file's frontmatter.

    Returns True if the file was modified.
    """
    text = path.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(text)
    if fm is None:
        return False

    changed = False
    if category_type and not fm.get("category_type"):
        fm["category_type"] = category_type
        changed = True
    if systematic_category and not fm.get("systematic_category"):
        fm["systematic_category"] = systematic_category
        changed = True
    if global_category and not fm.get("global_category"):
        fm["global_category"] = global_category
        changed = True

    if not changed:
        return False

    path.write_text(_write_frontmatter(fm, body), encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Main enrichment
# ---------------------------------------------------------------------------

def enrich_canton(
    repo_path: Path,
    canton: str,
    fetcher: CantonalFetcher,
    dry_run: bool = False,
) -> dict:
    """Enrich all law files for a canton with LexFind category metadata.

    Returns a summary dict with counts.
    """
    canton = canton.lower()
    lang = CANTON_LANGUAGES.get(canton, ["de"])[0]

    # 1. Fetch LexFind catalog (has categories for all cantons)
    logger.info("Fetching LexFind catalog for %s ...", canton.upper())
    catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)

    # Build lookup: systematic_number → entry
    cat_map: dict[str, CantonalLawEntry] = {}
    for entry in catalog:
        cat_map[entry.systematic_number] = entry

    logger.info("%s: %d catalog entries from LexFind", canton.upper(), len(cat_map))

    # 2. Find all .md files for this canton
    canton_dir = repo_path / "ch" / canton
    md_files = sorted(canton_dir.rglob("*.md"))

    matched = 0
    classified = 0
    skipped = 0
    already = 0
    total = len(md_files)

    for md_path in md_files:
        text = md_path.read_text(encoding="utf-8")
        fm, _body = _parse_frontmatter(text)
        if fm is None:
            skipped += 1
            continue

        if fm.get("category_type") and fm.get("systematic_category") and fm.get("global_category"):
            already += 1
            continue

        sys_num = fm.get("systematic_number", "")
        if isinstance(sys_num, (int, float)):
            sys_num = str(sys_num)

        # Try exact match first, then stripped match
        entry = cat_map.get(sys_num)
        if not entry:
            # Try without quotes that yaml might add
            clean = sys_num.strip("'\"")
            entry = cat_map.get(clean)

        if entry and (entry.category_type or entry.systematic_category or entry.global_category):
            if not dry_run:
                update_file_categories(
                    md_path,
                    entry.category_type,
                    entry.systematic_category,
                    entry.global_category,
                )
            matched += 1
        else:
            # Fallback: classify type from title
            title = fm.get("title", "")
            file_lang = fm.get("language", lang)
            cat_type = _detect_fallback_type(title, file_lang)
            if cat_type and not dry_run:
                update_file_categories(md_path, cat_type, "", "")
            classified += 1

    summary = {
        "canton": canton.upper(),
        "total_files": total,
        "lexfind_matched": matched,
        "title_classified": classified,
        "already_enriched": already,
        "skipped": skipped,
    }
    logger.info(
        "%s: %d matched from LexFind, %d classified from title, %d already had categories, %d skipped",
        canton.upper(), matched, classified, already, skipped,
    )
    return summary


def enrich_all(
    repo_path: Path,
    cantons: list[str] | None = None,
    rate_limit: float = 0.5,
    dry_run: bool = False,
) -> list[dict]:
    """Enrich categories for multiple cantons.

    If cantons is None, enriches all cantons that are missing categories
    (i.e. everything except the 9 LexFind-only cantons).
    """
    if cantons is None:
        cantons = [c for c in ALL_CANTONS if c not in _ALREADY_ENRICHED]

    fetcher = CantonalFetcher(rate_limit=rate_limit)
    results = []

    for canton in cantons:
        try:
            summary = enrich_canton(repo_path, canton, fetcher, dry_run=dry_run)
            results.append(summary)
        except Exception:
            logger.exception("Failed to enrich %s", canton.upper())
            results.append({"canton": canton.upper(), "error": True})

    return results
