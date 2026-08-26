"""Tests for the legal event stream — one record per (law, date)."""
from __future__ import annotations

import pytest
import json

from legalize_ch.events import (
    EVENT_COLUMNS,
    LAW_COLUMNS,
    aggregate_events,
    build_events,
    compute_indicators,
    is_consolidation,
    law_dimension,
    law_key,
    law_prefix,
    law_sizes,
    write_events,
)

CO_SUBJECT = ("SR 220: Bundesgesetz vom 30. März 1911 betreffend die Ergänzung des "
              "Schweizerischen Zivilgesetzbuches (Fünfter Teil: Obligationenrecht) (2025-01-01)")
CANT_SUBJECT = ("BE 811.011: Verordnung über die Rechte und Pflichten der Patientinnen "
                "und Patienten und der Gesundheitsfachpersonen (2023-01-01)")


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
        assert is_consolidation(CO_SUBJECT, "2025-01-01") == "SR"

    def test_cantonal_consolidation_accepted(self):
        """19,547 of these were read as bulk metadata while the pattern only
        knew the federal 'SR' prefix."""
        assert is_consolidation(CANT_SUBJECT, "2023-01-01") == "BE"

    def test_the_prefix_is_the_commit_register(self):
        assert is_consolidation("ZH 412.1: Lehrpersonalverordnung (2019-08-01)",
                                "2019-08-01") == "ZH"

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
        assert not is_consolidation(CANT_SUBJECT, "2026-07-27")


class TestLawPrefix:
    def test_federal_law_is_the_sr_register(self):
        assert law_prefix(_fed()) == "SR"

    def test_cantonal_law_is_its_canton(self):
        assert law_prefix(_cant(canton="BE")) == "BE"

    def test_the_path_is_never_consulted(self):
        """ch/fr/ holds federal French law AND Fribourg law — only the
        frontmatter distinguishes them."""
        assert law_prefix({"_path": "ch/fr/101.md"}) == "SR"
        assert law_prefix({"_path": "ch/fr/de/137.21.md", "canton": "FR"}) == "FR"


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
        cons = {"ch/de/220.md": {"2025-01-01": "SR"}}
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
        cons = {"ch/zh/de/131.1.md": {"2020-02-01": "SR"}}
        assert [e["date"] for e in build_events(entries, cons)] == ["2019-01-01"]

    def test_a_cantonal_consolidation_dates_its_own_canton(self):
        """The same commit shape from the law's own register IS the event —
        this is what the federal-only pattern was throwing away."""
        entries = [_cant(version_date="2019-01-01")]
        cons = {"ch/zh/de/131.1.md": {"2020-02-01": "ZH"}}
        evs = build_events(entries, cons)
        assert [e["date"] for e in evs] == ["2019-01-01", "2020-02-01"]
        assert evs[1]["source"] == "cantonal_consolidation"

    def test_a_cantonal_consolidation_never_dates_another_canton(self):
        entries = [_cant(canton="ZH", version_date="2019-01-01")]
        cons = {"ch/zh/de/131.1.md": {"2020-02-01": "BE"}}
        assert [e["date"] for e in build_events(entries, cons)] == ["2019-01-01"]

    def test_language_versions_of_one_consolidation_are_one_event(self):
        entries = [_fed(lang=lang, version_date="2025-01-01") for lang in ("de", "fr", "it")]
        cons = {f"ch/{lang}/220.md": {"2025-01-01": "SR"} for lang in ("de", "fr", "it")}
        assert len(build_events(entries, cons)) == 1

    def test_publication_is_the_earliest_date(self):
        entries = [_fed(enactment_date="1911-03-30", enactment_date_source="text",
                        version_date="2025-01-01")]
        evs = build_events(entries, {"ch/de/220.md": {"2024-01-01": "SR"}})
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
        cons = {f"ch/{lang}/220.md": {"2024-01-01": "SR", "2025-01-01": "SR"}
                for lang in ("de", "fr")}
        deltas = {
            "ch/de/220.md": {
                "2024-01-01": {"lines_added": 9000, "lines_removed": 0, "prefix": "SR"},
                "2025-01-01": {"lines_added": 1908, "lines_removed": 96, "prefix": "SR"}},
            "ch/fr/220.md": {
                "2024-01-01": {"lines_added": 8800, "lines_removed": 0, "prefix": "SR"},
                "2025-01-01": {"lines_added": 1850, "lines_removed": 90, "prefix": "SR"}},
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
            "2022-01-01": {"lines_added": 3000, "lines_removed": 0, "prefix": "SR"},
            "2025-01-01": {"lines_added": 12, "lines_removed": 4, "prefix": "SR"},
        }}
        evs = build_events(entries, {}, deltas)
        assert [("delta" in e) for e in evs] == [False, False, True]
        assert evs[2]["delta"] == {"lines_added": 12, "lines_removed": 4}

    def test_a_delta_from_another_register_is_not_this_law_s_magnitude(self):
        """A ride-along file touched by a federal batch keeps its own count."""
        entries = [_cant(version_dates=["2019-01-01", "2022-01-01", "2025-01-01"],
                         version_dates_source="lexfind_family")]
        deltas = {"ch/zh/de/131.1.md": {
            "2022-01-01": {"lines_added": 300, "lines_removed": 0, "prefix": "ZH"},
            "2025-01-01": {"lines_added": 40, "lines_removed": 9, "prefix": "SR"},
        }}
        evs = build_events(entries, {}, deltas)
        assert [("delta" in e) for e in evs] == [False, False, False]

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
        cube = aggregate_events(build_events(entries, {}), {"commits_scanned": 7},
                                law_sizes(entries))
        assert cube["totals"] == {"events": 3, "publications": 2, "revisions": 1,
                                  "laws_with_events": 2}
        assert cube["by_year"]["2025"]["federal"]["revision"] == 1
        assert cube["by_year"]["2025"]["cantonal"]["publication"] == 1
        assert cube["provenance"]["commits_scanned"] == 7

    def test_articles_cover_cantonal_law_where_lines_cannot(self):
        """The magnitude the markdown supports without a version history."""
        entries = [
            _fed(version_dates=["2024-01-01", "2025-01-01"], version_dates_source="fedlex"),
            _cant(version_dates=["2025-06-01"], version_dates_source="lexfind_family"),
        ]
        cube = aggregate_events(build_events(entries, {}), {}, law_sizes(entries))
        fed25 = cube["by_year"]["2025"]["federal"]
        can25 = cube["by_year"]["2025"]["cantonal"]
        assert fed25["articles_revision"] == 12       # the federal law's 12 articles
        assert can25["articles_publication"] == 4     # the cantonal law's 4
        assert can25["lines"] == 0                    # nothing to diff against

    def test_articles_are_zero_without_the_size_map(self):
        """The page must not offer a measure the cube was not built with."""
        entries = [_cant(version_date="2025-06-01")]
        cube = aggregate_events(build_events(entries, {}), {})
        assert cube["by_year"]["2025"]["cantonal"]["articles_publication"] == 0


class TestLawSizes:
    def test_language_versions_are_one_law_not_three(self):
        entries = [_fed(lang=lang, version_date="2025-01-01") for lang in ("de", "fr", "it")]
        assert law_sizes(entries) == {"federal/220": {"chars": 1000, "articles": 12}}

    def test_every_law_in_the_corpus_has_a_size(self):
        entries = [_fed(), _cant(), _cant(canton="BE", num="101")]
        sizes = law_sizes(entries)
        assert set(sizes) == {"federal/220", "ZH/131.1", "BE/101"}
        assert all(v["articles"] > 0 for v in sizes.values())


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

    def test_articles_in_revised_laws_is_reported_for_both_scopes(self):
        entries = [
            _fed(sr="1", version_dates=["2020-01-01", "2024-01-01"],
                 version_dates_source="fedlex"),
            _cant(version_dates=["2020-01-01", "2024-01-01"],
                  version_dates_source="lexfind_family"),
        ]
        evs = build_events(entries, {})
        by_year = compute_indicators(evs, entries, law_sizes(entries))["by_year"]["2024"]
        assert by_year["federal"]["articles_in_revised_laws"] == 12
        assert by_year["cantonal"]["articles_in_revised_laws"] == 4
        assert by_year["all"]["articles_in_revised_laws"] == 16
        # articles / laws in force — the cantonal cell is a number, not a gap
        assert by_year["cantonal"]["article_churn"] == 4.0

    def test_magnitude_coverage_is_counted_not_asserted(self):
        """The share decides whether the page may offer the lines measure, so it
        is measured on every rebuild rather than written into a note."""
        entries = [
            _fed(sr="1", version_dates=["2020-01-01", "2024-01-01", "2025-01-01"],
                 version_dates_source="fedlex"),
            _cant(version_dates=["2020-01-01", "2024-01-01"],
                  version_dates_source="lexfind_family"),
        ]
        deltas = {"ch/de/1.md": {
            "2024-01-01": {"lines_added": 100, "lines_removed": 0, "prefix": "SR"},
            "2025-01-01": {"lines_added": 12, "lines_removed": 4, "prefix": "SR"},
        }}
        cov = compute_indicators(build_events(entries, {}, deltas), entries)["coverage"]
        m = cov["lines_changed_measured"]
        # the federal law's first delta is the import and carries no magnitude
        assert m["federal"] == {"revisions": 2, "revisions_with_delta": 1, "share": 0.5}
        assert m["cantonal"] == {"revisions": 1, "revisions_with_delta": 0, "share": 0.0}


def _decode(out_dir):
    """Read the published form back into build_events() records.

    The encoding is only worth its saving if it is lossless, so the tests
    decode it the way a consumer would — positionally, through the codebooks
    and the join — rather than inspecting the rows they just wrote.
    """
    laws = json.loads((out_dir / "laws.json").read_text())
    lbook, lcols = laws["codebooks"], laws["columns"]
    by_law = {}
    for row in laws["rows"]:
        r = dict(zip(lcols, row))
        attrs = {}
        for field in ("scope", "canton", "domain", "type"):
            if r[field] is not None:
                attrs[field] = lbook[field][r[field]]
        by_law[r["law"]] = (attrs, r)

    index = json.loads((out_dir / "index.json").read_text())
    events = []
    for year in index["years"]:
        y = json.loads((out_dir / f"{year}.json").read_text())
        for row in y["rows"]:
            r = dict(zip(y["columns"], row))          # short rows: rest absent
            rec = {"date": r["date"], "law": r["law"],
                   "event": y["codebooks"]["event"][r["event"]],
                   "seq": r["seq"],
                   "source": y["codebooks"]["source"][r["source"]]}
            if r.get("delta"):
                rec["delta"] = {"lines_added": r["delta"][0],
                                "lines_removed": r["delta"][1]}
            attrs, law = by_law[r["law"]]
            rec.update(attrs)
            # the size is the law's, credited to the event that produced it
            if law["chars"] is not None and r["date"] == law["latest"]:
                rec["size_current"] = {"chars": law["chars"],
                                       "articles": law["articles"]}
            events.append(rec)
    return events


class TestWriteEvents:
    def _events(self):
        entries = [
            _fed(sr="220", version_dates=["2020-01-01", "2024-01-01", "2025-01-01"],
                 version_dates_source="fedlex", global_category="2 Privatrecht",
                 category_type="Gesetz"),
            _cant(version_dates=["2020-05-01"], version_dates_source="lexfind_family",
                  global_category="1 Staat", category_type="Verfassung"),
        ]
        deltas = {"ch/de/220.md": {
            "2024-01-01": {"lines_added": 10, "lines_removed": 2, "prefix": "SR"},
            "2025-01-01": {"lines_added": 7, "lines_removed": 1, "prefix": "SR"},
        }}
        return build_events(entries, {}, deltas)

    def test_roundtrip_is_lossless(self, tmp_path):
        """The split into laws.json + year rows drops no field and no record."""
        evs = self._events()
        write_events(evs, tmp_path)
        key = lambda r: (r["date"], r["law"])  # noqa: E731
        assert sorted(_decode(tmp_path), key=key) == sorted(evs, key=key)

    def test_law_constants_are_written_once(self, tmp_path):
        """The whole saving: a law's scope/canton/domain/type/size live in the
        law table, not on each of its events."""
        write_events(self._events(), tmp_path)
        year = json.loads((tmp_path / "2025.json").read_text())
        assert year["columns"] == list(EVENT_COLUMNS)
        assert not {"scope", "canton", "domain", "type", "size_current"} & set(year)
        for row in year["rows"]:
            assert len(row) <= len(EVENT_COLUMNS)
        laws = json.loads((tmp_path / "laws.json").read_text())
        assert laws["columns"] == list(LAW_COLUMNS)
        assert laws["count"] == 2 == len(laws["rows"])

    def test_latest_marks_the_law_s_current_version(self, tmp_path):
        """The denormalised form said this by hanging size_current on one event;
        dropped, a consumer could not tell which text is the law's today."""
        write_events(self._events(), tmp_path)
        rows = {r[0]: r for r in json.loads((tmp_path / "laws.json").read_text())["rows"]}
        latest = LAW_COLUMNS.index("latest")
        assert rows["federal/220"][latest] == "2025-01-01"
        assert rows["ZH/131.1"][latest] == "2020-05-01"
        assert rows["federal/220"][LAW_COLUMNS.index("chars")] == 1000

    def test_absent_delta_is_omitted_not_nulled(self, tmp_path):
        """Short rows are the encoding's second saving; a null in the slot
        would cost half a megabyte across the real stream to say nothing."""
        write_events(self._events(), tmp_path)
        rows = json.loads((tmp_path / "2020.json").read_text())["rows"]
        assert all(len(r) == len(EVENT_COLUMNS) - 1 for r in rows)  # no deltas in 2020
        rows_2025 = json.loads((tmp_path / "2025.json").read_text())["rows"]
        assert [len(r) for r in rows_2025] == [len(EVENT_COLUMNS)]  # delta present

    def test_index_reports_laws_and_how_to_decode(self, tmp_path):
        index = write_events(self._events(), tmp_path)
        assert index["total_events"] == 4
        assert index["total_laws"] == 2
        assert index["format"] == "columnar"
        assert "laws.json" in index["decoding"]
        assert json.loads((tmp_path / "2025.json").read_text())["laws"] == "laws.json"

    def test_unknown_field_refuses_rather_than_drops(self, tmp_path):
        """A field added to build_events() but not to a column list would
        vanish silently — the encoder is lossless only if it says so."""
        evs = self._events()
        evs[0]["confidence"] = "reconstructed"
        with pytest.raises(ValueError, match="confidence"):
            write_events(evs, tmp_path)

    def test_codebooks_cover_every_value_used(self, tmp_path):
        write_events(self._events(), tmp_path)
        laws = json.loads((tmp_path / "laws.json").read_text())
        assert laws["codebooks"]["scope"] == ["cantonal", "federal"]
        assert laws["codebooks"]["canton"] == ["ZH"]
        federal = next(r for r in laws["rows"] if r[0].startswith("federal/"))
        assert federal[LAW_COLUMNS.index("canton")] is None

    def test_law_dimension_collapses_repeats(self):
        """4.1 events per law on the real corpus, one row each here."""
        dim = law_dimension(self._events())
        assert dim["count"] == 2
        assert [r[0] for r in dim["rows"]] == sorted(r[0] for r in dim["rows"])
