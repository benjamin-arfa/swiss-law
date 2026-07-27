"""Tests for enactment-based analytics semantics."""
from __future__ import annotations

from legalize_ch.stats import (
    effective_global_category,
    enactment_year,
    generate_chstat_comparison,
    generate_concordats_by_domain,
)


class TestEnactmentYear:
    def test_enactment_beats_version(self):
        assert enactment_year({"enactment_date": "1970-01-01",
                               "version_date": "2015-04-26"}) == "1970"

    def test_min_version_dates_fallback(self):
        assert enactment_year({"version_dates": ["2001-05-01", "1988-03-09"],
                               "version_date": "2001-05-01"}) == "1988"

    def test_version_date_last_resort(self):
        assert enactment_year({"version_date": "2015-04-26"}) == "2015"

    def test_undated(self):
        assert enactment_year({}) == ""


class TestEffectiveGlobalCategory:
    def test_lexfind_precedence(self):
        e = {"global_category": "8.10 Spital",
             "global_category_inferred": "6 Finanzen", "inference_source": "title_keywords"}
        assert effective_global_category(e) == ("8.10 Spital", "lexfind")

    def test_inferred_fallback(self):
        e = {"global_category_inferred": "6 Finanzen", "inference_source": "title_keywords"}
        assert effective_global_category(e) == ("6 Finanzen", "title_keywords")


def _concordat(canton="GR", nr="1.1", enacted=None, version="2015-04-26",
               gc="4.10 Schule", inferred=None):
    e = {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
         "language": "de", "_path": f"ch/{canton.lower()}/de/{nr}.md",
         "category_type": "Interkantonale Vereinbarung",
         "version_date": version}
    if enacted:
        e["enactment_date"] = enacted
    if gc:
        e["global_category"] = gc
    if inferred:
        e["global_category_inferred"] = inferred
        e["inference_source"] = "title_keywords"
    return e


class TestConcordatsEnactmentSemantics:
    def test_old_law_amended_later_counts_under_enactment(self):
        conc = generate_concordats_by_domain(
            [_concordat(enacted="1970-01-01", version="2015-04-26")])
        assert "1970" in conc["by_year"]
        assert "2015" in conc["by_version_year"]
        assert conc["year_semantics"] == "enactment"

    def test_inferred_domain_used_with_provenance(self):
        conc = generate_concordats_by_domain(
            [_concordat(gc=None, inferred="6 Finanzen")])
        assert conc["cantons"]["GR"]["fin"] == 1
        assert conc["domain_provenance"] == {"title_keywords": 1}
        assert conc["unclassified_in_autres"] == 0

    def test_chstat_comparison(self):
        entries = [
            _concordat(nr="a", enacted="1990-01-01", version="2010-01-01"),
            _concordat(nr="b", enacted="2010-01-01"),
            _concordat(nr="c", version=""),  # undated
            {**_concordat(nr="d", enacted="1985-01-01"), "is_active": False},
        ]
        cmp = generate_chstat_comparison(entries)
        gr = cmp["cantons"]["GR"]
        assert gr["ours_enacted_until_2003"] == {
            "active": 1, "repealed_listed": 1, "total": 2}
        assert gr["undated"] == 1
        assert gr["unexplained"] == 67 - 2
        assert cmp["chstat_total"] == 2522
        assert cmp["ours_enacted_until_2003_total"] == 2
