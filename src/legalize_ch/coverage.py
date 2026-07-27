"""Coverage audit — prove the local collection matches the source catalogs.

For every canton, compares the LexFind catalog (ALL instrument types)
against local ``ch/<canton>/<lang>/`` files and reports what is missing,
broken down by category type. For federal law, compares local SR numbers
against the Fedlex catalog. This is the guarantee that every law type is
fetched — gaps become visible (and the weekly backfill closes them)
instead of being discovered ad hoc.
"""
from __future__ import annotations

import json
import logging
from collections import Counter
from pathlib import Path

from .cantonal import ALL_CANTONS, CANTON_LANGUAGES, CantonalFetcher, canton_to_path
from .categories import canonical_category_type

logger = logging.getLogger(__name__)

_LEXFIND_LANGUAGES = ("de", "fr", "it")

COVERAGE_NOTE = (
    "Cantonal reference: LexFind systematics catalog (all instrument types, "
    "active and repealed). Laws absent from LexFind's systematics tree "
    "entirely are invisible to this audit. Federal reference: Fedlex catalog."
)


def canton_coverage(repo_path: Path, canton: str,
                    fetcher: CantonalFetcher) -> dict:
    """Compare one canton's local files against the LexFind catalog."""
    langs = [l for l in CANTON_LANGUAGES.get(canton, ["de"]) if l in _LEXFIND_LANGUAGES]
    by_type: dict[str, Counter] = {}
    catalog_total = present_total = 0

    for lang in langs:
        catalog = fetcher._fetch_lexfind_catalog_by_systematics(canton, lang)
        for entry in catalog:
            ctype = canonical_category_type(entry.category_type or "") or "(untyped)"
            c = by_type.setdefault(ctype, Counter())
            c["catalog"] += 1
            catalog_total += 1
            if (repo_path / canton_to_path(canton, entry.systematic_number, lang)).exists():
                c["present"] += 1
                present_total += 1

    return {
        "canton": canton.upper(),
        "languages": langs,
        "catalog": catalog_total,
        "present": present_total,
        "missing": catalog_total - present_total,
        "by_type": {
            t: {"catalog": c["catalog"], "present": c["present"],
                "missing": c["catalog"] - c["present"]}
            for t, c in sorted(by_type.items(), key=lambda kv: -kv[1]["catalog"])
        },
    }


def federal_coverage(repo_path: Path, rate_limit: float = 1.0) -> dict:
    """Compare local federal SR numbers against the Fedlex catalog."""
    from .fetcher import FedlexFetcher
    from .stats import collect_all_frontmatter

    local_srs = {
        str(e.get("sr_number"))
        for e in collect_all_frontmatter(repo_path)
        if e.get("_scope") == "federal" and e.get("sr_number")
    }
    try:
        fetcher = FedlexFetcher(rate_limit=rate_limit)
        catalog = fetcher.fetch_catalog()
        catalog_srs = {str(law.sr_number) for law in catalog if law.sr_number}
    except Exception as e:
        logger.warning("Fedlex catalog unavailable: %s", e)
        return {"catalog": None, "present": len(local_srs), "missing": None,
                "error": f"Fedlex catalog unavailable: {e}"}

    missing = sorted(catalog_srs - local_srs)
    return {
        "catalog": len(catalog_srs),
        "present": len(local_srs),
        "missing": len(missing),
        "missing_sample": missing[:50],
    }


def run_coverage(repo_path: str | Path, cantons: list[str] | None = None,
                 rate_limit: float = 1.0, include_federal: bool = True) -> dict:
    """Full coverage report. Returns the report dict."""
    repo_path = Path(repo_path)
    cantons = [c.lower() for c in (cantons or ALL_CANTONS)]
    fetcher = CantonalFetcher(rate_limit=rate_limit)

    report: dict = {"note": COVERAGE_NOTE, "cantons": {}, "total_missing": 0}
    for canton in cantons:
        try:
            cov = canton_coverage(repo_path, canton, fetcher)
        except Exception as e:
            logger.exception("Coverage failed for %s", canton.upper())
            cov = {"canton": canton.upper(), "error": str(e),
                   "catalog": 0, "present": 0, "missing": -1, "by_type": {}}
        report["cantons"][canton.upper()] = cov
        report["total_missing"] += max(cov.get("missing", 0), 0)
        logger.info("%s: catalog=%s present=%s missing=%s",
                    canton.upper(), cov.get("catalog"), cov.get("present"),
                    cov.get("missing"))

    if include_federal:
        report["federal"] = federal_coverage(repo_path, rate_limit)
        if isinstance(report["federal"].get("missing"), int):
            report["total_missing"] += report["federal"]["missing"]

    return report


def write_coverage(report: dict, output_path: str | Path):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=1, ensure_ascii=False),
                    encoding="utf-8")
    logger.info("Wrote coverage report to %s (total missing: %s)",
                path, report.get("total_missing"))
