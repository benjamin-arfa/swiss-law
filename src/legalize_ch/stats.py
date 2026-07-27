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
    {"key": "etat", "label_fr": "Organisation de l'état, sécurité", "codes": ["1", "5"]},
    {"key": "sante", "label_fr": "Santé, sécurité sociale", "codes": ["8"]},
    {"key": "educ", "label_fr": "Éducation, science, culture", "codes": ["4"]},
    {"key": "infra", "label_fr": "Infrastructure, trafic, environnement", "codes": ["7"]},
    {"key": "eco", "label_fr": "Économie, agriculture", "codes": ["9"]},
    {"key": "fin", "label_fr": "Finances publiques, impôts", "codes": ["6"]},
    {"key": "autres", "label_fr": "Autres / non classés", "codes": ["2", "3", "10"]},
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

    by_category_type = Counter(
        canonical_category_type(e["category_type"])
        for e in cantonal if e.get("category_type")
    )
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
        vd = str(e.get("version_date", ""))
        if len(vd) >= 4:
            year = vd[:4]
            by_year[year] += 1
            by_year_scope[year][e["_scope"]] += 1
        if len(vd) >= 7:
            by_month[vd[:7]] += 1

    # ─── Time x field cross-tabs ────────────────────────────────────────
    def _yearly_breakdown(field: str, scope_filter: str | None = None) -> dict[str, dict[str, int]]:
        result: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
        for e in entries:
            if scope_filter and e["_scope"] != scope_filter:
                continue
            val = e.get(field, "")
            vd = str(e.get("version_date", ""))
            if val and len(vd) >= 4:
                if field == "category_type":
                    val = canonical_category_type(val)
                result[vd[:4]][val] += 1
        return {y: dict(counts) for y, counts in sorted(result.items())}

    category_type_by_year = _yearly_breakdown("category_type", "cantonal")
    canton_by_year = _yearly_breakdown("canton", "cantonal")

    # Canton × category_type cross-tab
    category_type_by_canton: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for e in cantonal:
        c = e.get("canton", "")
        ct = canonical_category_type(e.get("category_type", ""))
        if c and ct:
            category_type_by_canton[c][ct] += 1

    # Year × canton × category_type 3-way cross-tab
    cat_by_canton_by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int))
    )
    for e in cantonal:
        vd = str(e.get("version_date", ""))
        c = e.get("canton", "")
        ct = canonical_category_type(e.get("category_type", ""))
        if len(vd) >= 4 and c and ct:
            cat_by_canton_by_year[vd[:4]][c][ct] += 1

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
        "by_category_type": dict(by_category_type.most_common()),
        "by_systematic_category": dict(by_systematic_category.most_common()),
        "by_global_category": dict(by_global_category.most_common()),
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

    return {
        "federal": federal,
        "cantonal": {k: v for k, v in sorted(by_canton.items())},
        "total": len(federal) + sum(len(v) for v in by_canton.values()),
    }


def generate_harmonized_categories(entries: list[dict],
                                   repo_path: str | Path = ".") -> dict:
    """Aggregate ALL laws (federal + cantonal) on the harmonized taxonomy.

    The taxonomy is LexFind's global systematics ("domaine juridique") —
    the same tree for the Confederation and all 26 cantons.  Cantonal laws
    carry ``global_category`` directly; federal laws resolve via the
    fetched SR mapping (docs/federal_global_categories.json), falling back
    to the SR top-level prefix (which mirrors the global tree by design).
    """
    from .categories import federal_fallback_code, load_federal_global_categories

    repo = Path(repo_path)
    deduped = _deduplicate(entries)
    fed_map = load_federal_global_categories(repo)

    code_counts: dict[str, dict[str, int]] = defaultdict(lambda: {"federal": 0, "cantonal": 0})
    stats_counts = {"federal_lexfind": 0, "federal_fallback": 0,
                    "federal_unmapped": 0, "cantonal_classified": 0,
                    "cantonal_unclassified": 0}

    for e in deduped:
        if e["_scope"] == "cantonal":
            code = _extract_identifier(str(e.get("global_category", "")))
            if code:
                code_counts[code]["cantonal"] += 1
                stats_counts["cantonal_classified"] += 1
            else:
                stats_counts["cantonal_unclassified"] += 1
        else:
            sr = str(e.get("sr_number", ""))
            label = fed_map.get(sr, "")
            code = _extract_identifier(label)
            if code:
                stats_counts["federal_lexfind"] += 1
            else:
                code = federal_fallback_code(sr)
                if code:
                    stats_counts["federal_fallback"] += 1
                else:
                    stats_counts["federal_unmapped"] += 1
                    continue
            code_counts[code]["federal"] += 1

    # Annotate the multilingual global tree with rolled-up counts
    trees_dir = repo / "docs" / "trees"
    from .categories import build_global_title_map
    titles = {lang: build_global_title_map(trees_dir, lang) for lang in ("de", "fr", "it")}
    global_tree = _load_tree(trees_dir / "global.json")
    seen_codes: set[str] = set()

    def _annotate(nodes: list[dict]) -> list[dict]:
        result = []
        for n in nodes:
            ident = str(n.get("identifier", ""))
            own = code_counts.get(ident, {"federal": 0, "cantonal": 0})
            if ident:
                seen_codes.add(ident)
            children = _annotate(n.get("children", []))
            federal = own["federal"] + sum(c["federal"] for c in children)
            cant = own["cantonal"] + sum(c["cantonal"] for c in children)
            if federal + cant == 0:
                continue
            node = {
                "identifier": ident,
                "title": {lang: m.get(ident, "") for lang, m in titles.items()
                          if m.get(ident)},
                "total": federal + cant,
                "federal": federal,
                "cantonal": cant,
                "own": own["federal"] + own["cantonal"],
            }
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
        if canonical_category_type(e.get("category_type", "")) == "Interkantonale Vereinbarung"
    ]

    code_to_key = {c: d["key"] for d in CONCORDAT_DOMAINS for c in d["codes"]}
    domain_keys = [d["key"] for d in CONCORDAT_DOMAINS]

    table: dict[str, dict[str, int]] = {
        canton: {k: 0 for k in domain_keys} for canton in ALL_CANTON_CODES
    }
    unclassified = 0
    for e in concordats:
        canton = str(e.get("canton", "")).upper()
        if canton not in table:
            logger.warning("Concordat with unknown canton %r: %s", canton, e.get("_path"))
            continue
        top_code = _extract_identifier(str(e.get("global_category", ""))).split(".")[0]
        key = code_to_key.get(top_code)
        if key is None:
            key = "autres"
            unclassified += 1
        table[canton][key] += 1

    for row in table.values():
        row["total"] = sum(row.values())
    totals = {k: sum(row[k] for row in table.values()) for k in domain_keys}
    totals["total"] = sum(totals.values())

    return {
        "title": "Concordats intercantonaux par domaine",
        "source": "LexFind (Institut pour le fédéralisme, Université de Fribourg)",
        "total_concordats": totals["total"],
        "domains": [
            {"key": d["key"], "label_fr": d["label_fr"], "global_category_codes": d["codes"]}
            for d in CONCORDAT_DOMAINS
        ],
        "cantons": table,
        "totals": totals,
        "unclassified_in_autres": unclassified,
        "notes": [
            "« Autres » inclut droit civil, droit pénal et les concordats sans "
            "domaine juridique dans la base publique LexFind (~28 % non classés à la source)",
            "Couverture selon les collections importées — lancer backfill-lexfind "
            "pour compléter les cantons sous-représentés",
        ],
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
        vd = str(e.get("version_date", ""))
        if len(vd) < 4:
            continue
        year = vd[:4]
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
                ct = canonical_category_type(e.get("category_type", ""))
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
