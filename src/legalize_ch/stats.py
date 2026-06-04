"""Statistics generator — aggregate frontmatter fields across all law files."""
from __future__ import annotations

import json
import logging
from collections import Counter, defaultdict
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


def _parse_frontmatter(path: Path) -> dict | None:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[4:end]) or None
    except yaml.YAMLError:
        return None


def collect_all_frontmatter(repo_path: str | Path = ".") -> list[dict]:
    """Scan all .md files under ch/ and return their frontmatter dicts."""
    ch_dir = Path(repo_path) / "ch"
    if not ch_dir.exists():
        return []

    results = []
    for md in sorted(ch_dir.rglob("*.md")):
        if md.name in ("INDEX.md", "README.md"):
            continue
        fm = _parse_frontmatter(md)
        if fm and (fm.get("sr_number") or fm.get("systematic_number")):
            scope = "cantonal" if fm.get("canton") else "federal"
            fm["_scope"] = scope
            fm["_path"] = str(md.relative_to(repo_path))
            results.append(fm)

    logger.info("Scanned %d law files", len(results))
    return results


def generate_stats(repo_path: str | Path = ".") -> dict:
    """Generate comprehensive statistics from all law frontmatter."""
    entries = collect_all_frontmatter(repo_path)
    if not entries:
        return {}

    total = len(entries)
    federal = [e for e in entries if e["_scope"] == "federal"]
    cantonal = [e for e in entries if e["_scope"] == "cantonal"]

    # ─── Per-field counters ─────────────────────────────────────────────
    by_language = Counter(e.get("language", "unknown") for e in entries)
    by_source = Counter(e.get("source", "unknown") for e in entries)
    by_canton = Counter(e["canton"] for e in cantonal if e.get("canton"))

    # Category breakdowns (cantonal only — federal uses SR prefix categories)
    by_category_type = Counter(
        e.get("category_type", "")
        for e in cantonal if e.get("category_type")
    )
    by_systematic_category = Counter(
        e.get("systematic_category", "")
        for e in cantonal if e.get("systematic_category")
    )
    by_global_category = Counter(
        e.get("global_category", "")
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
                result[vd[:4]][val] += 1
        return {y: dict(counts) for y, counts in sorted(result.items())}

    category_type_by_year = _yearly_breakdown("category_type", "cantonal")
    language_by_year = _yearly_breakdown("language")
    canton_by_year = _yearly_breakdown("canton", "cantonal")

    # Canton × category_type cross-tab
    category_type_by_canton: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for e in cantonal:
        c = e.get("canton", "")
        ct = e.get("category_type", "")
        if c and ct:
            category_type_by_canton[c][ct] += 1

    # Year × canton × category_type 3-way cross-tab
    cat_by_canton_by_year: dict[str, dict[str, dict[str, int]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(int))
    )
    for e in cantonal:
        vd = str(e.get("version_date", ""))
        c = e.get("canton", "")
        ct = e.get("category_type", "")
        if len(vd) >= 4 and c and ct:
            cat_by_canton_by_year[vd[:4]][c][ct] += 1

    return {
        "total_laws": total,
        "federal_laws": len(federal),
        "cantonal_laws": len(cantonal),
        "by_language": dict(by_language.most_common()),
        "by_source": dict(by_source.most_common()),
        "by_canton": dict(by_canton.most_common()),
        "by_sr_category": dict(by_sr_category.most_common()),
        "by_category_type": dict(by_category_type.most_common()),
        "by_systematic_category_top20": dict(by_systematic_category.most_common(20)),
        "by_global_category_top20": dict(by_global_category.most_common(20)),
        "by_year": dict(sorted(by_year.items())),
        "by_month": dict(sorted(by_month.items())),
        "by_year_scope": {y: dict(c) for y, c in sorted(by_year_scope.items())},
        "category_type_by_year": category_type_by_year,
        "language_by_year": language_by_year,
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


def generate_publications(entries: list[dict], repo_name: str = "swiss-law-as-source/swiss-law-as-source.github.io") -> dict[int, dict]:
    """Generate per-year publication JSON files from frontmatter entries.

    Groups laws by version_date year, producing the same shape as the old
    static_export: ``{date_prefix, count, publications: [...]}``.
    """
    by_year: dict[int, list[dict]] = defaultdict(list)

    for e in entries:
        vd = str(e.get("version_date", ""))
        if len(vd) < 4:
            continue
        year = int(vd[:4])
        sr = str(e.get("sr_number") or e.get("systematic_number", ""))
        if not sr:
            continue
        scope = e.get("_scope", "federal")
        lang = e.get("language", "de")
        canton = e.get("canton", "")

        if scope == "cantonal" and canton:
            path = f"ch/{canton.lower()}/{lang}/{sr}.md"
        else:
            prefix = sr.split(".")[0]
            path = f"ch/{prefix}/{lang}/{sr}.md"

        rec = {
            "date": vd,
            "sr_number": sr,
            "title": e.get("title", ""),
            "scope": scope,
            "language": lang,
            "canton": canton,
            "path": path,
            "url_main": f"https://raw.githubusercontent.com/{repo_name}/main/{path}",
        }
        if e.get("systematic_category"):
            rec["systematic_category"] = e["systematic_category"]
        if e.get("global_category"):
            rec["global_category"] = e["global_category"]
        if e.get("category_type"):
            rec["category_type"] = e["category_type"]
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

    # Global tree
    logger.info("Fetching global systematics tree...")
    global_raw = fetcher._get_json(f"{LEXFIND_API}/de/global/systematics")
    if global_raw:
        tree = _clean_tree(global_raw)
        (out / "global.json").write_text(json.dumps(tree, indent=2, ensure_ascii=False))
        logger.info("Wrote global tree (%d top-level nodes)", len(tree))

    # CH (federal) tree — entity 27
    logger.info("Fetching CH (federal) systematics tree...")
    ch_entity_id = fetcher._lexfind_entity_id("ch", "de")
    if ch_entity_id:
        ch_raw = fetcher._get_json(f"{LEXFIND_API}/de/entities/{ch_entity_id}/systematics")
        if ch_raw:
            tree = _clean_tree(ch_raw)
            (out / "ch.json").write_text(json.dumps(tree, indent=2, ensure_ascii=False))
            logger.info("Wrote CH (federal) tree (%d top-level nodes)", len(tree))

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
