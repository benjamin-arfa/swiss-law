"""Statistics generator — aggregate frontmatter fields across all law files."""
from __future__ import annotations

import json
import logging
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import quote

import yaml

from .categories import (
    CATEGORY_TYPE_LABELS,
    build_canton_title_map,
    build_global_title_map,
    canonical_category_type,
    canonical_global_category,
    canonical_systematic_category,
)

logger = logging.getLogger(__name__)

CONCORDAT_TYPES = {
    "Interkantonale Vereinbarung",
    "Accord intercantonal",
    "Accordo intercantonale",
}

# Earliest plausible enactment year. LexFind serves 1000-01-01 as an
# "unknown" placeholder (348 files, mostly BE 669.x), and LexWork has at
# least one century typo (ch/bs/de/561.112.md: 1019-02-01 for 2019-02-01).
# The oldest genuine entries are 1562/1564 concordats, so 1400 filters the
# sentinels without touching real data. Applied at aggregation time only —
# frontmatter keeps the raw upstream values as provenance.
MIN_PLAUSIBLE_YEAR = 1400


def _plausible_date(d: str) -> bool:
    y = str(d)[:4]
    return y.isdigit() and int(y) >= MIN_PLAUSIBLE_YEAR

ALL_CANTON_CODES = [
    "AG", "AI", "AR", "BE", "BL", "BS", "FR", "GE", "GL", "GR", "JU", "LU",
    "NE", "NW", "OW", "SG", "SH", "SO", "SZ", "TG", "TI", "UR", "VD", "VS",
    "ZG", "ZH",
]

# chstat.ch-style domains ("Concordats par domaine"), mapped from the
# top-level codes of the LexFind global systematics tree (docs/trees/global.json).
# Codes 2 (Zivilrecht), 3 (Strafrecht), 10 (Publikationen ohne Text) and laws
# without a global_category fall into "autres" so nothing is silently dropped.
CONCORDAT_DOMAINS = [
    {"key": "etat", "label_fr": "Organisation de l'état, sécurité", "label_en": "State organisation, security", "codes": ["1", "5"]},
    {"key": "sante", "label_fr": "Santé, sécurité sociale", "label_en": "Health, social security", "codes": ["8"]},
    {"key": "educ", "label_fr": "Éducation, science, culture", "label_en": "Education, science, culture", "codes": ["4"]},
    {"key": "infra", "label_fr": "Infrastructure, trafic, environnement", "label_en": "Infrastructure, transport, environment", "codes": ["7"]},
    {"key": "eco", "label_fr": "Économie, agriculture", "label_en": "Economy, agriculture", "codes": ["9"]},
    {"key": "fin", "label_fr": "Finances publiques, impôts", "label_en": "Public finance, taxes", "codes": ["6"]},
    {"key": "autres", "label_fr": "Autres / non classés", "label_en": "Other / unclassified", "codes": ["2", "3", "10"]},
]


def _parse_frontmatter(path: Path) -> tuple[dict | None, str]:
    """Parse a law file. Returns (frontmatter, body) — (None, "") if invalid."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None, ""
    if not text.startswith("---"):
        return None, ""
    end = text.find("\n---", 3)
    if end == -1:
        return None, ""
    try:
        fm = yaml.safe_load(text[4:end]) or None
    except yaml.YAMLError:
        return None, ""
    return fm, text[end + 4:]


_ARTICLE_RE = re.compile(
    r"(?:Art\.|Artikel\b|Article\b|Articolo\b)\s*(\d+[a-z]{0,3}\b|premier\b)"
    r"|^\s*§+\s*(\d+[a-z]{0,3})\b",
    re.MULTILINE,
)


def count_articles(body: str) -> int:
    """Heuristic article count: number of distinct article identifiers
    referenced as 'Art. N' / 'Article N|premier' / 'Articolo N' or a
    line-leading '§ N'.  Counting distinct IDs (not occurrences) keeps
    run-on federal texts and repeated cross-references from inflating it.
    """
    return len({m.group(1) or m.group(2) for m in _ARTICLE_RE.finditer(body)})


def collect_all_frontmatter(repo_path: str | Path = ".") -> list[dict]:
    """Scan all .md files under ch/ and return their frontmatter dicts.

    Each dict also carries ``_scope``, ``_path``, and body metrics
    ``_body_chars`` / ``_body_articles`` (used by the law index).
    """
    ch_dir = Path(repo_path) / "ch"
    if not ch_dir.exists():
        return []

    results = []
    for md in sorted(ch_dir.rglob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        fm, body = _parse_frontmatter(md)
        if fm and (fm.get("sr_number") or fm.get("systematic_number")):
            scope = "cantonal" if fm.get("canton") else "federal"
            fm["_scope"] = scope
            fm["_path"] = str(md.relative_to(repo_path))
            fm["_body_chars"] = len(body)
            fm["_body_articles"] = count_articles(body)
            results.append(fm)

    logger.info("Scanned %d law files", len(results))
    return results


def enactment_year(e: dict) -> str:
    """Best-known year the law was ORIGINALLY enacted.

    Laws are (law, version) pairs: ``version_date`` is only the current
    consolidated version. Uses the EARLIEST evidence: if the version
    history starts before the recorded enactment date (contradiction),
    the law provably existed at the earlier date. Empty string when
    nothing is known.
    """
    candidates = []
    ed = str(e.get("enactment_date", ""))
    if len(ed) >= 4 and _plausible_date(ed):
        candidates.append(ed)
    vds = e.get("version_dates")
    if isinstance(vds, list) and vds:
        plausible = [str(v) for v in vds if _plausible_date(str(v))]
        if plausible:
            candidates.append(min(plausible))
    if not candidates:
        vd = str(e.get("version_date", ""))
        if len(vd) >= 4 and _plausible_date(vd):
            candidates.append(vd)
    return min(candidates)[:4] if candidates else ""


def effective_category_type(e: dict) -> tuple[str, str]:
    """(instrument type, provenance) — LexFind first; rule-inferred fills 'Other'."""
    ct = canonical_category_type(str(e.get("category_type", "")))
    if ct and ct != "Anderes":
        return ct, "lexfind"
    inf = str(e.get("category_type_inferred", ""))
    if inf:
        return inf, f"rule:{e.get('type_inference_rule', '')}"
    return ct, "lexfind" if ct else ""


def effective_global_category(e: dict) -> tuple[str, str]:
    """(global_category value, provenance) — LexFind first, inferred second."""
    gc = str(e.get("global_category", ""))
    if gc:
        return gc, "lexfind"
    gi = str(e.get("global_category_inferred", ""))
    if gi:
        return gi, str(e.get("inference_source", "inferred"))
    return "", ""


def _group_by_identity(entries: list[dict]) -> dict[str, list[dict]]:
    """Group file-level entries by unique law identity.

    Key: ``federal/{sr_number}`` or ``{canton}/{systematic_number}``.
    """
    groups: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if e["_scope"] == "federal":
            key = f"federal/{e.get('sr_number', '')}"
        else:
            key = f"{e.get('canton', '')}/{e.get('systematic_number', '')}"
        groups[key].append(e)
    return groups


def _deduplicate(entries: list[dict]) -> list[dict]:
    """Deduplicate entries so each law counts once regardless of language.

    Groups by unique law identity (sr_number for federal,
    canton/systematic_number for cantonal), keeps the German version
    as representative, falling back to the first available.
    """
    groups = _group_by_identity(entries)

    result = []
    for group in groups.values():
        de_versions = [e for e in group if e.get("language") == "de"]
        representative = de_versions[0] if de_versions else group[0]
        representative["_languages"] = sorted(
            {e.get("language", "unknown") for e in group}
        )
        result.append(representative)

    logger.info("Deduplicated %d files → %d unique laws", len(entries), len(result))
    return result


def generate_stats(repo_path: str | Path = ".") -> dict:
    """Generate comprehensive statistics from all law frontmatter.

    All counts are deduplicated: each law counts once regardless of how
    many language versions exist.  A supplementary ``by_languages`` field
    shows the raw file-level language distribution.
    """
    all_entries = collect_all_frontmatter(repo_path)
    if not all_entries:
        return {}

    # Language distribution of files (before dedup — useful context)
    by_languages = Counter(e.get("language", "unknown") for e in all_entries)
    total_files = len(all_entries)

    # Deduplicate: one entry per unique law
    entries = _deduplicate(all_entries)

    total = len(entries)
    federal = [e for e in entries if e["_scope"] == "federal"]
    cantonal = [e for e in entries if e["_scope"] == "cantonal"]

    # ─── Per-field counters ─────────────────────────────────────────────
    by_source = Counter(e.get("source", "unknown") for e in entries)
    by_canton = Counter(e["canton"] for e in cantonal if e.get("canton"))

    # Category breakdowns (cantonal only — federal uses SR prefix categories).
    # Keys are harmonized: instrument types to their canonical German label,
    # global categories by dotted code (German tree title), canton systematics
    # by (canton, code) so language variants merge and label collisions split.
    trees_dir = Path(repo_path) / "docs" / "trees"
    global_titles = build_global_title_map(trees_dir)
    canton_titles: dict[str, dict[str, str]] = {}

    def _canton_titles(canton: str) -> dict[str, str]:
        if canton not in canton_titles:
            canton_titles[canton] = build_canton_title_map(trees_dir, canton)
        return canton_titles[canton]

    by_category_type: Counter = Counter()
    type_provenance: Counter = Counter()
    for e in cantonal:
        ct, prov = effective_category_type(e)
        if ct:
            by_category_type[ct] += 1
            type_provenance["inferred" if prov.startswith("rule:") else prov] += 1
    by_systematic_category = Counter(
        canonical_systematic_category(
            str(e.get("canton", "")), e["systematic_category"],
            _canton_titles(str(e.get("canton", "")).lower()))
        for e in cantonal if e.get("systematic_category")
    )
    by_global_category = Counter(
        canonical_global_category(e["global_category"], global_titles)
        for e in cantonal if e.get("global_category")
    )

    # Federal SR categories — use the full CH tree from LexFind if available,
    # otherwise fall back to SR number prefix matching
    ch_tree_path = Path(repo_path) / "docs" / "trees" / "ch.json"
    sr_cat_map = _build_sr_category_map(ch_tree_path)
    by_sr_category: Counter[str] = Counter()
    for e in federal:
        sr = str(e.get("sr_number", ""))
        label = sr_cat_map.get(sr, "")
        if not label:
            label = _match_sr_to_tree(sr, sr_cat_map)
        if label:
            by_sr_category[label] += 1

    # ─── Time breakdowns (version_date) ─────────────────────────────────
    by_year: Counter[str] = Counter()
    by_month: Counter[str] = Counter()
    by_year_scope: dict[str, Counter[str]] = defaultdict(Counter)

    for e in entries:
        year = enactment_year(e)
        if year:
            by_year[year] += 1
            by_year_scope[year][e["_scope"]] += 1
        vd = str(e.get("version_date", ""))
        if len(vd) >= 7 and _plausible_date(vd):
            by_month[vd[:7]] += 1

    # ─── Time x field cross-tabs ────────────────────────────────────────
    def _yearly_breakdown(field: str, scope_filter: str | None = None) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for e in entries:
            if scope_filter and e["_scope"] != scope_filter:
                continue
            val = e.get(field, "")
            year = enactment_year(e)
            if val and year:
                if field == "category_type":
                    val = effective_category_type(e)[0]
                result[year][val] += 1
        return {y: dict(counts) for y, counts in sorted(result.items())}

    category_type_by_year = _yearly_breakdown("category_type", "cantonal")
    canton_by_year = _yearly_breakdown("canton", "cantonal")

    # Canton × category_type cross-tab
    category_type_by_canton: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for e in cantonal:
        c = e.get("canton", "")
        ct = effective_category_type(e)[0]
        if c and ct:
            category_type_by_canton[c][ct] += 1

    # Year × canton × category_type 3-way cross-tab
    cat_by_canton_by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int))
    )
    for e in cantonal:
        year = enactment_year(e)
        c = e.get("canton", "")
        ct = effective_category_type(e)[0]
        if year and c and ct:
            cat_by_canton_by_year[year][c][ct] += 1

    return {
        "total_laws": total,
        "federal_laws": len(federal),
        "cantonal_laws": len(cantonal),
        "total_files": total_files,
        "by_languages": dict(by_languages.most_common()),
        "by_source": dict(by_source.most_common()),
        "by_canton": dict(by_canton.most_common()),
        "by_sr_category": dict(by_sr_category.most_common()),
        "category_type_labels": CATEGORY_TYPE_LABELS,
        "type_provenance": dict(type_provenance.most_common()),
        "by_category_type": dict(by_category_type.most_common()),
        "by_systematic_category": dict(by_systematic_category.most_common()),
        "by_global_category": dict(by_global_category.most_common()),
        "year_semantics": "enactment",
        "by_year": dict(sorted(by_year.items())),
        "by_month": dict(sorted(by_month.items())),
        "by_year_scope": {y: dict(c) for y, c in sorted(by_year_scope.items())},
        "category_type_by_year": category_type_by_year,
        "canton_by_year": canton_by_year,
        "category_type_by_canton": {c: dict(v) for c, v in sorted(category_type_by_canton.items())},
        "category_type_by_canton_by_year": {
            y: {c: dict(v) for c, v in sorted(cantons.items())}
            for y, cantons in sorted(cat_by_canton_by_year.items())
        },
    }


def generate_tags(entries: list[dict]) -> dict:
    """Build a per-law tag index from frontmatter entries.

    Returns a dict mapping each law identifier to its tags, suitable for
    serving at ``/api/v1/tags`` or embedding in a static ``tags.json``.
    """
    by_canton: dict[str, list[dict]] = defaultdict(list)
    federal: list[dict] = []

    for e in entries:
        identifier = str(e.get("systematic_number") or e.get("sr_number", ""))
        if not identifier:
            continue
        rec = {
            "id": identifier,
            "title": e.get("title", ""),
            "language": e.get("language", ""),
            "version_date": str(e.get("version_date", "")),
        }
        if e.get("canton"):
            rec["systematic_category"] = e.get("systematic_category", "")
            rec["global_category"] = e.get("global_category", "")
            rec["category_type"] = e.get("category_type", "")
            rec["source"] = e.get("source", "")
            by_canton[str(e["canton"])].append(rec)
        else:
            rec["sr_category"] = _sr_category_label(identifier)
            rec["source"] = e.get("source", "")
            federal.append(rec)

    total_files = len(federal) + sum(len(v) for v in by_canton.values())
    unique_laws = len({
        (str(e.get("canton", "")),
         str(e.get("systematic_number") or e.get("sr_number", "")))
        for e in entries
        if e.get("systematic_number") or e.get("sr_number")
    })
    return {
        "federal": federal,
        "cantonal": {k: v for k, v in sorted(by_canton.items())},
        # records are per language FILE (kept for consumers); the headline
        # total counts unique laws so languages don't inflate it
        "total": unique_laws,
        "total_files": total_files,
    }


# chstat.ch 2003 reference table ("Concordats par domaine", data-theme 1842),
# derived from the Institute of Federalism's database — frozen historical
# reference for verification. Columns: etat, sante, educ, infra, eco, fin.
CHSTAT_2003 = {
    "ZH": [21, 8, 28, 27, 13, 30], "BE": [33, 14, 43, 5, 16, 29],
    "LU": [17, 12, 19, 9, 11, 11], "UR": [17, 7, 15, 9, 9, 10],
    "SZ": [17, 8, 31, 22, 14, 4], "OW": [19, 15, 26, 11, 9, 5],
    "NW": [20, 14, 26, 11, 13, 2], "GL": [14, 9, 24, 11, 14, 11],
    "ZG": [15, 5, 19, 4, 10, 15], "FR": [17, 10, 29, 6, 14, 16],
    "SO": [31, 15, 23, 7, 22, 20], "BS": [34, 27, 36, 19, 11, 14],
    "BL": [36, 22, 40, 19, 18, 24], "SH": [14, 9, 21, 6, 8, 11],
    "AR": [11, 10, 27, 20, 13, 13], "AI": [15, 6, 20, 5, 8, 12],
    "SG": [22, 23, 50, 49, 45, 29], "GR": [14, 7, 23, 3, 7, 13],
    "AG": [22, 10, 28, 10, 16, 26], "TG": [18, 9, 38, 18, 13, 18],
    "TI": [13, 3, 18, 2, 6, 2], "VD": [20, 7, 26, 10, 12, 23],
    "VS": [14, 4, 19, 4, 7, 15], "NE": [21, 8, 31, 4, 12, 17],
    "GE": [19, 4, 19, 3, 6, 8], "JU": [19, 14, 33, 3, 6, 9],
}


def generate_chstat_comparison(entries: list[dict]) -> dict:
    """Full reconciliation of our concordats vs chstat.ch's 2003 table.

    Per canton: our concordats ENACTED on or before 2003, split into
    still-active and repealed-but-listed (LexFind ``is_active: false``);
    ``unexplained`` = chstat − (active + repealed) = concordats delisted
    from LexFind entirely (only the Institute's internal DB has them) plus
    accession-vs-decision-date noise (cantons accede to concordats at
    different times; our date is the act's decision date).
    """
    cantonal = [e for e in _deduplicate(entries) if e["_scope"] == "cantonal"]
    concordats = [
        e for e in cantonal
        if effective_category_type(e)[0] == "Interkantonale Vereinbarung"
    ]

    rows: dict[str, dict] = {
        c: {"active": 0, "repealed_listed": 0, "undated": 0,
            "enacted_after_2003": 0, "all_time": 0, "date_provenance": {}}
        for c in ALL_CANTON_CODES
    }
    group_minima = _concordat_group_minima(concordats)
    year_evidence: Counter = Counter()
    for e in concordats:
        c = str(e.get("canton", "")).upper()
        if c not in rows:
            continue
        rows[c]["all_time"] += 1
        year, evidence = earliest_known_year(e, group_minima)
        if not year:
            rows[c]["undated"] += 1
            year_evidence["undated"] += 1
            continue
        if year > "2003":
            rows[c]["enacted_after_2003"] += 1
            continue
        year_evidence[evidence] += 1
        status = "repealed_listed" if e.get("is_active") is False else "active"
        rows[c][status] += 1
        src = str(e.get("enactment_date_source", "") or "version_date_only")
        rows[c]["date_provenance"][src] = rows[c]["date_provenance"].get(src, 0) + 1

    keys6 = ["etat", "sante", "educ", "infra", "eco", "fin"]
    out_rows = {}
    diagnosis_totals: dict[str, int] = defaultdict(int)
    for c in sorted(CHSTAT_2003):
        ch = CHSTAT_2003[c]
        r = rows.get(c, {})
        explained = r.get("active", 0) + r.get("repealed_listed", 0)
        unexplained = sum(ch) - explained
        if abs(unexplained) <= 5:
            diagnosis = "reconciled"
        elif r.get("all_time", 0) >= sum(ch):
            # We hold at least as many concordats as chstat counted in
            # 2003 — the shortfall is in the DATES (fixable), not absence.
            diagnosis = "dating"
        else:
            diagnosis = "delisting_or_coverage"
        diagnosis_totals[diagnosis] += 1
        out_rows[c] = {
            "chstat_2003": dict(zip(keys6, ch)) | {"total": sum(ch)},
            "ours_enacted_until_2003": {
                "active": r.get("active", 0),
                "repealed_listed": r.get("repealed_listed", 0),
                "total": explained,
            },
            "all_time_total": r.get("all_time", 0),
            "undated": r.get("undated", 0),
            "unexplained": unexplained,
            "diagnosis": diagnosis,
            "date_provenance": r.get("date_provenance", {}),
        }
    chstat_total = sum(sum(v) for v in CHSTAT_2003.values())
    ours_total = sum(v["ours_enacted_until_2003"]["total"] for v in out_rows.values())
    return {
        "note": "Reconciliation vs chstat.ch 2003 (data-theme 1842, Institute "
                "of Federalism / LexFind). ours = concordats with EARLIEST "
                "KNOWN EVIDENCE of existence <= 2003 (own enactment date, own "
                "version history, or the sibling group's authoritative minimum "
                "when the canton's own date is unverified — a concordat is the "
                "same act in every member canton), split active / "
                "repealed_listed. Authoritative accession dates are kept: a "
                "canton that verifiably joined after 2003 is not counted. "
                "unexplained = chstat - ours: concordats delisted from LexFind "
                "entirely + accession-vs-decision-date differences (cantons "
                "accede at different times; our date is the act's decision "
                "date) + undated laws. Improve dates with "
                "enrich_dates_lexwork.sh then enrich-dates --siblings.",
        "source_chstat": "https://www.chstat.ch/fr/data-theme/1842/Concordats-par-domaine",
        "chstat_total": chstat_total,
        "ours_enacted_until_2003_total": ours_total,
        "unexplained_total": chstat_total - ours_total,
        "undated_total": sum(v["undated"] for v in out_rows.values()),
        "diagnosis_totals": dict(diagnosis_totals),
        "year_evidence_le2003": dict(year_evidence),
        "date_provenance_total": {
            k: sum(v["date_provenance"].get(k, 0) for v in out_rows.values())
            for k in {p for v in out_rows.values() for p in v["date_provenance"]}
        },
        "cantons": out_rows,
    }


def generate_unclassified_types(entries: list[dict]) -> dict:
    """Review list: every law LexFind types as 'Other', with our rule-based
    inference (or null for the residual). The audit trail behind
    ``category_type_inferred``."""
    from .domain_inference import classify_type

    rows = []
    for e in _deduplicate(entries):
        if e["_scope"] != "cantonal":
            continue
        ct = canonical_category_type(str(e.get("category_type", "")))
        if ct not in ("", "Anderes"):
            continue
        inferred = e.get("category_type_inferred")
        rule = e.get("type_inference_rule")
        if not inferred:
            result = classify_type(str(e.get("title", "")))
            if result:
                inferred, rule = result
        rows.append({
            "entity": str(e.get("canton", "")).upper(),
            "id": str(e.get("systematic_number", "")),
            "title": e.get("title", ""),
            "lexfind_type": e.get("category_type", ""),
            "inferred_type": inferred or None,
            "rule": rule or None,
        })
    classified = sum(1 for r in rows if r["inferred_type"])
    return {
        "note": "Laws LexFind files under the catch-all instrument type "
                "'Anderes/Autre/Altro', with our rule-based classification "
                "(title-leading-word rules; see type_inference_rule ids). "
                "inferred_type null = genuinely other instruments "
                "(directives, rulings, concessions, tariffs...).",
        "total": len(rows),
        "classified": classified,
        "residual": len(rows) - classified,
        "items": sorted(rows, key=lambda r: (r["entity"], r["id"])),
    }


def _ancestor_codes(code: str) -> list[str]:
    """Depth-1 and (if present) depth-2 ancestor codes: '8.10.5' → ['8', '8.10']."""
    parts = code.split(".")
    result = [parts[0]]
    if len(parts) > 1:
        result.append(f"{parts[0]}.{parts[1]}")
    return result


def _harmonized_code(e: dict, fed_map: dict[str, str]) -> tuple[str, str, str] | None:
    """(scope, code, provenance) of an entry on the harmonized taxonomy.

    Cantonal laws use their (effective) global_category; federal laws
    resolve via the fetched SR mapping, falling back to the SR top-level
    prefix. None when the entry cannot be placed on the tree.
    """
    from .categories import federal_fallback_code

    if e["_scope"] == "cantonal":
        gc, prov = effective_global_category(e)
        code = _extract_identifier(gc)
        return ("cantonal", code, prov) if code else None
    sr = str(e.get("sr_number", ""))
    code = _extract_identifier(fed_map.get(sr, ""))
    if code:
        return "federal", code, "lexfind"
    code = federal_fallback_code(sr)
    return ("federal", code, "fallback") if code else None


def generate_harmonized_categories(entries: list[dict],
                                   repo_path: str | Path = ".") -> dict:
    """Aggregate ALL laws (federal + cantonal) on the harmonized taxonomy.

    The taxonomy is LexFind's global systematics ("domaine juridique") —
    the same tree for the Confederation and all 26 cantons.  Cantonal laws
    carry ``global_category`` directly; federal laws resolve via the
    fetched SR mapping (docs/federal_global_categories.json), falling back
    to the SR top-level prefix (which mirrors the global tree by design).
    """
    from .categories import DOMAIN_EN, load_federal_global_categories

    repo = Path(repo_path)
    deduped = _deduplicate(entries)
    fed_map = load_federal_global_categories(repo)

    code_counts: dict[str, dict[str, int]] = defaultdict(lambda: {"federal": 0, "cantonal": 0})
    # Cantonal canton×type breakdowns, accumulated per depth-1/depth-2
    # ancestor node so shallow nodes can offer a secondary split.
    breakdowns: dict[str, dict[str, Counter]] = defaultdict(lambda: defaultdict(Counter))
    stats_counts = {"federal_lexfind": 0, "federal_fallback": 0,
                    "federal_unmapped": 0, "cantonal_classified": 0,
                    "cantonal_unclassified": 0}

    for e in deduped:
        hc = _harmonized_code(e, fed_map)
        if hc is None:
            key = ("cantonal_unclassified" if e["_scope"] == "cantonal"
                   else "federal_unmapped")
            stats_counts[key] += 1
            continue
        scope, code, prov = hc
        code_counts[code][scope] += 1
        if scope == "cantonal":
            stats_counts["cantonal_classified"] += 1
            stats_counts[f"cantonal_{prov}"] = stats_counts.get(f"cantonal_{prov}", 0) + 1
            canton = str(e.get("canton", "")).upper()
            ctype = effective_category_type(e)[0] or "(untyped)"
            for anc in _ancestor_codes(code):
                breakdowns[anc][canton][ctype] += 1
        else:
            stats_counts[f"federal_{prov}"] += 1

    # Annotate the multilingual global tree with rolled-up counts
    trees_dir = repo / "docs" / "trees"
    from .categories import build_global_title_map
    titles = {lang: build_global_title_map(trees_dir, lang) for lang in ("de", "fr", "it")}
    global_tree = _load_tree(trees_dir / "global.json")
    seen_codes: set[str] = set()

    def _annotate(nodes: list[dict], depth: int = 1) -> list[dict]:
        result = []
        for n in nodes:
            ident = str(n.get("identifier", ""))
            own = code_counts.get(ident, {"federal": 0, "cantonal": 0})
            if ident:
                seen_codes.add(ident)
            children = _annotate(n.get("children", []), depth + 1)
            federal = own["federal"] + sum(c["federal"] for c in children)
            cant = own["cantonal"] + sum(c["cantonal"] for c in children)
            if federal + cant == 0:
                continue
            title = {lang: m.get(ident, "") for lang, m in titles.items()
                     if m.get(ident)}
            if depth == 1 and ident in DOMAIN_EN:
                title["en"] = DOMAIN_EN[ident]
            node = {
                "identifier": ident,
                "title": title,
                "total": federal + cant,
                "federal": federal,
                "cantonal": cant,
                "own": own["federal"] + own["cantonal"],
            }
            # Secondary-split data for shallow nodes (cantonal laws only)
            if depth <= 2 and ident in breakdowns:
                per_canton = breakdowns[ident]
                node["by_canton"] = {c: sum(t.values())
                                     for c, t in sorted(per_canton.items())}
                by_type: Counter = Counter()
                for t in per_canton.values():
                    by_type.update(t)
                node["by_type"] = dict(by_type.most_common())
                node["by_canton_type"] = {c: dict(t.most_common())
                                          for c, t in sorted(per_canton.items())}
            if children:
                node["children"] = children
            result.append(node)
        return result

    tree = _annotate(global_tree)
    orphans = {c: v for c, v in code_counts.items() if c not in seen_codes}
    if orphans:
        logger.warning("Harmonized categories: %d codes not in the global tree "
                       "(%d laws)", len(orphans),
                       sum(v["federal"] + v["cantonal"] for v in orphans.values()))

    top_level = [
        {"identifier": n["identifier"], "title": n["title"],
         "total": n["total"], "federal": n["federal"], "cantonal": n["cantonal"]}
        for n in tree
    ]

    return {
        "note": "Harmonized taxonomy: LexFind global systematics ('domaine "
                "juridique') covering federal AND cantonal law. Labels per "
                "language in /api/v1/categories/global.json. Federal laws "
                "without a LexFind assignment fall back to their SR "
                "top-level prefix.",
        "counts": stats_counts,
        "top_level": top_level,
        "tree": tree,
    }


def generate_harmonized_by_year(entries: list[dict],
                                repo_path: str | Path = ".") -> dict:
    """Per-enactment-year counts on the harmonized taxonomy, depth ≤ 2.

    Companion cube to ``generate_harmonized_categories`` — kept in a
    separate file so the main endpoint's payload stays stable and the
    dashboard only fetches it when a year filter is active.  Sparse:
    only non-zero (year, code) cells are emitted, values are
    ``[federal, cantonal]`` pairs.  Undated laws (including implausible
    sentinel dates) land in the ``unknown`` bucket.
    """
    from .categories import load_federal_global_categories

    deduped = _deduplicate(entries)
    fed_map = load_federal_global_categories(Path(repo_path))

    years: dict[str, dict[str, list[int]]] = defaultdict(
        lambda: defaultdict(lambda: [0, 0]))
    unknown: dict[str, list[int]] = defaultdict(lambda: [0, 0])

    for e in deduped:
        hc = _harmonized_code(e, fed_map)
        if hc is None:
            continue
        scope, code, _ = hc
        idx = 0 if scope == "federal" else 1
        year = enactment_year(e)
        target = years[year] if year else unknown
        for anc in _ancestor_codes(code):
            target[anc][idx] += 1

    return {
        "note": "Per-enactment-year counts on the harmonized taxonomy "
                "(LexFind global systematics), depth <= 2. Values are "
                "[federal, cantonal] pairs. Titles: join "
                "/api/v1/categories/global.json or "
                "/api/v1/stats/harmonized_categories.json.",
        "year_semantics": "enactment",
        "depth": 2,
        "years": {y: dict(codes) for y, codes in sorted(years.items())},
        "unknown": dict(unknown),
    }


def _concordat_group_minima(concordats: list[dict]) -> dict[str, str]:
    """Per sibling group (normalized title): the earliest AUTHORITATIVE
    evidence date (lexwork_api enactment or version minimum). A concordat
    is the same act in every member canton — the group's earliest
    authoritative date bounds when the act existed."""
    from .date_enricher import _normalize_title

    minima: dict[str, str] = {}
    for e in concordats:
        cand = []
        if str(e.get("enactment_date_source", "")) in ("lexfind_family", "lexwork_api") \
                and e.get("enactment_date") and _plausible_date(str(e["enactment_date"])):
            cand.append(str(e["enactment_date"]))
        vds = e.get("version_dates")
        if isinstance(vds, list) and vds \
                and str(e.get("version_dates_source", "")) == "lexwork_api":
            plausible = [str(v) for v in vds if _plausible_date(str(v))]
            if plausible:
                cand.append(min(plausible))
        if not cand:
            continue
        k = _normalize_title(e.get("title", ""))
        if not k:
            continue
        m = min(cand)
        if k not in minima or m < minima[k]:
            minima[k] = m
    return minima


def earliest_known_year(e: dict, group_minima: dict[str, str]) -> tuple[str, str]:
    """(year, evidence) — earliest known evidence a concordat existed.

    Own evidence (enactment date, version history) always counts; the
    sibling group's authoritative minimum is used ONLY when the entry's
    own date provenance is weak (text-parsed or missing) — an
    authoritative accession date is canton-specific truth and is kept.
    """
    from .date_enricher import _normalize_title

    src = str(e.get("enactment_date_source", "")).split(":")[0]
    # FROZEN canonical basis (see api/v1/quality/methodology_changelog.json):
    # a lexfind_family date IS the act's original date — use it alone,
    # no mixing with version minima or sibling evidence. Sentinel dates
    # (LexFind's 1000-01-01 "unknown" placeholder) fall through instead.
    if src == "lexfind_family" and e.get("enactment_date") \
            and _plausible_date(str(e["enactment_date"])):
        return str(e["enactment_date"])[:4], "lexfind_family"
    cand: list[tuple[str, str]] = []
    if e.get("enactment_date") and _plausible_date(str(e["enactment_date"])):
        cand.append((str(e["enactment_date"]), "own_enactment"))
    vds = e.get("version_dates")
    if isinstance(vds, list) and vds:
        plausible = [str(v) for v in vds if _plausible_date(str(v))]
        if plausible:
            cand.append((min(plausible), "own_versions"))
    if src not in ("lexwork_api", "fedlex"):
        gm = group_minima.get(_normalize_title(e.get("title", "")))
        if gm:
            cand.append((gm, "sibling_group"))
    if not cand:
        vd = str(e.get("version_date", ""))
        if len(vd) >= 4 and _plausible_date(vd):
            cand.append((vd, "own_enactment"))
    if not cand:
        return "", "undated"
    d, ev = min(cand)
    return d[:4], ev


def generate_concordats_by_domain(entries: list[dict]) -> dict:
    """Tabulate intercantonal agreements (concordats) per canton per domain.

    Reproduces the layout of chstat.ch's "Concordats par domaine" table
    (which is likewise derived from LexFind data), with an extra
    "autres" column for concordats outside the six chstat domains or
    without a global_category.  Entries are deduplicated so each
    concordat counts once regardless of language versions.
    """
    cantonal = [e for e in _deduplicate(entries) if e["_scope"] == "cantonal"]
    concordats = [
        e for e in cantonal
        if effective_category_type(e)[0] == "Interkantonale Vereinbarung"
    ]
    group_minima = _concordat_group_minima(concordats)
    tab = _domain_cross_tab(
        concordats, lambda e: earliest_known_year(e, group_minima))

    return {
        "title": "Intercantonal agreements (concordats) by domain",
        "source": "LexFind (Institute of Federalism, University of Fribourg)",
        "total_concordats": tab["totals"]["total"],
        "domains": _domains_export(),
        "cantons": tab["cantons"],
        "totals": tab["totals"],
        "year_semantics": "enactment",
        "by_year": tab["by_year"],
        "by_version_year": tab["by_version_year"],
        "unclassified_in_autres": tab["unclassified_in_autres"],
        "domain_provenance": tab["domain_provenance"],
        "year_evidence": tab["year_evidence"],
        "notes": [
            "\"Other\" includes civil law, criminal law and concordats without "
            "a legal domain in LexFind's public database (~28% unclassified at the source)",
            "Coverage follows the imported collections — run backfill-lexfind "
            "to complete under-represented cantons",
            "Counting unit: canton memberships, not distinct treaties — each "
            "agreement counts once per signatory canton whose collection "
            "publishes it (a 26-canton concordat counts 26), matching the "
            "chstat.ch methodology. Distinct agreements with their signing "
            "cantons: /api/v1/stats/concordats_signatories.json",
        ],
    }


def _domains_export() -> list[dict]:
    return [
        {"key": d["key"], "label_fr": d["label_fr"], "label_en": d["label_en"],
         "global_category_codes": d["codes"]}
        for d in CONCORDAT_DOMAINS
    ]


def _domain_cross_tab(laws: list[dict], year_fn) -> dict:
    """Canton × domain accumulation shared by the concordats table and the
    per-instrument-type tables.

    ``year_fn(e) -> (year, evidence)``.  Per-year breakdowns: ``by_year``
    uses the year_fn result (enactment semantics — a 1970 act amended in
    2015 counts as 1970); ``by_version_year`` uses the current
    consolidated version's year (transparency).
    """
    code_to_key = {c: d["key"] for d in CONCORDAT_DOMAINS for c in d["codes"]}
    domain_keys = [d["key"] for d in CONCORDAT_DOMAINS]

    table: dict[str, dict[str, int]] = {
        canton: {k: 0 for k in domain_keys} for canton in ALL_CANTON_CODES
    }
    by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int)))
    by_version_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int)))
    unclassified = 0
    provenance: Counter = Counter()
    year_evidence: Counter = Counter()
    for e in laws:
        canton = str(e.get("canton", "")).upper()
        if canton not in table:
            logger.warning("Law with unknown canton %r: %s", canton, e.get("_path"))
            continue
        gc, prov = effective_global_category(e)
        top_code = _extract_identifier(gc).split(".")[0]
        key = code_to_key.get(top_code)
        if key is None:
            key = "autres"
            unclassified += 1
        else:
            provenance[prov] += 1
        table[canton][key] += 1
        year, evidence = year_fn(e)
        year_evidence[evidence] += 1
        by_year[year or "unknown"][canton][key] += 1
        vd = str(e.get("version_date", ""))
        vyear = vd[:4] if len(vd) >= 4 and _plausible_date(vd) else "unknown"
        by_version_year[vyear][canton][key] += 1

    for row in table.values():
        row["total"] = sum(row.values())
    totals = {k: sum(row[k] for row in table.values()) for k in domain_keys}
    totals["total"] = sum(totals.values())

    return {
        "cantons": table,
        "totals": totals,
        "by_year": {y: {c: dict(d) for c, d in cantons.items()}
                    for y, cantons in sorted(by_year.items())},
        "by_version_year": {y: {c: dict(d) for c, d in cantons.items()}
                            for y, cantons in sorted(by_version_year.items())},
        "unclassified_in_autres": unclassified,
        "domain_provenance": dict(provenance),
        "year_evidence": dict(year_evidence),
    }


# canonical German instrument-type label → filename slug for
# api/v1/stats/types/{slug}_by_domain.json
TYPE_SLUGS = {
    "Staatsvertrag": "staatsvertrag",
    "Interkantonale Vereinbarung": "interkantonale_vereinbarung",
    "Verfassung": "verfassung",
    "Gesetz": "gesetz",
    "Anderes": "anderes",
    "Verordnung": "verordnung",
    "Reglement": "reglement",
    "Verordnung des Parlaments (Dekret)": "dekret",
    "Gemeindeerlass": "gemeindeerlass",
}


def generate_types_by_domain(entries: list[dict],
                             concordat_override: dict | None = None) -> dict:
    """Canton × domain cross-tab per instrument type — the concordats table
    generalized to every text category.

    Returns ``{"files": {slug: table_dict}, "index": index_dict}``.  Each
    table reuses the concordats_by_domain key names (``domains``,
    ``cantons``, ``totals``, ``by_year``…) so the dashboard renders any
    type with the same code.  The intercantonal type keeps its
    provenance-ranked year logic (``earliest_known_year``); other types
    use plain ``enactment_year`` — sibling-group evidence only makes
    sense for the same act existing in several cantons.
    """
    cantonal = [e for e in _deduplicate(entries) if e["_scope"] == "cantonal"]
    by_type: dict[str, list[dict]] = defaultdict(list)
    for e in cantonal:
        ct = effective_category_type(e)[0]
        if ct in TYPE_SLUGS:
            by_type[ct].append(e)

    def _plain_year(e: dict) -> tuple[str, str]:
        y = enactment_year(e)
        return y, ("dated" if y else "undated")

    files: dict[str, dict] = {}
    index_types: list[dict] = []
    for label_de, laws in by_type.items():
        slug = TYPE_SLUGS[label_de]
        if label_de == "Interkantonale Vereinbarung":
            gm = _concordat_group_minima(laws)
            tab = _domain_cross_tab(laws, lambda e: earliest_known_year(e, gm))
        else:
            tab = _domain_cross_tab(laws, _plain_year)
        label = CATEGORY_TYPE_LABELS.get(label_de, {"de": label_de})
        notes = [
            "\"Other\" column includes civil law, criminal law and laws "
            "without a legal domain in LexFind's public database",
            "Coverage follows the imported collections — run backfill-lexfind "
            "to complete under-represented cantons",
        ]
        if label_de == "Interkantonale Vereinbarung":
            notes.append(
                "Counting unit: canton memberships, not distinct treaties — "
                "each agreement counts once per signatory canton whose "
                "collection publishes it, matching the chstat.ch methodology")
        files[slug] = {
            "title": f"Cantonal acts of type '{label_de}' by canton and domain",
            "type": {"slug": slug, "label": label},
            "source": "LexFind (Institute of Federalism, University of Fribourg)",
            "total": tab["totals"]["total"],
            "domains": _domains_export(),
            "cantons": tab["cantons"],
            "totals": tab["totals"],
            "year_semantics": "enactment",
            "by_year": tab["by_year"],
            "unclassified_in_autres": tab["unclassified_in_autres"],
            "domain_provenance": tab["domain_provenance"],
            "notes": notes,
        }
        entry = {"slug": slug, "label": label,
                 "total": tab["totals"]["total"],
                 "path": f"api/v1/stats/types/{slug}_by_domain.json"}
        if slug == "interkantonale_vereinbarung" and concordat_override:
            # keep the dashboard selector consistent with the headline
            # (chstat-calibrated) table it actually displays
            entry.update(concordat_override)
            entry["published_total"] = tab["totals"]["total"]
        index_types.append(entry)

    index_types.sort(key=lambda t: -t["total"])
    index = {
        "note": "Canton × domain cross-tabs per instrument type. Same shape "
                "as /api/v1/stats/concordats_by_domain.json.",
        "types": index_types,
    }
    return {"files": files, "index": index}


# Canton names as they appear in treaty titles, in all three languages
# (incl. spelling variants).  A canton named in an agreement's title is a
# signatory even when its own collection does not publish the text —
# ported from scripts/fetch_concordats_to_2003.py and extended with
# French/Italian variants (fr-only cantons title their copies in French).
CANTON_NAME_VARIANTS = {
    "ZH": ["Zürich", "Zurich", "Zurigo"],
    "BE": ["Bern", "Berne", "Berna"],
    "LU": ["Luzern", "Lucerne", "Lucerna"],
    "UR": ["Uri"],
    "SZ": ["Schwyz", "Schwytz", "Svitto"],
    "OW": ["Obwalden", "Obwald", "Obvaldo"],
    "NW": ["Nidwalden", "Nidwald", "Nidvaldo"],
    "GL": ["Glarus", "Glaris", "Glarona"],
    "ZG": ["Zug", "Zoug", "Zugo"],
    "FR": ["Freiburg", "Fribourg", "Friburgo"],
    "SO": ["Solothurn", "Soleure", "Soletta"],
    "BS": ["Basel-Stadt", "Bâle-Ville", "Basilea Città"],
    "BL": ["Basel-Landschaft", "Basel-Land", "Bâle-Campagne", "Basilea Campagna"],
    "SH": ["Schaffhausen", "Schaffhouse", "Sciaffusa"],
    "AR": ["Appenzell Ausserrhoden", "Appenzell A.Rh", "Appenzell AR",
           "Appenzell Rhodes-Extérieures"],
    "AI": ["Appenzell Innerrhoden", "Appenzell I.Rh", "Appenzell IR",
           "Appenzell Rhodes-Intérieures"],
    "SG": ["St.Gallen", "St. Gallen", "Sankt Gallen", "Saint-Gall", "San Gallo"],
    "GR": ["Graubünden", "Grisons", "Grigioni"],
    "AG": ["Aargau", "Argovie", "Argovia"],
    "TG": ["Thurgau", "Thurgovie", "Turgovia"],
    "TI": ["Tessin", "Ticino"],
    "VD": ["Waadt", "Vaud"],
    "VS": ["Wallis", "Valais", "Vallese"],
    "NE": ["Neuenburg", "Neuchâtel"],
    "GE": ["Genf", "Genève", "Ginevra"],
    "JU": ["Jura", "Giura"],
}
# "Basel"/"Bâle" alone (without Stadt/Landschaft) historically means BS in
# pre-1833 treaties; matched only when neither compound form is present.
_BASEL_BARE = ("Basel", "Bâle", "Basilea")


def cantons_named_in_title(title: str) -> list[str]:
    """Return the sorted canton codes explicitly named in a treaty title."""
    t = title or ""
    found = set()
    for code, variants in CANTON_NAME_VARIANTS.items():
        if any(v in t for v in variants):
            found.add(code)
    if "BS" not in found and "BL" not in found \
            and any(b in t for b in _BASEL_BARE):
        found.add("BS")
    return sorted(found)


def _concordat_agreement_groups(entries: list[dict]) -> list[dict]:
    """Distinct intercantonal agreements with their estimated signatory sets.

    Takes RAW (pre-dedup) entries so every language version's title can be
    scanned for named cantons.  Sibling copies of the same agreement across
    cantons are grouped by normalized title (the same grouping
    ``propagate_concordat_dates`` uses).  Per agreement:

    - ``published``: cantons whose collections publish the text
    - ``named``: cantons explicitly named in any language version's title
    - ``signatories``: the union — the best available estimate of the full
      signatory set (LexFind publishes no official member-canton lists)
    """
    from .date_enricher import _normalize_title

    cantonal_raw = [
        e for e in entries if e["_scope"] == "cantonal"
        and effective_category_type(e)[0] == "Interkantonale Vereinbarung"
    ]
    # all-language titles per unique law, before dedup drops fr/it copies
    titles_by_identity: dict[str, list[str]] = {
        k: [str(f.get("title", "")) for f in files]
        for k, files in _group_by_identity(cantonal_raw).items()
    }
    concordats = _deduplicate(cantonal_raw)
    group_minima = _concordat_group_minima(concordats)
    code_to_key = {c: d["key"] for d in CONCORDAT_DOMAINS for c in d["codes"]}

    groups: dict[str, list[dict]] = defaultdict(list)
    for e in concordats:
        k = _normalize_title(e.get("title", ""))
        if not k:  # untitled: keep as its own singleton group
            k = f"_untitled/{e.get('canton')}/{e.get('systematic_number')}"
        groups[k].append(e)

    agreements = []
    for members in groups.values():
        de_members = [e for e in members if e.get("language") == "de"]
        rep = de_members[0] if de_members else members[0]
        gc, _ = effective_global_category(rep)
        domain = code_to_key.get(_extract_identifier(gc).split(".")[0], "autres")
        years = [y for y, _ in (earliest_known_year(e, group_minima)
                                for e in members) if y]
        per_canton: dict[str, dict] = {}
        named: set[str] = set()
        for e in sorted(members, key=lambda x: str(x.get("canton", ""))):
            canton = str(e.get("canton", "")).upper()
            per_canton.setdefault(canton, {
                "systematic_number": str(e.get("systematic_number", "")),
                "languages": e.get("_languages", [str(e.get("language", ""))]),
            })
            ident = f"{e.get('canton', '')}/{e.get('systematic_number', '')}"
            for t in titles_by_identity.get(ident, [str(e.get("title", ""))]):
                named.update(cantons_named_in_title(t))
        named &= set(ALL_CANTON_CODES)
        published = sorted(per_canton)
        agreements.append({
            "title": str(rep.get("title", "")),
            "domain": domain,
            "year": min(years) if years else "",
            "published": published,
            "named": sorted(named),
            "signatories": sorted(set(published) | named),
            "per_canton": per_canton,
        })
    return agreements


def generate_concordat_signatories(entries: list[dict]) -> dict:
    """Distinct intercantonal agreements with their signing cantons.

    Signatories = cantons whose collections publish the text, UNION the
    cantons explicitly named in any language version's title.  Only
    implemented for intercantonal agreements — the signing-cantons
    dimension exists only for texts adopted by several cantons.
    """
    agreements = [{
        "title": a["title"],
        "domain": a["domain"],
        "year": a["year"],
        "n_signatories": len(a["signatories"]),
        "signatories": a["signatories"],
        "published": a["published"],
        "named_in_title": a["named"],
        "per_canton": a["per_canton"],
    } for a in _concordat_agreement_groups(entries)]

    agreements.sort(key=lambda a: (-a["n_signatories"], a["year"] or "9999",
                                   a["title"]))
    return {
        "title": "Intercantonal agreements with signing cantons",
        "source": "LexFind (Institute of Federalism, University of Fribourg)",
        "total_agreements": len(agreements),
        "year_semantics": "enactment",
        "domains": _domains_export(),
        "agreements": agreements,
        "notes": [
            "Signatories = cantons whose collections publish the text, plus "
            "cantons explicitly named in the title of any language version "
            "— the best available estimate: LexFind does not publish "
            "official member-canton lists per text",
            "Grouping is by normalized title and therefore language-"
            "sensitive: a canton publishing only a French version of an "
            "agreement titled in German elsewhere appears as a separate "
            "entry",
        ],
    }


def generate_concordats_by_domain_signatories(entries: list[dict]) -> dict:
    """Canton × domain concordats table under the chstat/BADAC 2003
    methodology: one agreement counts once per SIGNATORY canton — an
    agreement signed by 10 cantons contributes 10 to its year's total.

    Signatory sets are estimated per agreement (published collections ∪
    cantons named in titles, see ``_concordat_agreement_groups``).  Same
    output shape as ``generate_concordats_by_domain`` so the dashboard
    table, CSV export and embeds render it unchanged.
    """
    agreements = _concordat_agreement_groups(entries)
    domain_keys = [d["key"] for d in CONCORDAT_DOMAINS]

    table: dict[str, dict[str, int]] = {
        canton: {k: 0 for k in domain_keys} for canton in ALL_CANTON_CODES
    }
    by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int)))
    named_only_adds = 0
    until_2003 = 0
    for a in agreements:
        for canton in a["signatories"]:
            table[canton][a["domain"]] += 1
            by_year[a["year"] or "unknown"][canton][a["domain"]] += 1
        named_only_adds += len(set(a["signatories"]) - set(a["published"]))
        if a["year"] and a["year"] <= "2003":
            until_2003 += len(a["signatories"])

    for row in table.values():
        row["total"] = sum(row.values())
    totals = {k: sum(row[k] for row in table.values()) for k in domain_keys}
    totals["total"] = sum(totals.values())

    return {
        "title": "Intercantonal agreements (concordats) by domain — "
                 "signatory-canton counting",
        "source": "LexFind (Institute of Federalism, University of Fribourg)",
        "methodology": "chstat/BADAC 2003: each agreement counts once per "
                       "signatory canton (an agreement signed by 10 cantons "
                       "counts 10). Signatory set per agreement = cantons "
                       "publishing the text in their collections ∪ cantons "
                       "named in any language version's title.",
        "total_concordats": totals["total"],
        "total_memberships": totals["total"],
        "total_agreements": len(agreements),
        "memberships_until_2003": until_2003,
        "chstat_2003_reference": 2522,
        "memberships_added_by_title_evidence": named_only_adds,
        "domains": _domains_export(),
        "cantons": table,
        "totals": totals,
        "year_semantics": "enactment",
        "by_year": {y: {c: dict(d) for c, d in cantons.items()}
                    for y, cantons in sorted(by_year.items())},
        "notes": [
            "THE computed concordats statistic: each agreement counts once "
            "per signing canton (signed by 10 cantons → 10 occurrences), "
            "purely from the source data — no scaling, no external baseline",
            "Signatories per agreement = cantons publishing the text in "
            "their collections ∪ cantons named in any language version's "
            "title; LexFind/LexWork publish no official member lists",
            "chstat.ch/BADAC's 2003 figure (2,522 memberships ≤2003) is an "
            "external reference only — our computed ≤2003 value is lower "
            "because agreements repealed decades ago were delisted from "
            "today's collections (historical attrition); see the "
            "verification report",
            "Distinct agreements with their signatory sets: "
            "/api/v1/stats/concordats_signatories.json",
        ],
    }


def generate_undated_laws(entries: list[dict]) -> dict:
    """Review list of laws with no plausible enactment-year evidence.

    A law is undated when ``enactment_year`` finds nothing usable: either
    no date fields at all (``no_date``) or only implausible values —
    LexFind's 1000-01-01 "unknown" sentinel and similar pre-1400 dates
    (``implausible_date``).  Published at api/v1/quality/undated_laws.json
    so the excluded laws can be inspected one by one.
    """
    link_base = "https://github.com/benjamin-arfa/swiss-law/blob/main/"
    laws = []
    by_entity: Counter = Counter()
    by_reason: Counter = Counter()
    for e in _deduplicate(entries):
        if enactment_year(e):
            continue
        entity = "CH" if e["_scope"] == "federal" else str(e.get("canton", "")).upper()
        raw_dates: dict = {}
        if e.get("enactment_date"):
            raw_dates["enactment_date"] = str(e["enactment_date"])
        if e.get("version_date"):
            raw_dates["version_date"] = str(e["version_date"])
        vds = e.get("version_dates")
        if isinstance(vds, list) and vds:
            raw_dates["version_dates"] = [str(v) for v in vds]
        reason = "implausible_date" if raw_dates else "no_date"
        by_entity[entity] += 1
        by_reason[reason] += 1
        laws.append({
            "entity": entity,
            "id": str(e.get("sr_number") or e.get("systematic_number") or ""),
            "title": str(e.get("title", "")),
            "category_type": effective_category_type(e)[0],
            "languages": e.get("_languages", [str(e.get("language", ""))]),
            "raw_dates": raw_dates,
            "enactment_date_source": str(e.get("enactment_date_source", "")),
            "reason": reason,
            "link": link_base + str(e.get("_path", "")),
        })
    laws.sort(key=lambda l: (l["entity"], l["id"]))
    return {
        "title": "Laws excluded from year-based statistics (no plausible date)",
        "note": "enactment_year() found no usable evidence: 'no_date' = no "
                "date fields at all; 'implausible_date' = only sentinel or "
                f"typo values before year {MIN_PLAUSIBLE_YEAR} (e.g. LexFind's "
                "1000-01-01 'unknown' placeholder). Raw upstream values are "
                "kept in raw_dates for review.",
        "total": len(laws),
        "by_entity": dict(by_entity.most_common()),
        "by_reason": dict(by_reason),
        "laws": laws,
    }


def _build_sr_category_map(ch_tree_path: Path) -> dict[str, str]:
    """Build SR number prefix → category label map from the CH tree JSON.

    Walks the tree and maps each node's identifier to its full label
    (e.g., "1.1" → "1.1 Bund und Kantone"). Returns empty dict if
    the tree file doesn't exist yet (first run before trees are fetched).
    """
    if not ch_tree_path.exists():
        return {}
    try:
        tree = json.loads(ch_tree_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}

    result: dict[str, str] = {}

    def _walk(nodes: list[dict]):
        for node in nodes:
            ident = node.get("identifier", "")
            title = node.get("title", "")
            if ident:
                result[ident] = f"{ident} {title}"
            for child in node.get("children", []):
                _walk([child])

    _walk(tree)
    return result


def _match_sr_to_tree(sr: str, cat_map: dict[str, str]) -> str:
    """Find the deepest matching category for an SR number.

    SR numbers like ``172.010.1`` need to match tree identifiers like ``172``.
    International law like ``0.142.113.672`` needs to match ``0.142``.
    Tries progressively shorter prefixes by removing segments and digits.
    """
    if not cat_map:
        return ""
    sr = sr.rstrip(".")
    # Try full SR first, then shorten by removing rightmost segment
    candidate = sr
    while candidate:
        if candidate in cat_map:
            return cat_map[candidate]
        # Remove trailing zeros from numeric segments (172.010 → 172.01 → 172.0)
        stripped = candidate.rstrip("0").rstrip(".")
        if stripped and stripped != candidate and stripped in cat_map:
            return cat_map[stripped]
        # Remove last segment
        if "." in candidate:
            candidate = candidate.rsplit(".", 1)[0]
        elif len(candidate) > 1:
            candidate = candidate[:-1]
        else:
            break
    return ""


def _sr_category_label(sr: str) -> str:
    cats = {
        "0": "Völkerrecht",
        "1": "Staat – Volk – Behörden",
        "2": "Privatrecht – Zivilrechtspflege – Vollstreckung",
        "3": "Strafrecht – Strafrechtspflege – Strafvollzug",
        "4": "Schule – Wissenschaft – Kultur",
        "5": "Landesverteidigung",
        "6": "Finanzen",
        "7": "Öffentliche Werke – Energie – Verkehr",
        "8": "Gesundheit – Arbeit – Soziale Sicherheit",
        "9": "Wirtschaft – Technische Zusammenarbeit",
    }
    prefix = sr.split(".")[0][:1] if sr else ""
    return cats.get(prefix, "")


def write_stats_json(stats: dict, output_path: str | Path = "docs/stats.json"):
    """Write stats to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stats, indent=2, ensure_ascii=False))
    logger.info("Wrote stats to %s", path)


def write_tags_json(tags: dict, output_path: str | Path = "docs/tags.json"):
    """Write per-law tag index to JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(tags, indent=2, ensure_ascii=False))
    logger.info("Wrote tags to %s (%d entries)", path, tags.get("total", 0))


def _iter_tree(nodes: list[dict]):
    """Yield every node of a nested tree (depth-first)."""
    for n in nodes:
        yield n
        yield from _iter_tree(n.get("children", []))


def _clean_tree(raw: dict) -> list[dict]:
    """Convert LexFind systematics response to a clean hierarchy list."""
    if not isinstance(raw, dict) or "" not in raw:
        return []
    root_children = raw.get("", {}).get("children", [])

    def _build(node_id: int) -> dict | None:
        node = raw.get(str(node_id))
        if not node:
            return None
        result = {
            "id": node_id,
            "identifier": node.get("identifier", ""),
            "title": node.get("title", ""),
        }
        children = node.get("children", [])
        if children:
            result["children"] = [
                c for c in (_build(cid) for cid in children) if c
            ]
        return result

    return [c for c in (_build(cid) for cid in root_children) if c]


def generate_publications(entries: list[dict], repo_name: str = "benjamin-arfa/swiss-law") -> dict[int, dict]:
    """Generate per-year publication JSON files from frontmatter entries.

    Each law appears once per year (deduplicated across languages).
    A ``languages`` field lists all available language versions.
    """
    # Group all file-level entries by (law_identity, year)
    groups: dict[tuple[str, int], list[dict]] = defaultdict(list)

    for e in entries:
        vd = str(e.get("version_date", ""))
        if len(vd) < 4:
            continue
        year = int(vd[:4])
        sr = str(e.get("sr_number") or e.get("systematic_number", ""))
        if not sr:
            continue
        scope = e.get("_scope", "federal")
        canton = e.get("canton", "")
        if scope == "cantonal" and canton:
            key = f"{canton}/{sr}"
        else:
            key = f"federal/{sr}"
        groups[(key, year)].append(e)

    by_year: dict[int, list[dict]] = defaultdict(list)

    for (_, year), group in groups.items():
        de_versions = [e for e in group if e.get("language") == "de"]
        rep = de_versions[0] if de_versions else group[0]
        sr = str(rep.get("sr_number") or rep.get("systematic_number", ""))
        scope = rep.get("_scope", "federal")
        canton = rep.get("canton", "")
        lang = rep.get("language", "de")
        languages = sorted({e.get("language", "unknown") for e in group})

        path = rep.get("_path", "")
        if not path:
            if scope == "cantonal" and canton:
                path = f"ch/{canton.lower()}/{lang}/{sr}.md"
            else:
                prefix = sr.split(".")[0]
                path = f"ch/{prefix}/{lang}/{sr}.md"

        rec = {
            "date": str(rep.get("version_date", "")),
            "sr_number": sr,
            "title": rep.get("title", ""),
            "scope": scope,
            "languages": languages,
            "canton": canton,
            "path": path,
            "url_main": f"https://raw.githubusercontent.com/{repo_name}/main/{quote(path)}",
        }
        if rep.get("systematic_category"):
            rec["systematic_category"] = rep["systematic_category"]
        if rep.get("global_category"):
            rec["global_category"] = rep["global_category"]
        if rep.get("category_type"):
            rec["category_type"] = rep["category_type"]
        by_year[year].append(rec)

    result = {}
    for year in sorted(by_year):
        pubs = sorted(by_year[year], key=lambda p: (p["date"], p["sr_number"]))
        result[year] = {
            "date_prefix": str(year),
            "count": len(pubs),
            "publications": pubs,
        }
    return result


def _extract_identifier(category_string: str) -> str:
    return category_string.split(" ", 1)[0] if category_string else ""


def _load_tree(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _annotate_tree(
    tree_nodes: list[dict],
    identifier_to_laws: dict[str, list[dict]],
) -> list[dict]:
    """Annotate tree nodes with law counts and type breakdowns, prune empty."""
    result = []
    for node in tree_nodes:
        ident = node.get("identifier", "")
        own_laws = identifier_to_laws.get(ident, [])

        children = _annotate_tree(
            node.get("children", []), identifier_to_laws,
        )

        own_count = len(own_laws)
        own_by_type: Counter[str] = Counter(
            e.get("category_type", "") for e in own_laws
        )

        child_total = sum(c["total"] for c in children)
        child_by_type: Counter[str] = Counter()
        for c in children:
            child_by_type.update(c["by_type"])

        total = own_count + child_total
        if total == 0:
            continue

        combined_by_type = dict((own_by_type + child_by_type).most_common())

        annotated: dict = {
            "identifier": ident,
            "title": node.get("title", ""),
            "total": total,
            "own": own_count,
            "by_type": combined_by_type,
        }
        if children:
            annotated["children"] = children
        result.append(annotated)

    return result


def generate_yearly_canton_stats(
    entries: list[dict],
    trees_dir: str | Path = "docs/trees",
) -> dict[str, dict[str, dict]]:
    """Generate per-year per-canton/CH stats with cross-tabs and tree structures.

    Entries are deduplicated before counting so each law is counted once
    regardless of language versions.

    Returns ``{year: {entity: stats_dict}}`` where entity is a canton code
    or ``"CH"`` for federal.
    """
    deduped = _deduplicate(entries)

    trees_path = Path(trees_dir)
    global_tree = _load_tree(trees_path / "global.json")
    global_titles = build_global_title_map(trees_path)
    tree_cache: dict[str, list[dict]] = {}

    def _get_canton_tree(entity: str) -> list[dict]:
        if entity not in tree_cache:
            tree_cache[entity] = _load_tree(trees_path / f"{entity.lower()}.json")
        return tree_cache[entity]

    data: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))

    for e in deduped:
        year = enactment_year(e)
        if not year:
            continue
        if e.get("_scope") == "cantonal" and e.get("canton"):
            entity = str(e["canton"]).upper()
        else:
            entity = "CH"
        data[year][entity].append(e)

    result: dict[str, dict[str, dict]] = {}
    for year in sorted(data):
        result[year] = {}
        for entity in sorted(data[year]):
            laws = data[year][entity]

            # --- by_type with cross-tabs (canonical type labels) ---
            type_groups: dict[str, list[dict]] = defaultdict(list)
            categorized = 0
            for e in laws:
                ct = effective_category_type(e)[0]
                if ct:
                    type_groups[ct].append(e)
                    categorized += 1

            by_type: dict[str, dict] = {}
            for type_name in sorted(type_groups, key=lambda t: -len(type_groups[t])):
                type_laws = type_groups[type_name]
                by_type[type_name] = {
                    "total": len(type_laws),
                    "by_topic": dict(Counter(
                        e["systematic_category"] for e in type_laws
                        if e.get("systematic_category")
                    ).most_common()),
                    "by_global_category": dict(Counter(
                        canonical_global_category(e["global_category"], global_titles)
                        for e in type_laws
                        if e.get("global_category")
                    ).most_common()),
                }

            # --- by_topic_tree ---
            topic_map: dict[str, list[dict]] = defaultdict(list)
            for e in laws:
                sc = e.get("systematic_category", "")
                if sc:
                    topic_map[_extract_identifier(sc)].append(e)

            canton_tree = _get_canton_tree(entity)
            by_topic_tree = _annotate_tree(canton_tree, topic_map)

            # --- by_global_category_tree ---
            global_map: dict[str, list[dict]] = defaultdict(list)
            for e in laws:
                gc = e.get("global_category", "")
                if gc:
                    global_map[_extract_identifier(gc)].append(e)

            by_global_tree = _annotate_tree(global_tree, global_map)

            # --- language versions available ---
            langs_available: Counter[str] = Counter()
            for e in laws:
                for lang in e.get("_languages", [e.get("language", "unknown")]):
                    langs_available[lang] += 1

            result[year][entity] = {
                "year": year,
                "year_semantics": "enactment",
                "entity": entity,
                "total": len(laws),
                "categorized": categorized,
                "uncategorized": len(laws) - categorized,
                "by_type": by_type,
                "by_topic_tree": by_topic_tree,
                "by_global_category_tree": by_global_tree,
                "languages_available": dict(langs_available.most_common()),
            }

    return result


def write_yearly_canton_stats(
    stats: dict[str, dict[str, dict]],
    output_dir: str | Path = "docs/api/v1/stats",
):
    """Write per-year per-canton stats as ``{year}/{entity}.json``.

    For year/entity combinations with no data, writes a stub JSON with
    ``total: 0`` and navigation hints (available years for that entity,
    available entities for that year) so consumers never get a 404.
    """
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    all_years = sorted(stats.keys())
    all_entities: set[str] = set()

    # First pass: build reverse indexes
    years_by_entity: dict[str, list[str]] = defaultdict(list)
    entities_by_year: dict[str, list[str]] = defaultdict(list)
    for year, entities in stats.items():
        for entity in entities:
            all_entities.add(entity)
            years_by_entity[entity].append(year)
            entities_by_year[year].append(entity)
    for entity in years_by_entity:
        years_by_entity[entity].sort()
    for year in entities_by_year:
        entities_by_year[year].sort()

    # Second pass: write files with navigation metadata
    for year, entities in stats.items():
        year_dir = out / year
        year_dir.mkdir(parents=True, exist_ok=True)
        for entity, payload in entities.items():
            payload["available_years_for_entity"] = years_by_entity[entity]
            payload["available_entities_for_year"] = entities_by_year[year]
            (year_dir / f"{entity}.json").write_text(
                json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
            )

    # Write stubs for missing combinations
    sorted_entities = sorted(all_entities)
    stubs = 0
    for year in all_years:
        year_dir = out / year
        year_dir.mkdir(parents=True, exist_ok=True)
        existing = set(stats.get(year, {}).keys())
        for entity in sorted_entities:
            if entity in existing:
                continue
            stub = {
                "year": year,
                "entity": entity,
                "total": 0,
                "message": f"No data for {entity} in {year}.",
                "available_years_for_entity": years_by_entity.get(entity, []),
                "available_entities_for_year": entities_by_year.get(year, []),
            }
            (year_dir / f"{entity}.json").write_text(
                json.dumps(stub, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            stubs += 1

    real_files = sum(len(e) for e in stats.values())
    index = {
        "years": all_years,
        "entities": sorted_entities,
        "total_files": real_files,
    }
    (out / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info(
        "Wrote %d year×entity stats files + %d stubs to %s",
        real_files, stubs, out,
    )


def write_publications(pubs_by_year: dict[int, dict], output_dir: str | Path = "docs/api/v1/publications"):
    """Write per-year publication JSON files + index."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    years = sorted(pubs_by_year.keys())
    total = sum(p["count"] for p in pubs_by_year.values())

    for year, payload in pubs_by_year.items():
        (out / f"{year}.json").write_text(
            json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    index = {
        "years": years,
        "total_publications": total,
        "earliest_year": years[0] if years else None,
        "latest_year": years[-1] if years else None,
    }
    (out / "index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    logger.info("Wrote %d year files (%d publications) to %s", len(years), total, out)


def fetch_and_write_trees(output_dir: str | Path = "docs/trees", rate_limit: float = 0.5):
    """Fetch category trees from LexFind API and write as static JSON files."""
    from .cantonal import (
        CantonalFetcher, ALL_CANTONS, CANTON_LANGUAGES, LEXFIND_API,
    )

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    fetcher = CantonalFetcher(rate_limit=rate_limit)

    # Global tree — all three languages (fr/it feed the Categories API)
    for lang in ("de", "fr", "it"):
        logger.info("Fetching global systematics tree (%s)...", lang)
        global_raw = fetcher._get_json(f"{LEXFIND_API}/{lang}/global/systematics")
        if global_raw:
            tree = _clean_tree(global_raw)
            suffix = "" if lang == "de" else f"_{lang}"
            (out / f"global{suffix}.json").write_text(
                json.dumps(tree, indent=2, ensure_ascii=False))
            n_nodes = sum(1 for _ in _iter_tree(tree))
            logger.info("Wrote global tree %s (%d nodes, %d top-level)",
                        lang, n_nodes, len(tree))

    # CH (federal) tree — entity 27
    logger.info("Fetching CH (federal) systematics tree...")
    ch_entity_id = fetcher._lexfind_entity_id("ch", "de")
    if ch_entity_id:
        ch_raw = fetcher._get_json(f"{LEXFIND_API}/de/entities/{ch_entity_id}/systematics")
        if ch_raw:
            tree = _clean_tree(ch_raw)
            (out / "ch.json").write_text(json.dumps(tree, indent=2, ensure_ascii=False))
            logger.info("Wrote CH (federal) tree (%d top-level nodes)", len(tree))

    # Federal SR → global-category mapping (harmonized taxonomy)
    from .categories import fetch_federal_global_categories
    logger.info("Fetching federal global-category mapping...")
    try:
        fetch_federal_global_categories(fetcher, Path(output_dir).parent.parent)
    except Exception:
        logger.exception("Federal global-category fetch failed (continuing)")

    # Per-canton trees
    for canton in ALL_CANTONS:
        lang = CANTON_LANGUAGES.get(canton, ["de"])[0]
        entity_id = fetcher._lexfind_entity_id(canton, lang)
        if entity_id is None:
            logger.warning("No entity ID for %s, skipping tree", canton.upper())
            continue
        raw = fetcher._get_json(f"{LEXFIND_API}/{lang}/entities/{entity_id}/systematics")
        if raw:
            tree = _clean_tree(raw)
            (out / f"{canton}.json").write_text(
                json.dumps(tree, indent=2, ensure_ascii=False)
            )
            logger.info("Wrote %s tree (%d top-level nodes)", canton.upper(), len(tree))

    logger.info("All trees written to %s", out)
