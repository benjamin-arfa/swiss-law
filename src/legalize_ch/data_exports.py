"""Plain-CSV data exports for the site's data page (api/v1/csv/).

All exports are derived from the already-generated stats dicts — no
repository re-scan.  Three tiers, per the data page's download section:

- ``{slug}_canton_year.csv``: one instrument type, all cantons × all years
- ``laws_cube.csv``: everything — all types, cantons, years and domains
- ``concordats_memberships_since_1848.csv``: the chstat-calibrated
  concordats table (signatory counting, chstat 2003 baseline)
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

from .stats import CONCORDAT_DOMAINS

logger = logging.getLogger(__name__)

SOURCE_LINE = ("Calculs propres basés sur la base de données de l'Institut "
               "pour le fédéralisme (LexFind); https://swiss-law-as-source.github.io")

DOMAIN_KEYS = [d["key"] for d in CONCORDAT_DOMAINS]


def _wide_rows(by_year: dict) -> list[list]:
    """by_year {year: {canton: {domain: n}}} → rows [canton, year, d1..d7, total]."""
    rows = []
    for year in sorted(by_year):
        for canton in sorted(by_year[year]):
            doms = by_year[year][canton]
            vals = [doms.get(k, 0) for k in DOMAIN_KEYS]
            if sum(vals) == 0:
                continue
            rows.append([canton, year, *vals, sum(vals)])
    return rows


def _csv(header_comments: list[str], columns: list[str], rows: list[list]) -> str:
    lines = [f"# {c}" for c in header_comments]
    lines.append(",".join(columns))
    lines.extend(",".join(str(v) for v in row) for row in rows)
    return "\n".join(lines) + "\n"


def generate_csv_exports(type_tables: dict, conc_sig: dict,
                         undated: dict | None = None) -> dict[str, str]:
    """Return {filename: csv_text} for api/v1/csv/.

    ``type_tables`` is ``generate_types_by_domain``'s return value;
    ``conc_sig`` is ``generate_concordats_by_domain_signatories``'s;
    ``undated`` (optional) is ``generate_undated_laws``'s — exported as a
    fillable correction template for the ``legalize-ch import-dates``
    round-trip.
    """
    files: dict[str, str] = {}
    index: list[dict] = []
    wide_cols = ["canton", "year", *DOMAIN_KEYS, "total"]

    for slug, tbl in sorted(type_tables["files"].items()):
        rows = _wide_rows(tbl.get("by_year", {}))
        label = tbl["type"]["label"].get("en") or tbl["type"]["label"].get("de", slug)
        name = f"{slug}_canton_year.csv"
        files[name] = _csv(
            [f"Swiss Law Collection — cantonal acts of type '{label}' by canton, "
             "year and legal domain",
             "counting_unit: published_copies — one count per canton whose "
             "collection publishes the act; this is the unit the site's year "
             "chart uses, so the two agree for any year",
             "year = enactment year; 'unknown' rows are undated laws",
             f"source: {SOURCE_LINE}"],
            wide_cols, rows)
        index.append({"file": name, "rows": len(rows),
                      "description": f"{label}: all cantons × all years × domains"})

    cube_rows = []
    for slug, tbl in sorted(type_tables["files"].items()):
        for year in sorted(tbl.get("by_year", {})):
            for canton in sorted(tbl["by_year"][year]):
                for dom, n in sorted(tbl["by_year"][year][canton].items()):
                    if n:
                        cube_rows.append([slug, canton, year, dom, n])
    files["laws_cube.csv"] = _csv(
        ["Swiss Law Collection — all cantonal acts: instrument type × canton × "
         "enactment year × legal domain",
         "counting_unit: published_copies — one count per canton whose "
         "collection publishes the act",
         f"source: {SOURCE_LINE}"],
        ["instrument_type", "canton", "year", "domain", "count"], cube_rows)
    index.append({"file": "laws_cube.csv", "rows": len(cube_rows),
                  "description": "Everything: all types × cantons × years × domains "
                                 "(long format)"})

    conc_rows = _wide_rows(conc_sig.get("by_year", {}))
    files["concordats_memberships.csv"] = _csv(
        ["Swiss Law Collection — intercantonal agreement memberships, computed: "
         "one occurrence per SIGNING canton per agreement (signed by 10 cantons "
         "-> 10 occurrences)",
         "counting_unit: signatory_memberships — a DIFFERENT unit from the "
         "site's year chart and from interkantonale_vereinbarung_canton_year.csv, "
         "which count published copies: this file also credits signatory cantons "
         "that never published their own copy, and dates each agreement by its "
         "earliest member. Per-year totals therefore differ by design",
         "signatories per agreement = cantons publishing the text in their "
         "collections + cantons named in any language version's title; no "
         "scaling, no external baseline",
         f"source: {SOURCE_LINE}"],
        wide_cols, conc_rows)
    index.append({"file": "concordats_memberships.csv",
                  "rows": len(conc_rows),
                  "description": "Concordat memberships, computed signatory "
                                 "counting (1 per signing canton per agreement)"})

    if undated:
        q = lambda s: '"' + str(s).replace('"', '""') + '"'
        und_rows = [
            [l["entity"], q(l["id"]), q(l["title"]), q(l["category_type"]),
             "|".join(l["languages"]),
             q(json.dumps(l["raw_dates"], ensure_ascii=False)),
             l["enactment_date_source"], l["reason"], l["link"],
             "", ""]   # ← columns for the user to fill
            for l in undated["laws"]
        ]
        files["undated_laws.csv"] = _csv(
            ["Swiss Law Collection — laws without a plausible enactment date "
             "(correction template)",
             "fill corrected_enactment_date (YYYY-MM-DD) and correction_note "
             "(source/citation), then run: legalize-ch import-dates "
             "undated_laws.csv — corrections are applied to the law files as "
             "enactment_date_source: manual_import and improve the statistics "
             "on the next regeneration",
             f"source: {SOURCE_LINE}"],
            ["entity", "id", "title", "category_type", "languages",
             "raw_dates", "enactment_date_source", "reason", "link",
             "corrected_enactment_date", "correction_note"],
            und_rows)
        index.append({"file": "undated_laws.csv", "rows": len(und_rows),
                      "description": "Undated laws — fillable correction "
                                     "template for legalize-ch import-dates"})

    files["index.json"] = json.dumps({
        "note": "Static CSV exports; regenerated with `legalize-ch stats`. "
                "SDMX versions: /api/sdmx/",
        "source": SOURCE_LINE,
        "files": index,
    }, indent=2, ensure_ascii=False) + "\n"
    return files


def write_csv_exports(files: dict[str, str], out_dir: str | Path) -> None:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")
    logger.info("Wrote %d CSV exports to %s", len(files), out)
