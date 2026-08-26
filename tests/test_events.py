"""Tests for the legal event stream — one record per (law, date)."""
from __future__ import annotations

from legalize_ch.events import (
    aggregate_events,
    build_events,
    compute_indicators,
    is_consolidation,
    law_key,
)

CO_SUBJECT = ("SR 220: Bundesgesetz vom 30. März 1911 betreffend die Ergänzung des "
              "Schweizerischen Zivilgesetzbuches (Fünfter Teil: Obligationenrecht) (2025-01-01)")


def _fed(sr="220", lang="de", **kw):
    e = {
        "sr_number": sr,
        "language": lang,
        "_scope": "federal",
        "_path": f"ch/{lang}/{sr}.md",
        "_body_chars": 1000,
        "_body_articles": 12,
    }
    e.update(kw)
    return e


def _cant(canton="ZH", num="131.1", lang="de", **kw):
    e = {
        "systematic_number": num,
        "canton": canton,
        "language": lang,
        "_scope": "cantonal",
        "_path": f"ch/{canton.lower()}/{lang}/{num}.md",
        "_body_chars": 500,
        "_body_articles": 4,
    }
    e.update(kw)
    return e


class TestConsolidationFilter:
    def test_backdated_consolidation_accepted(self):
        assert is_consolidation(CO_SUBJECT, "2025-01-01")

    def test_bulk_metadata_commit_rejected(self):
        # the commit that contaminated version_dates for every federal law
        assert not is_consolidation(
            "data: enactment dates + version histories + inferred domains for all laws",
            "2026-07-27")

    def test_backfill_commit_rejected(self):
        assert not is_consolidation("Backfill ZH: 1 law files from LexFind", "2026-08-24")

    def test_date_must_match_author_date(self):
        # a consolidation subject replayed by a later rewrite is not an event
        # on the rewrite's date
        assert not is_consolidation(CO_SUBJECT, "2026-07-27")


class TestLawKey:
    def test_language_versions_share_one_key(self):
        assert law_key(_fed(lang="de")) == law_key(_fed(lang="fr")) == "federal/220"

    def test_cantonal_key_is_canton_scoped(self):
        assert law_key(_cant()) == "ZH/131.1"


class TestBuildEvents:
    def test_git_history_dates_without_a_consolidation_are_dropped(self):
        """The 2026 enrichment window is not a legislative event."""
        entries = [_fed(version_date="2025-01-01",
                        version_dates=["1911-01-01", "2025-01-01", "2026-07-27"],
                        version_dates_source="git_history")]
        cons = {"ch/de/220.md": ["2025-01-01"]}
        dates = [e["date"] for e in build_events(entries, cons)]
        assert dates == ["2025-01-01"]

    def test_authoritative_version_dates_are_kept_whole(self):
        entries = [_cant(version_date="2020-05-01",
                         version_dates=["1998-01-01", "2010-03-01", "2020-05-01"],
                         version_dates_source="lexfind_family")]
        evs = build_events(entries, {})
        assert [e["date"] for e in evs] == ["1998-01-01", "2010-03-01", "2020-05-01"]
        assert [e["event"] for e in evs] == ["publication", "revision", "revision"]
        assert [e["seq"] for e in evs] == [0, 1, 2]

    def test_git_derived_enactment_date_is_dropped_too(self):
        entries = [_fed(enactment_date="2026-07-27", enactment_date_source="git_history",
                        version_date="2025-01-01")]
        assert [e["date"] for e in build_events(entries, {})] == ["2025-01-01"]

    def test_a_federal_consolidation_never_dates_a_cantonal_law(self):
        """Cantonal files that rode along in a federal batch commit must not
        inherit the federal act's entry into force."""
        entries = [_cant(version_date="2019-01-01")]
        cons = {"ch/zh/de/131.1.md": ["2020-02-01"]}
        assert [e["date"] for e in build_events(entries, cons)] == ["2019-01-01"]

    def test_language_versions_of_one_consolidation_are_one_event(self):
        entries = [_fed(lang=lang, version_date="2025-01-01") for lang in ("de", "fr", "it")]
        cons = {f"ch/{lang}/220.md": ["2025-01-01"] for lang in ("de", "fr", "it")}
        assert len(build_events(entries, cons)) == 1

    def test_publication_is_the_earliest_date(self):
        entries = [_fed(enactment_date="1911-03-30", enactment_date_source="text",
                        version_date="2025-01-01")]
        evs = build_events(entries, {"ch/de/220.md": ["2024-01-01"]})
        assert (evs[0]["date"], evs[0]["event"], evs[0]["seq"]) == ("1911-03-30", "publication", 0)
        assert [e["event"] for e in evs[1:]] == ["revision", "revision"]

    def test_reconciles_with_the_law_count(self):
        """publications == laws with a date; events >= laws. The whole point of
        keeping both counting units on the page."""
        entries = [
            _fed(version_date="2025-01-01"),
            _cant(version_dates=["1998-01-01", "2010-03-01"],
                  version_dates_source="lexfind_family", version_date="2010-03-01"),
            _cant(canton="BE", num="101", version_date="1999-09-09"),
            _cant(canton="VD", num="7.1"),  # no date at all — contributes nothing
        ]
        evs = build_events(entries, {})
        pubs = [e for e in evs if e["event"] == "publication"]
        assert len(pubs) == 3
        assert len(evs) >= len(pubs)
        assert {e["law"] for e in pubs} == {"federal/220", "ZH/131.1", "BE/101"}

    def test_delta_is_attached_from_the_german_file_only(self):
        """Summing three translations of one amendment would treble it."""
        entries = [_fed(lang=lang, version_date="2025-01-01") for lang in ("de", "fr")]
        cons = {f"ch/{lang}/220.md": ["2024-01-01", "2025-01-01"] for lang in ("de", "fr")}
        deltas = {
            "ch/de/220.md": {"2024-01-01": {"lines_added": 9000, "lines_removed": 0},
                             "2025-01-01": {"lines_added": 1908, "lines_removed": 96}},
            "ch/fr/220.md": {"2024-01-01": {"lines_added": 8800, "lines_removed": 0},
                             "2025-01-01": {"lines_added": 1850, "lines_removed": 90}},
        }
        evs = build_events(entries, cons, deltas)
        assert [e["date"] for e in evs] == ["2024-01-01", "2025-01-01"]
        assert evs[1]["delta"] == {"lines_added": 1908, "lines_removed": 96}

    def test_the_import_commit_carries_no_magnitude(self):
        """A backfilled act shows its whole body as lines added on the day it
        was imported; counting that would measure our collection work."""
        entries = [_fed(version_dates=["2019-01-01", "2022-01-01", "2025-01-01"],
                        version_dates_source="fedlex")]
        deltas = {"ch/de/220.md": {
            "2022-01-01": {"lines_added": 3000, "lines_removed": 0},   # the import
            "2025-01-01": {"lines_added": 12, "lines_removed": 4},
        }}
        evs = build_events(entries, {}, deltas)
        assert [("delta" in e) for e in evs] == [False, False, True]
        assert evs[2]["delta"] == {"lines_added": 12, "lines_removed": 4}

    def test_size_is_reported_on_the_current_version_only(self):
        entries = [_fed(version_dates=["2020-01-01", "2025-01-01"],
                        version_dates_source="lexfind_family")]
        evs = build_events(entries, {})
        assert "size_current" not in evs[0]
        assert evs[1]["size_current"] == {"chars": 1000, "articles": 12}

    def test_constant_and_empty_fields_are_not_written(self):
        """140k records x a null key is megabytes on every weekly rebuild."""
        (ev,) = build_events([_fed(version_date="2025-01-01")], {})
        assert "canton" not in ev and "domain" not in ev and "confidence" not in ev
        (cev,) = build_events([_cant(version_date="2020-05-01",
                                     global_category="1.50 Verwaltung")], {})
        assert cev["canton"] == "ZH" and cev["domain"] == "1.50 Verwaltung"


class TestAggregate:
    def test_cube_splits_by_scope_and_kind(self):
        entries = [
            _fed(version_dates=["2024-01-01", "2025-01-01"], version_dates_source="fedlex"),
            _cant(version_dates=["2025-06-01"], version_dates_source="lexfind_family"),
        ]
        cube = aggregate_events(build_events(entries, {}), {"commits_scanned": 7})
        assert cube["totals"] == {"events": 3, "publications": 2, "revisions": 1,
                                  "laws_with_events": 2}
        assert cube["by_year"]["2025"]["federal"]["revision"] == 1
        assert cube["by_year"]["2025"]["cantonal"]["publication"] == 1
        assert cube["provenance"]["commits_scanned"] == 7


class TestIndicators:
    def test_churn_and_instability_are_normalised_by_the_stock(self):
        entries = [
            _fed(sr="1", version_dates=["2020-01-01", "2024-01-01", "2024-07-01"],
                 version_dates_source="fedlex"),
            _fed(sr="2", version_dates=["2020-01-01"], version_dates_source="fedlex"),
        ]
        ind = compute_indicators(build_events(entries, {}), entries)["by_year"]["2024"]["federal"]
        assert ind["laws_in_force"] == 2
        assert ind["revisions"] == 2
        assert ind["laws_revised"] == 1
        assert ind["churn"] == 1.0            # 2 revisions / 2 laws
        assert ind["instability"] == 0.5      # 1 of 2 laws moved
        assert ind["median_gap_months"] == 27.0   # 48 months and 6 months

    def test_all_scope_is_pooled_not_averaged(self):
        """The median of two scopes is not the average of their medians."""
        entries = [
            _fed(sr="1", version_dates=["2020-01-01", "2024-01-01"],
                 version_dates_source="fedlex"),
            _cant(version_dates=["2023-01-01", "2024-01-01"],
                  version_dates_source="lexfind_family"),
        ]
        by_year = compute_indicators(build_events(entries, {}), entries)["by_year"]["2024"]
        assert by_year["federal"]["median_gap_months"] == 48.0
        assert by_year["cantonal"]["median_gap_months"] == 12.0
        assert by_year["all"]["median_gap_months"] == 30.0   # median(48, 12)
        assert by_year["all"]["laws_in_force"] == 2
        assert by_year["all"]["revisions"] == 2

    def test_repealed_laws_leave_the_stock(self):
        entries = [
            _fed(sr="1", version_dates=["2000-01-01"], version_dates_source="fedlex",
                 repealed_date="2010-01-01"),
            _fed(sr="2", version_dates=["2000-01-01", "2020-01-01"],
                 version_dates_source="fedlex"),
        ]
        by_year = compute_indicators(build_events(entries, {}), entries)["by_year"]
        assert by_year["2000"]["federal"]["laws_in_force"] == 2
        assert by_year["2020"]["federal"]["laws_in_force"] == 1
