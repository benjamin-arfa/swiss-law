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


class TestYearPlausibilityFloor:
    def test_lexfind_sentinel_is_unknown(self):
        assert enactment_year({"enactment_date": "1000-01-01"}) == ""

    def test_century_typo_in_version_dates_skipped(self):
        # ch/bs/de/561.112.md: lexwork_api typo 1019-02-01 for 2019-02-01
        assert enactment_year({"version_dates": ["1019-02-01", "2019-02-01"],
                               "version_date": "2019-02-01"}) == "2019"

    def test_sentinel_falls_back_to_version_history(self):
        assert enactment_year({"enactment_date": "1000-01-01",
                               "version_dates": ["1998-01-01"]}) == "1998"

    def test_genuine_old_concordat_kept(self):
        assert enactment_year({"enactment_date": "1562-06-01"}) == "1562"

    def test_earliest_known_year_sentinel_undated(self):
        from legalize_ch.stats import earliest_known_year
        e = {"title": "X", "enactment_date": "1000-01-01",
             "enactment_date_source": "lexfind_family"}
        assert earliest_known_year(e, {}) == ("", "undated")

    def test_earliest_known_year_sentinel_uses_other_evidence(self):
        from legalize_ch.stats import earliest_known_year
        e = {"title": "X", "enactment_date": "1000-01-01",
             "enactment_date_source": "lexfind_family",
             "version_dates": ["1998-01-01"]}
        assert earliest_known_year(e, {}) == ("1998", "own_versions")


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
        cmp = generate_chstat_comparison(entries, repo_path="/nonexistent")
        gr = cmp["cantons"]["GR"]
        assert gr["ours_enacted_until_2003"] == {
            "active": 1, "repealed_listed": 1, "repealed_by_2003": 0,
            "total": 2}
        assert gr["undated"] == 1
        assert gr["unexplained"] == 67 - 2
        assert cmp["chstat_total"] == 2522
        assert cmp["ours_enacted_until_2003_total"] == 2

    def test_repeal_dated_before_2004_excluded_from_snapshot(self):
        entries = [
            # repealed 1990 — chstat's 2003 snapshot never held it
            {**_concordat(nr="a", enacted="1970-01-01"),
             "is_active": False, "repealed_date": "1990-06-30"},
            # repealed 2015 — was in force in 2003, stays counted
            {**_concordat(nr="b", enacted="1970-01-01"),
             "is_active": False, "repealed_date": "2015-01-01"},
            # repeal undated — conservatively stays counted
            {**_concordat(nr="c", enacted="1970-01-01"), "is_active": False},
        ]
        cmp = generate_chstat_comparison(entries, repo_path="/nonexistent")
        gr = cmp["cantons"]["GR"]
        assert gr["ours_enacted_until_2003"] == {
            "active": 0, "repealed_listed": 2, "repealed_by_2003": 1,
            "total": 2}
        assert cmp["repealed_by_2003_total"] == 1
        assert cmp["ours_enacted_until_2003_total"] == 2


class TestEarliestKnownEvidence:
    def test_version_history_contradiction_wins(self):
        assert enactment_year({"enactment_date": "2010-01-01",
                               "version_dates": ["1999-05-01", "2010-01-01"]}) == "1999"

    def test_sibling_evidence_only_for_weak_provenance(self):
        from legalize_ch.stats import earliest_known_year
        minima = {"konkordat uber x": "1980-01-01"}
        weak = {"title": "Konkordat über X", "enactment_date": "2010-01-01",
                "enactment_date_source": "text"}
        strong = {"title": "Konkordat über X", "enactment_date": "2010-01-01",
                  "enactment_date_source": "lexwork_api"}
        assert earliest_known_year(weak, minima) == ("1980", "sibling_group")
        # authoritative accession date is canton-specific truth — kept
        assert earliest_known_year(strong, minima) == ("2010", "own_enactment")

    def test_undated_with_group_evidence(self):
        from legalize_ch.stats import earliest_known_year
        minima = {"konkordat uber x": "1980-01-01"}
        e = {"title": "Konkordat über X"}
        assert earliest_known_year(e, minima) == ("1980", "sibling_group")

    def test_truly_undated(self):
        from legalize_ch.stats import earliest_known_year
        assert earliest_known_year({"title": "Y"}, {}) == ("", "undated")


def _accession(canton="GR", nr="9.9", title=None, enacted="1980-01-01",
               ctype="Verordnung des Parlaments (Dekret)"):
    return {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
            "language": "de", "_path": f"ch/{canton.lower()}/de/{nr}.md",
            "category_type": ctype, "enactment_date": enacted,
            "title": title or ("Dekret über den Beitritt des Kantons "
                               "Graubünden zum Konkordat über die Fischerei")}


class TestMembershipEvidence:
    def test_accession_instrument_counted(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        ev = generate_concordat_membership_evidence(
            [_accession()], repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 1
        assert ev["accession"]["GR"][0]["status"] == "counted"
        assert ev["accession"]["GR"][0]["referenced_agreement"] \
            == "Konkordat über die Fischerei"

    def test_accession_not_counted_when_agreement_published(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        conc = {**_concordat(nr="1.2"),
                "title": "Konkordat über die Fischerei"}
        ev = generate_concordat_membership_evidence(
            [conc, _accession()], repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 0
        assert ev["accession"]["GR"][0]["status"] == "published_separately"

    def test_accession_inflection_tolerant_dedup(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        conc = {**_concordat(nr="1.2"),
                "title": "Interkantonale Vereinbarung über die Anerkennung "
                         "von Ausbildungsabschlüssen"}
        acc = _accession(title="Gesetz über den Beitritt zur Interkantonalen "
                               "Vereinbarung über die Anerkennung von "
                               "Ausbildungsabschlüssen", ctype="Gesetz")
        ev = generate_concordat_membership_evidence(
            [conc, acc], repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 0

    def test_accession_after_2003_not_counted(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        ev = generate_concordat_membership_evidence(
            [_accession(enacted="2010-01-01")], repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 0
        assert ev["accession"]["GR"][0]["status"] == "after_2003"

    def test_french_adhesion_pattern(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        acc = _accession(
            canton="JU", ctype="Loi",
            title="Loi portant adhésion de la République et Canton du Jura "
                  "au concordat sur les entreprises de sécurité")
        ev = generate_concordat_membership_evidence(
            [acc], repo_path="/nonexistent")
        assert ev["accession_counted"]["JU"] == 1

    def test_plain_vereinbarung_without_canton_names_ignored(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        acc = _accession(title="Dekret über den Beitritt zur Vereinbarung "
                               "über den Finanzausgleich")
        ev = generate_concordat_membership_evidence(
            [acc], repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 0

    def test_duplicate_instruments_counted_once(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        ev = generate_concordat_membership_evidence(
            [_accession(nr="9.9"), _accession(nr="9.10")],
            repo_path="/nonexistent")
        assert ev["accession_counted"]["GR"] == 1

    def test_chstat_comparison_includes_tiers(self):
        entries = [
            _concordat(nr="a", enacted="1990-01-01"),
            _accession(),
        ]
        cmp = generate_chstat_comparison(entries, repo_path="/nonexistent")
        gr = cmp["cantons"]["GR"]
        assert gr["ours_enacted_until_2003"]["total"] == 1
        assert gr["additional_evidence"] == {"accession": 1, "intlex_named": 0}
        assert gr["explained_total"] == 2
        assert gr["unexplained"] == 67 - 2
        assert cmp["explained_total"] == 2
        assert cmp["accession_evidence_total"] == 1

    def test_exceeds_reference_diagnosis(self):
        entries = [_concordat(canton="TI", nr=str(i),
                              enacted="1990-01-01", gc="4.10 Scuola")
                   for i in range(55)]  # chstat TI total = 44
        cmp = generate_chstat_comparison(entries, repo_path="/nonexistent")
        assert cmp["cantons"]["TI"]["diagnosis"] == "exceeds_reference"

    def test_federal_or_foreign_party_not_counted(self):
        from legalize_ch.stats import generate_concordat_membership_evidence
        acc = _accession(
            canton="NE", ctype="Loi",
            title="Décret portant adhésion du canton de Neuchâtel à l'accord "
                  "entre le Conseil fédéral suisse, agissant au nom des "
                  "cantons de Berne, de Vaud, de Neuchâtel et du Jura, et le "
                  "Gouvernement de la République française relatif à la "
                  "création d'une école")
        ev = generate_concordat_membership_evidence(
            [acc], repo_path="/nonexistent")
        assert ev["accession_counted"]["NE"] == 0
