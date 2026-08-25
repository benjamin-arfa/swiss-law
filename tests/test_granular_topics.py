"""Granular (full-depth) topic cubes and their 4-language label paths.

The granular export exists so the published data can be read at the depth
LexFind actually classifies at, instead of the 7 chstat domains.  Its whole
value rests on reconciling exactly with the domain table it is derived from,
so that is what most of these tests assert.
"""
from __future__ import annotations

import json
from pathlib import Path

from legalize_ch.categories import (
    GLOBAL_TREE_LANGS,
    build_global_path_map,
    generate_categories_api,
)
from legalize_ch.data_exports import _field, generate_csv_exports, topic_label
from legalize_ch.stats import (
    generate_concordats_by_domain,
    generate_concordats_by_domain_signatories,
    generate_types_by_domain,
    write_granular_cubes,
)

TREES = Path(__file__).resolve().parent.parent / "docs" / "trees"


def _law(canton="GR", nr="1.1", lang="de", ctype="Gesetz",
         gc="4.10 Schule", enacted="1990-01-01", title="Schulgesetz"):
    return {"_scope": "cantonal", "canton": canton, "systematic_number": nr,
            "language": lang, "_path": f"ch/{canton.lower()}/{lang}/{nr}.md",
            "category_type": ctype, "global_category": gc,
            "enactment_date": enacted, "version_date": "2015-01-01",
            "title": title}


def _sum_cube(by_year: dict) -> int:
    return sum(n for cantons in by_year.values()
               for row in cantons.values() for n in row.values())


class TestReconciliation:
    """Every (year, canton) granular sum equals the 7-domain sum."""

    ENTRIES = [
        _law(nr="a", gc="1.10.70.10.10 Einwohnerkontrolle", enacted="1994-02-01"),
        _law(nr="b", gc="1.10.70.20 Ausweise", enacted="1994-03-01"),
        _law(nr="c", gc="4 Schulwesen", enacted="2001-01-01"),
        _law(nr="d", gc="", enacted="2001-01-01"),
        _law(canton="BE", nr="e", gc="6.10.10 Steuern", enacted="1994-04-01"),
        _law(canton="BE", nr="f", gc="", enacted=""),  # → version_date 2015
    ]

    def test_per_year_per_canton_sums_match(self):
        granular = {}
        tbl = generate_types_by_domain(
            self.ENTRIES, granular_out=granular)["files"]["gesetz"]
        cube = granular["gesetz_by_topic"]
        assert set(cube["by_year"]) == set(tbl["by_year"])
        for year, cantons in tbl["by_year"].items():
            assert set(cube["by_year"][year]) == set(cantons)
            for canton, doms in cantons.items():
                assert (sum(cube["by_year"][year][canton].values())
                        == sum(doms.values()))

    def test_grand_totals_match(self):
        granular = {}
        tbl = generate_types_by_domain(
            self.ENTRIES, granular_out=granular)["files"]["gesetz"]
        cube = granular["gesetz_by_topic"]
        assert cube["total"] == tbl["totals"]["total"] == len(self.ENTRIES)
        assert _sum_cube(cube["by_year"]) == cube["total"]
        assert sum(cube["totals_by_code"].values()) == cube["total"]

    def test_domain_table_is_untouched(self):
        """The cube ships separately — the page-load JSON must not grow."""
        tbl = generate_types_by_domain(self.ENTRIES)["files"]["gesetz"]
        assert "by_year_granular" not in tbl
        conc = generate_concordats_by_domain(self.ENTRIES)
        assert "by_year_granular" not in conc

    def test_no_cube_written_without_the_out_param(self):
        granular = {}
        generate_types_by_domain(self.ENTRIES)
        assert granular == {}


class TestDepth:
    def test_full_code_survives(self):
        granular = {}
        generate_types_by_domain(
            [_law(gc="1.10.70.10.10 Einwohnerkontrolle", enacted="1994-01-01")],
            granular_out=granular)
        cube = granular["gesetz_by_topic"]
        assert cube["by_year"]["1994"]["GR"] == {"1.10.70.10.10": 1}
        assert cube["codes"] == ["1.10.70.10.10"]

    def test_top_level_only_stays_top_level(self):
        granular = {}
        generate_types_by_domain([_law(gc="4 Schulwesen", enacted="1994-01-01")],
                                 granular_out=granular)
        assert granular["gesetz_by_topic"]["by_year"]["1994"]["GR"] == {"4": 1}

    def test_unclassified_is_uncategorized(self):
        granular = {}
        generate_types_by_domain([_law(gc="", enacted="1994-01-01")],
                                 granular_out=granular)
        assert (granular["gesetz_by_topic"]["by_year"]["1994"]["GR"]
                == {"uncategorized": 1})

    def test_codes_sort_numerically_with_uncategorized_last(self):
        granular = {}
        generate_types_by_domain([
            _law(nr="a", gc="10.10 Publikationen"),
            _law(nr="b", gc="2.10 Zivilrecht"),
            _law(nr="c", gc=""),
            _law(nr="d", gc="2.10.5 Personenrecht"),
        ], granular_out=granular)
        assert granular["gesetz_by_topic"]["codes"] == [
            "2.10", "2.10.5", "10.10", "uncategorized"]


class TestSignatoriesCube:
    """The signatory table counts memberships, not copies — same rule applies."""

    ENTRIES = [
        _law(canton="GR", nr="1.1", ctype="Interkantonale Vereinbarung",
             title="Konkordat über die Schulen", enacted="1970-01-01",
             gc="4.10.20 Volksschule"),
        _law(canton="BE", nr="2.2", ctype="Interkantonale Vereinbarung",
             title="Konkordat über die Schulen", enacted="1970-01-01",
             gc="4.10.20 Volksschule"),
        _law(canton="ZH", nr="3.3", ctype="Interkantonale Vereinbarung",
             title="Vereinbarung Zürich und Bern über Steuern",
             enacted="1980-01-01", gc="6.10 Steuern"),
        _law(canton="BE", nr="4.4", ctype="Interkantonale Vereinbarung",
             title="Vereinbarung Zürich und Bern über Steuern",
             enacted="1980-01-01", gc="6.10 Steuern"),
    ]

    def test_totals_match_the_domain_table(self):
        granular = {}
        sig = generate_concordats_by_domain_signatories(
            self.ENTRIES, granular_out=granular)
        cube = granular["concordats_by_topic_signatories"]
        assert cube["counting_unit"] == "signatory_memberships"
        assert cube["slug"] == ""   # the data page's default selection
        assert cube["total"] == sig["totals"]["total"]
        for year, cantons in sig["by_year"].items():
            for canton, doms in cantons.items():
                assert (sum(cube["by_year"][year][canton].values())
                        == sum(doms.values()))

    def test_codes_are_full_depth(self):
        granular = {}
        generate_concordats_by_domain_signatories(
            self.ENTRIES, granular_out=granular)
        assert set(granular["concordats_by_topic_signatories"]["codes"]) == {
            "4.10.20", "6.10"}


class TestWriteGranularCubes:
    def test_index_resolves_slug_to_file(self, tmp_path):
        granular = {}
        entries = self.ENTRIES = [
            _law(nr="a"),
            _law(nr="b", ctype="Interkantonale Vereinbarung",
                 title="Konkordat A", canton="GR"),
            _law(nr="c", ctype="Interkantonale Vereinbarung",
                 title="Konkordat A", canton="BE"),
        ]
        generate_concordats_by_domain(entries, granular_out=granular)
        generate_concordats_by_domain_signatories(entries, granular_out=granular)
        generate_types_by_domain(entries, granular_out=granular)
        write_granular_cubes(granular, tmp_path)

        index = json.loads((tmp_path / "index.json").read_text())
        assert index["by_slug"][""] == "concordats_by_topic_signatories.json"
        assert index["by_slug"]["gesetz"] == "gesetz_by_topic.json"
        for entry in index["datasets"]:
            assert (tmp_path / entry["file"]).exists()
        # the published-copies concordats cube has no selector slug
        assert None not in index["by_slug"]


def _numeric_identifiers(tree_file: Path) -> set[str]:
    """LexFind's own dotted codes in a tree file (not our sentinels)."""
    def walk(nodes):
        for n in nodes:
            yield n
            yield from walk(n.get("children", []))
    tree = json.loads(tree_file.read_text(encoding="utf-8"))
    return {n["identifier"] for n in walk(tree)
            if str(n["identifier"])[:1].isdigit()}


class TestGlobalPathMap:
    PATHS = build_global_path_map(TREES)

    def test_covers_every_lexfind_node(self):
        assert set(self.PATHS) == _numeric_identifiers(TREES / "global.json")

    def test_the_uncategorized_sentinel_is_not_a_taxonomy_node(self):
        """Some snapshots of global.json carry it, some do not — either way
        the published map must be the same."""
        assert "uncategorized" not in self.PATHS

    def test_every_node_has_all_four_languages(self):
        for code, entry in self.PATHS.items():
            for lang in GLOBAL_TREE_LANGS:
                assert entry["title"][lang], f"{code} has no {lang} title"
                assert entry["path"][lang], f"{code} has no {lang} path"

    def test_no_trailing_whitespace(self):
        for entry in self.PATHS.values():
            for lang in GLOBAL_TREE_LANGS:
                assert entry["title"][lang] == entry["title"][lang].strip()
                assert entry["path"][lang] == entry["path"][lang].strip()

    def test_path_is_the_ancestor_chain(self):
        leaf = self.PATHS["1.10.70.10.10"]
        assert leaf["depth"] == 5
        assert leaf["parent"] == "1.10.70.10"
        assert leaf["path"]["fr"].startswith(self.PATHS["1"]["title"]["fr"] + ".")
        assert leaf["path"]["fr"].endswith("." + leaf["title"]["fr"])
        assert leaf["path"]["fr"].count(".") == 4

    def test_english_titles_are_not_german(self):
        assert self.PATHS["1"]["title"]["en"] == "State"
        assert self.PATHS["1.10.10"]["title"]["en"] == "Constitution"

    def test_top_level_path_is_the_title(self):
        assert self.PATHS["4"]["path"]["de"] == self.PATHS["4"]["title"]["de"]


class TestCategoriesApi:
    def test_global_json_carries_english(self, tmp_path):
        generate_categories_api(TREES, tmp_path)
        data = json.loads((tmp_path / "global.json").read_text())
        assert "machine translation" in data["title_en_source"]
        assert data["tree"][0]["title"]["en"] == "State"

    def test_global_paths_published_and_indexed(self, tmp_path):
        generate_categories_api(TREES, tmp_path)
        paths = json.loads((tmp_path / "global_paths.json").read_text())
        assert paths["total"] == len(build_global_path_map(TREES))
        assert paths["codes"]["1.10.10"]["title"]["en"] == "Constitution"
        index = json.loads((tmp_path / "index.json").read_text())
        assert index["global_paths"] == "api/v1/categories/global_paths.json"

    def test_global_en_is_not_written_as_a_canton(self, tmp_path):
        generate_categories_api(TREES, tmp_path)
        assert not (tmp_path / "GLOBAL_EN.json").exists()
        index = json.loads((tmp_path / "index.json").read_text())
        assert "GLOBAL_EN" not in index["cantons"]


class TestCsvQuoting:
    def test_comma_bearing_label_is_quoted(self):
        assert _field("Santé, travail.Assurances") == '"Santé, travail.Assurances"'

    def test_inner_quotes_are_doubled(self):
        assert _field('a "b", c') == '"a ""b"", c"'

    def test_plain_values_are_untouched(self):
        assert _field("GR") == "GR"
        assert _field(1994) == "1994"
        assert _field("Etat.Grundlagen") == "Etat.Grundlagen"

    def test_already_quoted_fields_are_left_alone(self):
        assert _field('"already, quoted"') == '"already, quoted"'

    def test_round_trips_through_csv(self):
        import csv
        import io
        row = ["GR", "1994", "Santé, travail.Assurances", 3]
        text = ",".join(_field(v) for v in row)
        assert next(csv.reader(io.StringIO(text))) == [str(v) for v in row]


class TestGranularCsvExport:
    def test_rows_carry_label_paths_and_reconcile(self):
        entries = [
            _law(nr="a", gc="1.10.70.10.10 Einwohnerkontrolle", enacted="1994-01-01"),
            _law(nr="b", gc="", enacted="1994-01-01"),
        ]
        granular = {}
        type_tables = generate_types_by_domain(entries, granular_out=granular)
        sig = generate_concordats_by_domain_signatories(entries,
                                                        granular_out=granular)
        paths = build_global_path_map(TREES)
        files = generate_csv_exports(type_tables, sig, granular=granular,
                                     topic_paths=paths)
        csv_text = files["gesetz_canton_year_topic.csv"]
        header, *rows = [line for line in csv_text.splitlines()
                         if not line.startswith("#")]
        assert header == "canton,year,topic,number"
        assert len(rows) == 2
        assert any("contrôle des habitants" in r for r in rows)
        assert any("Non classé" in r for r in rows)
        assert sum(int(r.rsplit(",", 1)[1]) for r in rows) == 2

    def test_registered_in_the_index(self):
        entries = [_law(nr="a", gc="4.10 Schule", enacted="1994-01-01")]
        granular = {}
        type_tables = generate_types_by_domain(entries, granular_out=granular)
        sig = generate_concordats_by_domain_signatories(entries,
                                                        granular_out=granular)
        files = generate_csv_exports(type_tables, sig, granular=granular,
                                     topic_paths=build_global_path_map(TREES))
        index = json.loads(files["index.json"])
        names = {f["file"] for f in index["files"]}
        assert "gesetz_canton_year_topic.csv" in names
        assert "gesetz_canton_year.csv" in names   # unchanged

    def test_existing_exports_are_unchanged_without_granular(self):
        entries = [_law(nr="a", gc="4.10 Schule", enacted="1994-01-01")]
        type_tables = generate_types_by_domain(entries)
        sig = generate_concordats_by_domain_signatories(entries)
        before = generate_csv_exports(type_tables, sig)
        granular = {}
        type_tables = generate_types_by_domain(entries, granular_out=granular)
        sig = generate_concordats_by_domain_signatories(entries,
                                                        granular_out=granular)
        after = generate_csv_exports(type_tables, sig, granular=granular,
                                     topic_paths=build_global_path_map(TREES))
        assert before["gesetz_canton_year.csv"] == after["gesetz_canton_year.csv"]
        assert before["laws_cube.csv"] == after["laws_cube.csv"]


class TestTopicLabel:
    PATHS = build_global_path_map(TREES)

    def test_known_code(self):
        assert topic_label("1.10.10", self.PATHS, "en") == "State.General provisions.Constitution"

    def test_uncategorized(self):
        assert topic_label("uncategorized", self.PATHS) == "Non classé"

    def test_unknown_code_falls_back_to_the_code(self):
        assert topic_label("99.99", self.PATHS) == "99.99"
