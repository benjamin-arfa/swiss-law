"""Tests for per-instrument-type domain tables and the signatories export."""
from __future__ import annotations

from legalize_ch.stats import (
    generate_concordat_signatories,
    generate_concordats_by_domain,
    generate_types_by_domain,
)


def _law(canton="GR", nr="1.1", lang="de", ctype="Gesetz",
         gc="4.10 Schule", enacted="1990-01-01", title="Schulgesetz"):
    return {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
            "language": lang, "_path": f"ch/{canton.lower()}/{lang}/{nr}.md",
            "category_type": ctype, "global_category": gc,
            "enactment_date": enacted, "version_date": "2015-01-01",
            "title": title}


class TestGenerateTypesByDomain:
    def test_language_dedup_and_cell_placement(self):
        entries = [
            _law(lang="de"),
            _law(lang="fr", ctype="Loi"),  # same law, French file
            _law(canton="BE", nr="2.2", ctype="Verordnung", gc="6.10 Steuern"),
        ]
        result = generate_types_by_domain(entries)
        gesetz = result["files"]["gesetz"]
        assert gesetz["total"] == 1  # not 2 — languages collapsed
        assert gesetz["cantons"]["GR"]["educ"] == 1
        vo = result["files"]["verordnung"]
        assert vo["cantons"]["BE"]["fin"] == 1
        assert vo["type"]["label"]["fr"] == "Ordonnance"

    def test_by_year_totals_match(self):
        entries = [
            _law(nr="a", enacted="1990-01-01"),
            _law(nr="b", enacted="2001-01-01"),
            _law(nr="c", enacted=""),  # falls back to version_date 2015
        ]
        gesetz = generate_types_by_domain(entries)["files"]["gesetz"]
        year_total = sum(
            n for cantons in gesetz["by_year"].values()
            for doms in cantons.values() for n in doms.values())
        assert year_total == gesetz["totals"]["total"] == 3

    def test_sentinel_year_lands_in_unknown(self):
        entries = [{**_law(enacted="1000-01-01"), "version_date": ""}]
        gesetz = generate_types_by_domain(entries)["files"]["gesetz"]
        assert "1000" not in gesetz["by_year"]
        assert gesetz["by_year"]["unknown"]["GR"]["educ"] == 1

    def test_index_sorted_by_total(self):
        entries = [
            _law(nr="a"), _law(nr="b"),
            _law(nr="c", ctype="Verordnung"),
        ]
        idx = generate_types_by_domain(entries)["index"]
        assert [t["slug"] for t in idx["types"]] == ["gesetz", "verordnung"]
        assert idx["types"][0]["path"] == "api/v1/stats/types/gesetz_by_domain.json"


class TestConcordatsBackwardCompat:
    def test_output_keys_unchanged(self):
        conc = generate_concordats_by_domain(
            [_law(ctype="Interkantonale Vereinbarung")])
        expected = {"title", "source", "total_concordats", "domains", "cantons",
                    "totals", "year_semantics", "by_year", "by_version_year",
                    "unclassified_in_autres", "domain_provenance",
                    "year_evidence", "notes"}
        assert expected <= set(conc)
        assert conc["total_concordats"] == 1


class TestGenerateConcordatSignatories:
    def test_siblings_group_across_cantons_and_languages(self):
        title = "Konkordat über die Schulen"
        entries = [
            _law(canton="GR", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1970-01-01"),
            _law(canton="BE", nr="9.9", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1970-01-01"),
            # second language file of the GR copy — must not add a signatory
            _law(canton="GR", nr="1.1", lang="it",
                 ctype="Accordo intercantonale", title=title,
                 enacted="1970-01-01"),
            # unrelated agreement stays separate
            _law(canton="ZH", nr="5.5", ctype="Interkantonale Vereinbarung",
                 title="Vereinbarung über die Fischerei", enacted="1980-01-01"),
        ]
        sig = generate_concordat_signatories(entries)
        assert sig["total_agreements"] == 2
        first = sig["agreements"][0]
        assert first["signatories"] == ["BE", "GR"]
        assert first["n_signatories"] == 2
        assert first["year"] == "1970"
        assert first["per_canton"]["GR"]["systematic_number"] == "1.1"
        second = sig["agreements"][1]
        assert second["signatories"] == ["ZH"]

    def test_non_concordats_excluded(self):
        sig = generate_concordat_signatories([_law(ctype="Gesetz")])
        assert sig["total_agreements"] == 0


class TestGenerateUndatedLaws:
    def test_sentinel_and_missing_dates_listed(self):
        from legalize_ch.stats import generate_undated_laws
        entries = [
            {**_law(canton="BE", nr="669.1", enacted="1000-01-01"),
             "version_date": ""},                       # sentinel only
            {**_law(canton="GR", nr="9.9", enacted=""), "version_date": ""},  # nothing
            _law(canton="ZH", nr="1.1", enacted="1990-01-01"),  # dated — excluded
        ]
        und = generate_undated_laws(entries)
        assert und["total"] == 2
        assert und["by_reason"] == {"implausible_date": 1, "no_date": 1}
        be = next(l for l in und["laws"] if l["entity"] == "BE")
        assert be["raw_dates"]["enactment_date"] == "1000-01-01"
        assert be["link"].endswith("ch/be/de/669.1.md")

    def test_language_dedup(self):
        from legalize_ch.stats import generate_undated_laws
        entries = [
            {**_law(canton="GR", nr="9.9", enacted=""), "version_date": ""},
            {**_law(canton="GR", nr="9.9", lang="it", enacted=""), "version_date": ""},
        ]
        assert generate_undated_laws(entries)["total"] == 1


class TestCantonsNamedInTitle:
    def test_german_and_french_variants(self):
        from legalize_ch.stats import cantons_named_in_title
        assert cantons_named_in_title(
            "Vereinbarung zwischen den Kantonen Zürich und Graubünden") == ["GR", "ZH"]
        assert cantons_named_in_title(
            "Accord entre les cantons de Genève et de Neuchâtel") == ["GE", "NE"]

    def test_bare_basel_means_bs(self):
        from legalize_ch.stats import cantons_named_in_title
        assert cantons_named_in_title("Konkordat mit Basel") == ["BS"]
        assert cantons_named_in_title(
            "Vereinbarung mit Basel-Landschaft") == ["BL"]

    def test_no_false_positives(self):
        from legalize_ch.stats import cantons_named_in_title
        assert cantons_named_in_title("Konkordat über die Schulen") == []


class TestSignatoryWeightedTable:
    def test_agreement_counts_once_per_signatory(self):
        from legalize_ch.stats import generate_concordats_by_domain_signatories
        title = "Vereinbarung zwischen den Kantonen Zürich, Bern und Luzern"
        entries = [
            # only two of the three named cantons publish the text
            _law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1990-01-01"),
            _law(canton="BE", nr="9.9", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1990-01-01"),
        ]
        conc = generate_concordats_by_domain_signatories(entries)
        # the user's rule: signed by 3 cantons → the year total is 3, not 1
        assert conc["total_memberships"] == 3
        assert conc["total_agreements"] == 1
        assert conc["cantons"]["LU"]["educ"] == 1   # named, not published
        assert conc["memberships_added_by_title_evidence"] == 1
        year_total = sum(n for cs in conc["by_year"]["1990"].values()
                         for n in cs.values())
        assert year_total == 3

    def test_until_2003_counter(self):
        from legalize_ch.stats import generate_concordats_by_domain_signatories
        pre = "Vereinbarung zwischen den Kantonen Zürich und Bern"
        post = "Vereinbarung zwischen den Kantonen Genf und Waadt"
        entries = [
            _law(canton="ZH", nr="a", ctype="Interkantonale Vereinbarung",
                 title=pre, enacted="1990-01-01"),
            _law(canton="GE", nr="b", ctype="Interkantonale Vereinbarung",
                 title=post, enacted="2010-01-01"),
        ]
        conc = generate_concordats_by_domain_signatories(entries)
        # only the 1990 concordat is ≤2003; it has two parties → 2 memberships
        assert conc["concordats_until_2003"] == 1
        assert conc["memberships_until_2003"] == 2
        assert conc["chstat_2003_reference"] == 2522

    def test_single_party_groups_are_not_concordats(self):
        from legalize_ch.stats import generate_concordats_by_domain_signatories
        entries = [
            # no second canton is evidenced anywhere: an unresolved membership,
            # not a one-canton concordat
            _law(canton="ZH", nr="a", ctype="Interkantonale Vereinbarung",
                 title="Konkordat A", enacted="1990-01-01"),
        ]
        conc = generate_concordats_by_domain_signatories(entries)
        assert conc["min_parties"] == 2
        assert conc["unresolved_single_party_groups"] == 1
        assert conc["total_agreements"] == 0
        assert conc["concordats_until_2003"] == 0
        assert conc["memberships_until_2003"] == 0

    def test_repeal_dated_before_2003_drops_the_canton(self):
        from legalize_ch.stats import generate_concordats_by_domain_signatories
        title = "Vereinbarung zwischen den Kantonen Zürich, Bern und Luzern"
        entries = [
            _law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1990-01-01"),
            _law(canton="BE", nr="9.9", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1990-01-01"),
        ]
        # ZH repealed its copy in 1995 — it was not in the 2003 stock, but the
        # title still names it, so title evidence keeps the membership
        zh: dict = entries[0]
        zh["is_active"] = False
        zh["repealed_date"] = "1995-06-01"
        conc = generate_concordats_by_domain_signatories(entries)
        assert conc["memberships_until_2003"] == 3
        ev = conc["memberships_until_2003_by_evidence"]
        # ZH is no longer counted as publishing-in-own-collection
        assert ev["published_in_own_collection"] == 1
        assert ev["named_in_title_only"] == 2

    def test_shape_matches_legacy_table(self):
        from legalize_ch.stats import generate_concordats_by_domain_signatories
        conc = generate_concordats_by_domain_signatories(
            [_law(ctype="Interkantonale Vereinbarung")])
        for key in ("title", "source", "domains", "cantons", "totals",
                    "year_semantics", "by_year", "notes", "total_concordats"):
            assert key in conc, key

    def test_signatories_export_includes_named(self):
        title = "Vereinbarung zwischen den Kantonen Zürich und Bern"
        sig = generate_concordat_signatories(
            [_law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                  title=title)])
        a = sig["agreements"][0]
        assert a["published"] == ["ZH"]
        assert a["named_in_title"] == ["BE", "ZH"]
        assert a["signatories"] == ["BE", "ZH"]
        assert a["n_signatories"] == 2


class TestConcordatPreamble:
    def test_stops_at_first_article(self):
        from legalize_ch.stats import concordat_preamble
        body = ("Konkordat\n\nDie Kantone Zürich und Bern vereinbaren:\n\n"
                "Art. 1\nDer Kanton Luzern wird hier nur zitiert.\n")
        pre = concordat_preamble(body)
        assert "vereinbaren" in pre
        assert "Luzern" not in pre  # cross-reference, not a party

    def test_no_article_marker_falls_back_to_head(self):
        from legalize_ch.stats import concordat_preamble
        assert concordat_preamble("Nur Fliesstext ohne Artikel").startswith("Nur")


class TestCantonsNamedAsParties:
    def test_enumerated_parties_are_extracted(self):
        from legalize_ch.stats import cantons_named_as_parties
        pre = ("Konkordat\n\nabgeschlossen zwischen den Kantonen Zürich, "
               "Luzern, Basel-Stadt und St. Gallen.\n")
        assert cantons_named_as_parties(pre) == ["BS", "LU", "SG", "ZH"]

    def test_open_concordat_without_named_members_yields_nothing(self):
        from legalize_ch.stats import cantons_named_as_parties
        assert cantons_named_as_parties("Die unterzeichnenden Kantone,\n"
                                        "vereinbaren:\n") == []

    def test_incidental_mention_without_party_marker_is_ignored(self):
        from legalize_ch.stats import cantons_named_as_parties
        # a seat-of-institution mention must not create a membership
        assert cantons_named_as_parties(
            "Vereinbarung über die Tollwutzentrale an der Universität Bern\n"
            "Vom 10. April 1991\n") == []


class TestSizeDistribution:
    def test_reproduces_bands_and_excludes_single_party_records(self):
        from legalize_ch.stats import generate_concordat_size_distribution
        title = "Vereinbarung zwischen den Kantonen Zürich, Bern und Luzern"
        entries = [
            _law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="1990-01-01"),
            # a record we can only tie to one canton: not a concordat count
            _law(canton="GR", nr="7.7", ctype="Interkantonale Vereinbarung",
                 title="Vereinbarung über das Schulwesen", enacted="1995-01-01"),
        ]
        dist = generate_concordat_size_distribution(entries)
        assert dist["ours"]["concordats"] == 1
        assert dist["ours"]["memberships"] == 3
        assert dist["ours"]["unresolved_single_party"] == 1
        band = {b["band"]: b for b in dist["bands"]}["3-4"]
        assert band["ours_concordats"] == 1
        assert dist["baseline"]["total_concordats"] == 733
        assert dist["baseline"]["total_memberships"] == 2564

    def test_post_2003_agreements_are_out_of_scope(self):
        from legalize_ch.stats import generate_concordat_size_distribution
        title = "Vereinbarung zwischen den Kantonen Zürich und Bern"
        entries = [
            _law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title=title, enacted="2010-01-01"),
        ]
        assert generate_concordat_size_distribution(entries)["ours"][
            "concordats"] == 0


class TestBadacBaseline:
    def test_bands_sum_to_the_published_totals(self):
        from legalize_ch.stats import badac_baseline_bands
        bands = badac_baseline_bands()
        assert sum(b["memberships"] for b in bands) == 2564
        # implied concordat counts reconstruct 733 to within rounding
        assert 720 <= sum(b["concordats_implied"] for b in bands) <= 740
        assert abs(sum(b["share_of_memberships"] for b in bands) - 1.0) < 1e-9

    def test_representative_size_defaults_to_the_computed_band_midpoint(self):
        from legalize_ch.stats import badac_baseline_bands
        bands = {b["band"]: b for b in badac_baseline_bands()}
        assert all(b["representative_size_basis"] == "band_midpoint"
                   for b in bands.values())
        # midpoints are computed from the band bounds, not written down
        for b in bands.values():
            assert b["representative_size"] == (b["lower"] + b["upper"]) / 2

    def test_observed_sizes_override_the_midpoint(self):
        from legalize_ch.stats import badac_baseline_bands
        # 8 concordats totalling 40 memberships -> mean size 5.0, not the
        # 7.5 midpoint of the 5-10 band
        bands = {b["band"]: b
                 for b in badac_baseline_bands({"5-10": (8, 40)})}
        five = bands["5-10"]
        assert five["representative_size"] == 5.0
        assert five["representative_size_basis"] == "observed_mean"
        assert five["concordats_implied"] == round(five["memberships"] / 5.0)
        # untouched bands keep the midpoint basis
        assert bands["2"]["representative_size_basis"] == "band_midpoint"

    def test_size_distribution_reconstruction_is_computed_from_our_data(self):
        from legalize_ch.stats import generate_concordat_size_distribution
        entries = [
            _law(canton="ZH", nr="1.1", ctype="Interkantonale Vereinbarung",
                 title="Vereinbarung zwischen den Kantonen Zürich, Bern, "
                       "Luzern und Uri", enacted="1990-01-01"),
        ]
        dist = generate_concordat_size_distribution(entries)
        rec = dist["baseline"]["reconstruction"]
        assert rec["stated_total"] == dist["baseline"]["total_concordats"]
        assert rec["concordats_implied_total"] == sum(
            b["badac_concordats_implied"] for b in dist["bands"])
        assert rec["accuracy"] == round(
            rec["concordats_implied_total"] / rec["stated_total"], 4)
        # the 3-4 band saw one 4-canton agreement: mean size 4.0 is used
        band = {b["band"]: b for b in dist["bands"]}["3-4"]
        assert band["ours_mean_size"] == 4.0
        assert band["badac_representative_size"] == 4.0
        assert band["badac_representative_size_basis"] == "observed_mean"
        assert rec["size_basis"]["3-4"] == "observed_mean"
        assert rec["size_basis"]["20-26"] == "band_midpoint"

    def test_baseline_prose_is_derived_not_restated(self):
        from legalize_ch.stats import (BADAC_2003_TOTAL_CONCORDATS,
                                       BADAC_2003_TOTAL_MEMBERSHIPS,
                                       generate_concordat_size_distribution)
        base = generate_concordat_size_distribution([])["baseline"]
        assert str(BADAC_2003_TOTAL_MEMBERSHIPS) in base["weighting"]
        assert str(BADAC_2003_TOTAL_CONCORDATS) in base["weighting"]
        assert base["mean_signatories"] == round(
            BADAC_2003_TOTAL_MEMBERSHIPS / BADAC_2003_TOTAL_CONCORDATS, 2)
