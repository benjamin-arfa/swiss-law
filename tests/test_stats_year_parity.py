"""The dashboard's year chart and the table under it must agree.

The chart is drawn from stats.json's year x canton x type cube; the table
under it from api/v1/stats/types/<slug>_by_domain.json. They used to be
built with two different year rules, so for intercantonal agreements — the
one type whose tables use sibling-canton evidence — the same selected year
showed two different totals (2001: 75 vs 76, 2002: 91 vs 90, 55 years
apart in total). ``canonical_year_fn`` is now the single rule; these tests
pin that the two artifacts stay in step.
"""
from __future__ import annotations

import yaml

from legalize_ch.stats import (
    CONCORDAT_TYPE,
    canonical_year_fn,
    generate_concordats_by_domain,
    generate_stats,
    generate_types_by_domain,
)

IKV = CONCORDAT_TYPE


def _law(canton="GR", nr="1.1", lang="de", ctype="Gesetz",
         gc="4.10 Schule", enacted="1990-01-01", title="Schulgesetz",
         **extra):
    e = {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
         "language": lang, "_path": f"ch/{canton.lower()}/{lang}/{nr}.md",
         "category_type": ctype, "global_category": gc,
         "enactment_date": enacted, "version_date": "2015-01-01",
         "title": title}
    e.update(extra)
    return e


def _concordat(canton, nr, enacted, title="Konkordat über die Schule", **extra):
    return _law(canton=canton, nr=nr, ctype=IKV, enacted=enacted,
                title=title, **extra)


def _by_year_totals(table: dict) -> dict[str, int]:
    return {y: sum(sum(row.values()) for row in cantons.values())
            for y, cantons in table["by_year"].items()}


class TestCanonicalYearFn:
    def test_concordat_takes_sibling_evidence_plain_law_does_not(self):
        # ZH holds the authoritative 1970 date; GR's own copy is text-parsed
        # and looks like 2002 — the act still existed in 1970.
        zh = _concordat("ZH", "a", "1970-05-01",
                        enactment_date_source="lexwork_api")
        gr = _concordat("GR", "a", "2002-05-01",
                        enactment_date_source="text_parse")
        law = _law(canton="BE", nr="b", enacted="2002-05-01",
                   enactment_date_source="text_parse")
        year_of = canonical_year_fn([zh, gr, law])
        assert year_of(zh)[0] == "1970"
        assert year_of(gr)[0] == "1970"      # sibling evidence applies
        assert year_of(law)[0] == "2002"     # ordinary law: own date only

    def test_returns_year_and_evidence(self):
        law = _law(enacted="1990-01-01")
        year, evidence = canonical_year_fn([law])(law)
        assert year == "1990"
        assert evidence

    def test_undated_law_reports_undated(self):
        law = _law(enacted="", version_date="")
        assert canonical_year_fn([law])(law) == ("", "undated")


class TestArtifactParity:
    """concordats_by_domain.json and types/*.json share one year rule."""

    def test_concordat_table_matches_its_per_type_table(self):
        entries = [
            _concordat("ZH", "a", "1970-05-01",
                       enactment_date_source="lexwork_api"),
            _concordat("GR", "a", "2002-05-01",
                       enactment_date_source="text_parse"),
            _concordat("BE", "b", "1998-01-01", title="Konkordat Steuern",
                       gc="6.10 Steuern"),
            _law(canton="VD", nr="c"),
        ]
        conc = generate_concordats_by_domain(entries)
        ikv = generate_types_by_domain(entries)["files"]["interkantonale_vereinbarung"]
        assert _by_year_totals(conc) == _by_year_totals(ikv)
        assert conc["totals"] == ikv["totals"]

    def test_sibling_evidence_moves_both_tables_together(self):
        entries = [
            _concordat("ZH", "a", "1970-05-01",
                       enactment_date_source="lexwork_api"),
            _concordat("GR", "a", "2002-05-01",
                       enactment_date_source="text_parse"),
        ]
        ikv = generate_types_by_domain(entries)["files"]["interkantonale_vereinbarung"]
        # both copies land in 1970, none in 2002
        assert _by_year_totals(ikv) == {"1970": 2}

    def test_counting_unit_is_declared(self):
        entries = [_concordat("ZH", "a", "1970-05-01")]
        conc = generate_concordats_by_domain(entries)
        ikv = generate_types_by_domain(entries)["files"]["interkantonale_vereinbarung"]
        assert conc["counting_unit"] == "published_copies"
        assert ikv["counting_unit"] == "published_copies"


def _write_repo(tmp_path, entries):
    """Materialize frontmatter dicts as a minimal ch/ tree."""
    for e in entries:
        p = tmp_path / e["_path"]
        p.parent.mkdir(parents=True, exist_ok=True)
        fm = {k: v for k, v in e.items() if not k.startswith("_")}
        p.write_text("---\n" + yaml.safe_dump(fm, allow_unicode=True)
                     + "---\n\nArt. 1 Zweck\n")
    return tmp_path


class TestCubeMatchesTypeTables:
    """THE invariant Mariana's report violated: for every instrument type and
    every year, the chart cube and the per-type table report one total."""

    def _entries(self):
        return [
            # a concordat whose GR copy only has weak, later evidence: the
            # cube used to file it under 2002 and the table under 1970
            _concordat("ZH", "a", "1970-05-01",
                       enactment_date_source="lexwork_api"),
            _concordat("GR", "a", "2002-05-01",
                       enactment_date_source="text_parse"),
            _concordat("BE", "b", "1998-01-01", title="Konkordat Steuern",
                       gc="6.10 Steuern"),
            _law(canton="VD", nr="c", enacted="2001-03-01"),
            _law(canton="TI", nr="d", ctype="Verordnung", enacted="2002-07-01",
                 gc="6.10 Steuern", title="Steuerverordnung"),
        ]

    def test_every_type_and_year_agrees(self, tmp_path):
        entries = self._entries()
        _write_repo(tmp_path, entries)
        stats = generate_stats(tmp_path)
        types = generate_types_by_domain(entries)["files"]

        cube_by_year: dict[str, dict[str, int]] = {}
        for year, cantons in stats["category_type_by_canton_by_year"].items():
            acc = cube_by_year.setdefault(year, {})
            for per_type in cantons.values():
                for t, n in per_type.items():
                    acc[t] = acc.get(t, 0) + n

        labels = {"interkantonale_vereinbarung": IKV, "gesetz": "Gesetz",
                  "verordnung": "Verordnung"}
        for slug, table in types.items():
            label = labels[slug]
            table_years = _by_year_totals(table)
            years = (set(table_years) | set(cube_by_year)) - {"unknown"}
            for y in years:
                assert table_years.get(y, 0) == cube_by_year.get(y, {}).get(label, 0), (
                    f"{slug} {y}: table {table_years.get(y, 0)} != "
                    f"cube {cube_by_year.get(y, {}).get(label, 0)}")

    def test_concordat_year_is_the_sibling_minimum_in_the_cube(self, tmp_path):
        _write_repo(tmp_path, self._entries())
        stats = generate_stats(tmp_path)
        cube = stats["category_type_by_canton_by_year"]
        # GR's copy follows ZH's authoritative 1970 date, not its own 2002 one
        assert cube["1970"]["GR"][IKV] == 1
        assert IKV not in cube.get("2002", {}).get("GR", {})

    def test_category_type_by_year_equals_the_cube(self, tmp_path):
        """The two series in stats.json must not drift either: they are what
        the chart legend and the chart bars are respectively built from."""
        _write_repo(tmp_path, self._entries())
        stats = generate_stats(tmp_path)
        for year, per_type in stats["category_type_by_year"].items():
            rolled: dict[str, int] = {}
            for cantons in [stats["category_type_by_canton_by_year"][year]]:
                for types in cantons.values():
                    for t, n in types.items():
                        rolled[t] = rolled.get(t, 0) + n
            assert per_type == rolled, f"{year}: {per_type} != {rolled}"

    def test_inferred_type_is_not_dropped_from_the_yearly_breakdown(self, tmp_path):
        """A law LexFind leaves untyped but the rules classify belongs in both
        series — it used to be counted in the cube and dropped from
        category_type_by_year."""
        entries = [_law(canton="VD", nr="c", ctype="",
                        title="Konkordat über die Fischerei",
                        category_type_inferred=IKV,
                        type_inference_rule="konkordat")]
        _write_repo(tmp_path, entries)
        stats = generate_stats(tmp_path)
        assert stats["category_type_by_year"]["1990"][IKV] == 1
        assert stats["category_type_by_canton_by_year"]["1990"]["VD"][IKV] == 1
