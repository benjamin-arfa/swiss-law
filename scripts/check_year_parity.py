#!/usr/bin/env python3
"""Post-regeneration check: the dashboard's chart and its table agree.

Reads the PUBLISHED site artifacts (no repo re-scan, runs in a second) and
asserts, for every instrument type and every year, that stats.json's
year x canton x type cube and api/v1/stats/types/<slug>_by_domain.json
report the same total — the invariant that broke when the two were built
with different year rules (concordats disagreed across 55 years: 2001 was
75 in the chart and 76 in the table, 2002 was 91 vs 90).

Also checks that the two concordat tables declare their counting units, so
a number on one unit is never published as if it were the other.

    ./scripts/check_year_parity.py [--site-repo /home/ubuntu/swiss-law-as-source]

Exit code 0 = parity holds, 1 = a mismatch (do not deploy).
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

DEFAULT_SITE = Path("/home/ubuntu/swiss-law-as-source")


def _by_year_totals(table: dict) -> dict[str, int]:
    return {y: sum(sum(row.values()) for row in cantons.values())
            for y, cantons in table.get("by_year", {}).items()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--site-repo", type=Path, default=DEFAULT_SITE)
    args = ap.parse_args()
    site: Path = args.site_repo

    load = lambda rel: json.loads((site / rel).read_text())

    try:
        stats = load("stats.json")
        index = load("api/v1/stats/types/index.json")
    except FileNotFoundError as e:
        print(f"FAIL: missing artifact {e.filename} — run `legalize-ch stats` first")
        return 1

    cube_by_year: dict[str, collections.Counter] = collections.defaultdict(
        collections.Counter)
    for year, cantons in stats["category_type_by_canton_by_year"].items():
        for per_type in cantons.values():
            for label_de, n in per_type.items():
                cube_by_year[year][label_de] += n

    problems = 0
    print(f"{'instrument type':34}{'mismatching years':>18}")
    for t in index["types"]:
        slug = t["slug"]
        label_de = t["label"].get("de")
        table = load(f"api/v1/stats/types/{slug}_by_domain.json")
        table_years = _by_year_totals(table)
        years = (set(table_years) | set(cube_by_year)) - {"unknown"}
        mismatched = sorted(
            y for y in years
            if table_years.get(y, 0) != cube_by_year.get(y, {}).get(label_de, 0))
        problems += len(mismatched)
        print(f"{slug:34}{len(mismatched):>18}"
              + ("   e.g. " + ", ".join(
                  f"{y}: chart {cube_by_year.get(y, {}).get(label_de, 0)} != "
                  f"table {table_years.get(y, 0)}" for y in mismatched[:3])
                 if mismatched else ""))

    # concordats_by_domain.json duplicates the intercantonal per-type table
    conc = load("api/v1/stats/concordats_by_domain.json")
    ikv = load("api/v1/stats/types/interkantonale_vereinbarung_by_domain.json")
    if _by_year_totals(conc) != _by_year_totals(ikv):
        print("FAIL: concordats_by_domain.json disagrees with its per-type table")
        problems += 1

    # units must be declared, and must be the two distinct ones
    sig = load("api/v1/stats/concordats_by_domain_signatories.json")
    units = {
        "concordats_by_domain.json": conc.get("counting_unit"),
        "types/interkantonale_vereinbarung_by_domain.json": ikv.get("counting_unit"),
        "concordats_by_domain_signatories.json": sig.get("counting_unit"),
    }
    print()
    for name, unit in units.items():
        print(f"  counting_unit  {name:56} {unit}")
    expected = {"concordats_by_domain.json": "published_copies",
                "types/interkantonale_vereinbarung_by_domain.json": "published_copies",
                "concordats_by_domain_signatories.json": "signatory_memberships"}
    if units != expected:
        print("FAIL: counting units are not declared as expected")
        problems += 1

    print(f"\n{'PASS — chart and tables agree' if not problems else f'FAIL — {problems} problems'}")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
