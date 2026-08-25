"""Canonical category dictionaries + harmonization helpers.

Law files store category fields in the language of the file, so raw
aggregation splits one category into up to three keys (Gesetz / Loi /
Legge) and, for canton-specific systematics, merges unrelated categories
that share a label.  This module provides:

- the instrument-type dictionary (LexFind category ids are stable across
  languages) with one label per language,
- canonicalization helpers used by the stats aggregations,
- generators for the public Categories API
  (``api/v1/categories/{index,types,global,<canton>}.json``).
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# LexFind /api/fe/{lang}/categories — ids are language-stable (verified live).
# "en" labels are our own translations (LexFind serves de/fr/it only).
CATEGORY_TYPES = [
    {"id": 1, "label": {"de": "Staatsvertrag", "fr": "Traité international", "it": "Trattato internazionale", "en": "International treaty"}},
    {"id": 2, "label": {"de": "Interkantonale Vereinbarung", "fr": "Accord intercantonal", "it": "Accordo intercantonale", "en": "Intercantonal agreement"}},
    {"id": 3, "label": {"de": "Verfassung", "fr": "Constitution", "it": "Costituzione", "en": "Constitution"}},
    {"id": 4, "label": {"de": "Gesetz", "fr": "Loi", "it": "Legge", "en": "Act"}},
    {"id": 5, "label": {"de": "Anderes", "fr": "Autre", "it": "Altro", "en": "Other"}},
    {"id": 6, "label": {"de": "Verordnung", "fr": "Ordonnance", "it": "Ordinanza", "en": "Ordinance"}},
    {"id": 7, "label": {"de": "Reglement", "fr": "Règlement", "it": "Regolamento", "en": "Regulation"}},
    {"id": 8, "label": {"de": "Verordnung des Parlaments (Dekret)", "fr": "Ordonnance parlementaire (décret)", "it": "Ordinanza parlamentaria (decreto legislativo)", "en": "Parliamentary ordinance (decree)"}},
    {"id": 9, "label": {"de": "Gemeindeerlass", "fr": "Acte législatif communal", "it": "Atto legislativo comunale", "en": "Municipal act"}},
]

# English names for the harmonized taxonomy's top-level domains
# (LexFind has no English tree; deeper nodes stay de/fr/it).
DOMAIN_EN = {
    "1": "State, people, authorities",
    "2": "Civil law",
    "3": "Criminal law",
    "4": "Education, science, culture",
    "5": "Defence, civil protection, police",
    "6": "Finance, taxes",
    "7": "Planning, construction, environment, transport",
    "8": "Health, labour, social security",
    "9": "Economy",
    "10": "Publications without text",
    "uncategorized": "Unclassifiable",
}

# any-language name → canonical (German) label
_CANONICAL_TYPE: dict[str, str] = {
    name: entry["label"]["de"]
    for entry in CATEGORY_TYPES
    for name in entry["label"].values()
}

# canonical label → {de, fr, it}
CATEGORY_TYPE_LABELS: dict[str, dict[str, str]] = {
    entry["label"]["de"]: entry["label"] for entry in CATEGORY_TYPES
}


def canonical_category_type(name: str) -> str:
    """Map a localized instrument-type name to its canonical (German) label."""
    return _CANONICAL_TYPE.get(name, name)


def _extract_code(value: str) -> str:
    return value.split(" ", 1)[0] if value else ""


def build_global_title_map(trees_dir: str | Path, lang: str = "de") -> dict[str, str]:
    """identifier → title from the global systematics tree (one language)."""
    suffix = "" if lang == "de" else f"_{lang}"
    path = Path(trees_dir) / f"global{suffix}.json"
    return _walk_titles(_load_tree(path))


def build_canton_title_map(trees_dir: str | Path, canton: str) -> dict[str, str]:
    """identifier → title from a canton's systematics tree."""
    return _walk_titles(_load_tree(Path(trees_dir) / f"{canton.lower()}.json"))


# The languages the global systematics is published in here.  LexFind serves
# de/fr/it (and rm); "en" is authored in this repo as docs/trees/global_en.json
# — see TITLE_EN_SOURCE.
GLOBAL_TREE_LANGS = ("de", "fr", "it", "en")

TITLE_EN_SOURCE = ("machine translation, reviewed — LexFind publishes no "
                   "English tree")


def build_global_path_map(trees_dir: str | Path) -> dict[str, dict]:
    """code → {code, depth, parent, title: {de,fr,it,en}, path: {de,fr,it,en}}.

    ``path[lang]`` is the dot-joined chain of titles from the top-level
    domain down to the node itself (``Etat.Dispositions générales.contrôle
    des habitants``) — the human-readable form of a dotted code.  Ancestor
    codes are derived by splitting the dotted code, so no tree walk is
    needed; a language missing a node falls back to the German title, and a
    code missing from the tree entirely falls back to the code itself.

    Titles are ``.strip()``ed here rather than in the trees: the fetched
    fr/it files carry a trailing newline from the source API and are kept
    byte-faithful to it.
    """
    maps = {lang: {k: v.strip() for k, v in
                   build_global_title_map(trees_dir, lang).items()}
            for lang in GLOBAL_TREE_LANGS}
    # Only LexFind's own dotted codes.  ``uncategorized`` is our sentinel for
    # "no legal domain in the source", present in some snapshots of the tree
    # and absent from others; leaving it out keeps this map identical either
    # way, and the consumers that need a label for it carry their own.
    codes = [c for c in maps["de"] if c[:1].isdigit()]
    out: dict[str, dict] = {}
    for code in sorted(codes, key=lambda c: [int(p) if p.isdigit() else p
                                             for p in c.split(".")]):
        parts = code.split(".")
        ancestors = [".".join(parts[:i + 1]) for i in range(len(parts))]
        title, path = {}, {}
        for lang in GLOBAL_TREE_LANGS:
            m = maps[lang]
            title[lang] = m.get(code) or maps["de"].get(code, "")
            path[lang] = ".".join(m.get(a) or maps["de"].get(a) or a
                                  for a in ancestors)
        out[code] = {
            "code": code,
            "depth": len(parts),
            "parent": ".".join(parts[:-1]) if len(parts) > 1 else None,
            "title": title,
            "path": path,
        }
    return out


def _load_tree(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _walk_titles(nodes: list[dict]) -> dict[str, str]:
    result: dict[str, str] = {}

    def _walk(ns: list[dict]):
        for n in ns:
            ident = str(n.get("identifier", ""))
            if ident and ident not in result:
                result[ident] = str(n.get("title", ""))
            _walk(n.get("children", []))

    _walk(nodes)
    return result


def canonical_global_category(value: str, title_map: dict[str, str]) -> str:
    """Harmonize a global_category value by its dotted code.

    ``7.70.50 Protection de la nature`` → ``7.70.50 Naturschutz`` (title
    from the German global tree). Unknown codes keep their raw value.
    """
    code = _extract_code(value)
    title = title_map.get(code)
    return f"{code} {title}" if title else value


def canonical_systematic_category(canton: str, value: str,
                                  title_map: dict[str, str]) -> str:
    """Harmonize a canton systematic_category: key by (canton, code).

    Prefixing with the canton splits cross-canton label collisions
    ("Universität" = code VIII in one canton, 217 in another); the tree
    title merges language variants within bilingual cantons.
    """
    code = _extract_code(value)
    title = title_map.get(code)
    body = f"{code} {title}" if title else value
    return f"{canton.upper()} {body}"


FEDERAL_GLOBAL_CATEGORIES_FILE = "docs/federal_global_categories.json"


def fetch_federal_global_categories(fetcher, repo_path: str | Path = ".") -> dict[str, str]:
    """Fetch the SR → global-category mapping for federal law from LexFind.

    LexFind classifies the Confederation (entity CH) in the same global
    "domaine juridique" tree as the cantons, which makes it the single
    harmonized taxonomy across federal and cantonal law.  Queries the
    global tree directly with the CH entity filter (the CH entity's own
    tree walk misses laws attached to non-leaf nodes, e.g. SR 101).
    Writes ``docs/federal_global_categories.json`` ({sr_number: "code title"}).
    """
    from .cantonal import LEXFIND_API, _GLOBAL_SYSTEMATICS_BATCH

    entity_id = fetcher._lexfind_entity_id("ch", "de")
    if entity_id is None:
        raise RuntimeError("LexFind CH entity not found")

    # All node ids, not just leaves — laws can be attached to internal
    # nodes too (e.g. SR 220 Obligationenrecht).
    gtree = fetcher._get_json(f"{LEXFIND_API}/de/global/systematics")
    if not isinstance(gtree, dict):
        raise RuntimeError("LexFind global systematics unavailable")
    node_ids = sorted(int(k) for k in gtree if k)

    mapping: dict[str, str] = {}
    for i in range(0, len(node_ids), _GLOBAL_SYSTEMATICS_BATCH):
        batch = node_ids[i:i + _GLOBAL_SYSTEMATICS_BATCH]
        params = "&".join(f"tols_for_systematics[]={lid}" for lid in batch)
        url = (f"{LEXFIND_API}/de/global/systematics"
               f"?active_only=false&entity_filter[]={entity_id}&{params}")
        data = fetcher._get_json(url)
        if not isinstance(data, dict):
            continue
        for k, v in data.items():
            if not k:
                continue
            label = f"{v.get('identifier', '')} {v.get('title', '')}".strip()
            for tol in v.get("tols", []):
                sr = str(tol.get("systematic_number", "")).strip()
                if sr and sr not in mapping:
                    mapping[sr] = label

    out = Path(repo_path) / FEDERAL_GLOBAL_CATEGORIES_FILE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(mapping, indent=1, ensure_ascii=False, sort_keys=True),
                   encoding="utf-8")
    logger.info("Wrote federal global-category mapping: %d SRs classified", len(mapping))
    return mapping


def load_federal_global_categories(repo_path: str | Path = ".") -> dict[str, str]:
    path = Path(repo_path) / FEDERAL_GLOBAL_CATEGORIES_FILE
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def federal_fallback_code(sr: str) -> str:
    """Map an SR number to a global-tree TOP-LEVEL code when LexFind has no
    assignment.  The SR top levels 1-9 mirror the global tree by design;
    international law (SR 0.X…) follows the domestic scheme after the dot.
    """
    sr = str(sr).strip()
    if sr.startswith("0.") and len(sr) > 2 and sr[2].isdigit():
        return sr[2]
    return sr[0] if sr[:1].isdigit() and sr[0] != "0" else ""


# ─── Categories API generators ────────────────────────────────────────────────

def generate_categories_api(trees_dir: str | Path, output_dir: str | Path):
    """Write the public category dictionaries to ``api/v1/categories/``.

    - ``types.json``: instrument types with one label per language
    - ``global.json``: domaine-juridique tree, titles in de/fr/it where
      the fr/it trees have been fetched (falls back to de-only)
    - ``{canton}.json``: per-canton systematic tree (primary language)
    - ``index.json``: available dictionaries
    """
    trees = Path(trees_dir)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    (out / "types.json").write_text(json.dumps({
        "note": "Instrument types (LexFind category ids, language-stable). "
                "stats.json by_category_type keys use the German label.",
        "types": CATEGORY_TYPES,
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    # Multilingual global tree: merge de/fr/it trees by node id
    de_tree = _load_tree(trees / "global.json")
    lang_maps = {}
    for lang in ("fr", "it", "en"):
        by_id: dict[int, str] = {}

        def _collect(ns):
            for n in ns:
                if n.get("id") is not None:
                    by_id[n["id"]] = str(n.get("title", ""))
                _collect(n.get("children", []))

        _collect(_load_tree(trees / f"global_{lang}.json"))
        lang_maps[lang] = by_id

    def _multilingual(ns: list[dict]) -> list[dict]:
        result = []
        for n in ns:
            title = {"de": str(n.get("title", ""))}
            for lang, m in lang_maps.items():
                t = m.get(n.get("id"))
                if t:
                    title[lang] = t
            node = {"identifier": str(n.get("identifier", "")), "title": title}
            children = _multilingual(n.get("children", []))
            if children:
                node["children"] = children
            result.append(node)
        return result

    (out / "global.json").write_text(json.dumps({
        "note": "Global systematics ('domaine juridique'). stats.json "
                "by_global_category keys are '<identifier> <german title>'.",
        "title_en_source": TITLE_EN_SOURCE,
        "tree": _multilingual(de_tree),
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    # code → depth/parent/titles/label paths, for consumers that need the
    # dotted codes of the granular exports resolved to readable labels.
    paths = build_global_path_map(trees)
    (out / "global_paths.json").write_text(json.dumps({
        "note": "Flat index of the global systematics: one entry per dotted "
                "code, with its ancestors' titles joined into a label path. "
                "Resolves the 'topic' codes in "
                "api/v1/stats/granular/*.json.",
        "title_en_source": TITLE_EN_SOURCE,
        "total": len(paths),
        "codes": paths,
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    cantons_written = []
    for tree_file in sorted(trees.glob("*.json")):
        stem = tree_file.stem
        if (stem in ("global", "global_fr", "global_it", "global_en", "ch")
                or len(stem) != 2):
            continue
        tree = _load_tree(tree_file)
        if not tree:
            continue
        (out / f"{stem.upper()}.json").write_text(json.dumps({
            "canton": stem.upper(),
            "note": "Canton systematics tree (primary language). stats.json "
                    "by_systematic_category keys are "
                    "'<CANTON> <identifier> <title>'.",
            "tree": tree,
        }, indent=1, ensure_ascii=False), encoding="utf-8")
        cantons_written.append(stem.upper())

    (out / "index.json").write_text(json.dumps({
        "types": "api/v1/categories/types.json",
        "global": "api/v1/categories/global.json",
        "global_paths": "api/v1/categories/global_paths.json",
        "cantons": {c: f"api/v1/categories/{c}.json" for c in cantons_written},
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    logger.info("Wrote categories API (%d canton trees) to %s",
                len(cantons_written), out)
