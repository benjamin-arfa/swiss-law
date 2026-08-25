"""Per-entity law index — one JSON per entity (CH + 26 cantons).

For every unique law: link, per-language character volume and heuristic
article count.  Sharded per entity so browsers never load one giant file:

- ``api/v1/laws/index.json`` — small master index (entity list + totals)
- ``api/v1/laws/{ENTITY}.json`` — the entity's laws with per-language metrics
- ``api/v1/laws/ALL.json`` — every entity in one compact cross-entity file
"""
from __future__ import annotations

import json
import logging
from pathlib import Path
from urllib.parse import quote

from .index_generator import CANTON_NAMES, _sr_sort_key
from .stats import _group_by_identity

logger = logging.getLogger(__name__)

LAW_REPO = "benjamin-arfa/swiss-law"

ARTICLE_COUNT_NOTE = (
    "Heuristic: number of distinct 'Art. N' / 'Article N' / 'Articolo N' / "
    "line-leading '§ N' markers per file. Cross-references to other laws "
    "inflate slightly; files without such markers (e.g. metadata-only pages, "
    "Roman-numeral treaties) count 0."
)

_LANG_PREFERENCE = ("de", "fr", "it", "rm")

# Federal legacy tree ch/{de,fr,it}/... coexists with the canonical
# ch/{prefix}/{lang}/... tree; prefer canonical files on duplicates.
_LEGACY_PREFIXES = ("ch/de/", "ch/fr/", "ch/it/", "ch/en/")


def _is_legacy_path(path: str) -> bool:
    return path.startswith(_LEGACY_PREFIXES)


def _pick_representative(versions: list[dict]) -> dict:
    for lang in _LANG_PREFERENCE:
        for v in versions:
            if v.get("language") == lang:
                return v
    return versions[0]


def generate_law_index(entries: list[dict], repo_name: str = LAW_REPO) -> dict[str, dict]:
    """Build per-entity law index from file-level frontmatter entries.

    Returns ``{entity_code: entity_payload}`` with ``CH`` for federal laws.
    """
    link_base = f"https://github.com/{repo_name}/blob/main/"
    raw_base = f"https://raw.githubusercontent.com/{repo_name}/main/"

    by_entity: dict[str, list[dict]] = {}

    for group in _group_by_identity(entries).values():
        rep = _pick_representative(group)
        if rep["_scope"] == "federal":
            entity = "CH"
            law_id = str(rep.get("sr_number", ""))
        else:
            entity = str(rep.get("canton", "")).upper()
            law_id = str(rep.get("systematic_number", ""))
        if not law_id or not entity:
            continue

        # One file per language; prefer the canonical tree over the
        # federal legacy ch/{lang}/ tree when both exist.
        per_lang: dict[str, dict] = {}
        for v in sorted(group, key=lambda v: v.get("_path", "")):
            lang = v.get("language", "unknown")
            existing = per_lang.get(lang)
            if existing and not (_is_legacy_path(existing["path"])
                                 and not _is_legacy_path(v["_path"])):
                continue
            per_lang[lang] = {
                "chars": v.get("_body_chars", 0),
                "articles": v.get("_body_articles", 0),
                "path": v["_path"],
            }

        preferred_lang = next(
            (l for l in _LANG_PREFERENCE if l in per_lang), next(iter(per_lang)))
        languages = {l: per_lang[l] for l in _LANG_PREFERENCE if l in per_lang}
        languages.update({l: d for l, d in per_lang.items() if l not in languages})

        item: dict = {
            "id": law_id,
            "title": rep.get("title", ""),
            "link": link_base + quote(per_lang[preferred_lang]["path"]),
            "languages": languages,
        }
        if rep.get("version_date"):
            item["version_date"] = str(rep["version_date"])
        if rep.get("enactment_date"):
            item["enactment_date"] = str(rep["enactment_date"])
            item["enactment_date_source"] = str(rep.get("enactment_date_source", ""))
        if isinstance(rep.get("version_dates"), list) and rep["version_dates"]:
            item["version_dates"] = [str(d) for d in rep["version_dates"]]
        if rep.get("abbreviation"):
            item["abbreviation"] = str(rep["abbreviation"])
        for field in ("category_type", "systematic_category", "global_category",
                      "global_category_inferred", "inference_source"):
            if rep.get(field):
                item[field] = rep[field]

        by_entity.setdefault(entity, []).append(item)

    result: dict[str, dict] = {}
    for entity in sorted(by_entity, key=lambda e: (e != "CH", e)):
        items = by_entity[entity]
        if entity == "CH":
            items.sort(key=lambda i: _sr_sort_key(i["id"]))
            name = "Federal (SR)"
        else:
            items.sort(key=lambda i: i["id"])
            name = CANTON_NAMES.get(entity.lower(), entity)
        result[entity] = {
            "entity": entity,
            "name": name,
            "laws": len(items),
            "total_chars": sum(l["chars"] for i in items for l in i["languages"].values()),
            "total_articles": sum(l["articles"] for i in items for l in i["languages"].values()),
            "link_base": link_base,
            "raw_base": raw_base,
            "article_count_note": ARTICLE_COUNT_NOTE,
            "items": items,
        }

    logger.info("Law index: %d laws across %d entities",
                sum(v["laws"] for v in result.values()), len(result))
    return result


def build_all_payload(index: dict[str, dict]) -> dict:
    """Merge the per-entity payloads into one compact cross-entity payload.

    Same shape as an entity payload so the site can load it through the same
    code path.  Item ids are entity-prefixed (``AG 110.000``) and the bulky
    per-item fields the cross-entity table never renders (``link``,
    ``version_dates``, category tags) are dropped — the entity files remain the
    place for those.  Keeping ``chars``/``articles`` is the point: without them
    the cross-entity view can only report federal volumes.
    """
    items: list[dict] = []
    for entity, payload in index.items():
        for i in payload["items"]:
            item = {
                "id": f"{entity} {i['id']}",
                "title": i.get("title", ""),
                "languages": {
                    lang: {"chars": d["chars"], "articles": d["articles"],
                           "path": d["path"]}
                    for lang, d in i["languages"].items()
                },
            }
            if i.get("enactment_date"):
                item["enactment_date"] = i["enactment_date"]
            items.append(item)

    first = next(iter(index.values())) if index else {}
    return {
        "entity": "ALL",
        "name": "All entities (Confederation + 26 cantons)",
        "laws": len(items),
        "total_chars": sum(v["total_chars"] for v in index.values()),
        "total_articles": sum(v["total_articles"] for v in index.values()),
        "link_base": first.get("link_base", ""),
        "raw_base": first.get("raw_base", ""),
        "article_count_note": ARTICLE_COUNT_NOTE,
        "items": items,
    }


def write_law_index(index: dict[str, dict], output_dir: str | Path):
    """Write per-entity JSON files + the small master index.json."""
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    entities = {}
    for entity, payload in index.items():
        (out / f"{entity}.json").write_text(
            json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")
        entities[entity] = {
            "name": payload["name"],
            "laws": payload["laws"],
            "total_chars": payload["total_chars"],
            "total_articles": payload["total_articles"],
            "file": f"api/v1/laws/{entity}.json",
        }

    all_payload = build_all_payload(index)
    # Compact (no indent): ~6.5 MB / 1.3 MB gzipped for 34k laws, versus
    # ~24 MB if it were pretty-printed like the per-entity files.
    (out / "ALL.json").write_text(
        json.dumps(all_payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")

    master = {
        "total_laws": sum(v["laws"] for v in entities.values()),
        "link_base": next(iter(index.values()))["link_base"] if index else "",
        "raw_base": next(iter(index.values()))["raw_base"] if index else "",
        "article_count_note": ARTICLE_COUNT_NOTE,
        "all": {
            "name": all_payload["name"],
            "laws": all_payload["laws"],
            "total_chars": all_payload["total_chars"],
            "total_articles": all_payload["total_articles"],
            "file": "api/v1/laws/ALL.json",
        },
        "entities": entities,
    }
    (out / "index.json").write_text(
        json.dumps(master, indent=1, ensure_ascii=False), encoding="utf-8")
    logger.info("Wrote law index (%d entities, %d laws in ALL.json) to %s",
                len(entities), all_payload["laws"], out)
