"""Tests for category harmonization (canonical keys across languages)."""
from __future__ import annotations

from legalize_ch.categories import (
    CATEGORY_TYPE_LABELS,
    CATEGORY_TYPES,
    canonical_category_type,
    canonical_global_category,
    canonical_systematic_category,
)


class TestCanonicalCategoryType:
    def test_french_maps_to_german(self):
        assert canonical_category_type("Loi") == "Gesetz"
        assert canonical_category_type("Ordonnance") == "Verordnung"
        assert canonical_category_type("Accord intercantonal") == "Interkantonale Vereinbarung"
        assert canonical_category_type("Autre") == "Anderes"

    def test_italian_maps_to_german(self):
        assert canonical_category_type("Legge") == "Gesetz"
        assert canonical_category_type("Accordo intercantonale") == "Interkantonale Vereinbarung"
        assert canonical_category_type("Costituzione") == "Verfassung"

    def test_german_is_identity(self):
        assert canonical_category_type("Gesetz") == "Gesetz"

    def test_unknown_passes_through(self):
        assert canonical_category_type("Mystery Type") == "Mystery Type"

    def test_labels_cover_all_types(self):
        assert len(CATEGORY_TYPE_LABELS) == len(CATEGORY_TYPES) == 9
        for labels in CATEGORY_TYPE_LABELS.values():
            assert set(labels) == {"de", "fr", "it", "en"}


class TestCanonicalGlobalCategory:
    TITLES = {"7.70.50": "Naturschutz", "6.10.30": "Staatsbeiträge, Subventionen"}

    def test_language_variants_merge_by_code(self):
        for v in ("7.70.50 Naturschutz", "7.70.50 Protection de la nature",
                  "7.70.50 Protezione della natura"):
            assert canonical_global_category(v, self.TITLES) == "7.70.50 Naturschutz"

    def test_unknown_code_keeps_raw_value(self):
        assert canonical_global_category("9.99 Unbekannt", self.TITLES) == "9.99 Unbekannt"


class TestCanonicalSystematicCategory:
    TITLES = {"419": "Schulgeld · Schulabkommen"}

    def test_canton_prefixed_and_title_normalized(self):
        assert canonical_systematic_category(
            "bs", "419 Ecolage · Accords scolaires", self.TITLES
        ) == "BS 419 Schulgeld · Schulabkommen"

    def test_same_label_different_canton_stays_split(self):
        a = canonical_systematic_category("gr", "217 Universität", {})
        b = canonical_systematic_category("bs", "VIII Universität", {})
        assert a != b and a.startswith("GR ") and b.startswith("BS ")


class TestConcordatInvariance:
    def test_three_names_one_canonical(self):
        names = ["Interkantonale Vereinbarung", "Accord intercantonal",
                 "Accordo intercantonale"]
        assert {canonical_category_type(n) for n in names} == {"Interkantonale Vereinbarung"}


from legalize_ch.categories import federal_fallback_code
from legalize_ch.stats import generate_harmonized_categories


class TestFederalFallbackCode:
    def test_international_law_follows_suffix(self):
        assert federal_fallback_code("0.142.113.672") == "1"
        assert federal_fallback_code("0.946.31") == "9"

    def test_domestic_uses_first_digit(self):
        assert federal_fallback_code("220") == "2"
        assert federal_fallback_code("831.10") == "8"

    def test_unparseable_empty(self):
        assert federal_fallback_code("") == ""
        assert federal_fallback_code("X.1") == ""


class TestGenerateHarmonizedCategories:
    def _entries(self):
        return [
            {"_scope": "federal", "sr_number": "101", "language": "de",
             "_path": "ch/1/de/101.md"},
            {"_scope": "federal", "sr_number": "999.99", "language": "de",
             "_path": "ch/999/de/999.99.md"},  # not in mapping -> fallback 9
            {"_scope": "cantonal", "canton": "GR", "systematic_number": "1.1",
             "language": "de", "_path": "ch/gr/de/1.1.md",
             "global_category": "1.10.10 Verfassung"},
        ]

    def test_tree_counts_and_provenance(self, tmp_path):
        import json
        trees = tmp_path / "docs" / "trees"
        trees.mkdir(parents=True)
        tree = [{"id": 1, "identifier": "1", "title": "Staat", "children": [
                    {"id": 2, "identifier": "1.10", "title": "Grundlagen", "children": [
                        {"id": 3, "identifier": "1.10.10", "title": "Verfassung"}]}]},
                {"id": 9, "identifier": "9", "title": "Wirtschaft"}]
        (trees / "global.json").write_text(json.dumps(tree))
        (tmp_path / "docs").joinpath("federal_global_categories.json").write_text(
            json.dumps({"101": "1.10.10 Verfassung"}))

        result = generate_harmonized_categories(self._entries(), tmp_path)

        top = {n["identifier"]: n for n in result["top_level"]}
        # SR 101 (lexfind-mapped) + GR law both roll up under "1"
        assert top["1"]["total"] == 2
        assert top["1"]["federal"] == 1 and top["1"]["cantonal"] == 1
        # 999.99 fell back to top-level 9
        assert top["9"]["federal"] == 1
        assert result["counts"]["federal_lexfind"] == 1
        assert result["counts"]["federal_fallback"] == 1
        assert result["counts"]["cantonal_classified"] == 1
        # deep node carries both scopes
        node = result["tree"][0]["children"][0]["children"][0]
        assert node["identifier"] == "1.10.10" and node["total"] == 2


class TestGenerateHarmonizedByYear:
    def _setup_repo(self, tmp_path):
        import json
        trees = tmp_path / "docs" / "trees"
        trees.mkdir(parents=True)
        tree = [{"id": 1, "identifier": "1", "title": "Staat", "children": [
                    {"id": 2, "identifier": "1.10", "title": "Grundlagen", "children": [
                        {"id": 3, "identifier": "1.10.10", "title": "Verfassung"}]}]},
                {"id": 9, "identifier": "9", "title": "Wirtschaft"}]
        (trees / "global.json").write_text(json.dumps(tree))
        (tmp_path / "docs").joinpath("federal_global_categories.json").write_text(
            json.dumps({"101": "1.10.10 Verfassung"}))

    def test_year_cube_and_language_dedup(self, tmp_path):
        from legalize_ch.stats import generate_harmonized_by_year
        self._setup_repo(tmp_path)
        entries = [
            {"_scope": "federal", "sr_number": "101", "language": "de",
             "_path": "ch/1/de/101.md", "enactment_date": "1999-06-01"},
            # same cantonal law in two languages — must count once
            {"_scope": "cantonal", "canton": "GR", "systematic_number": "1.1",
             "language": "de", "_path": "ch/gr/de/1.1.md",
             "global_category": "1.10.10 Verfassung",
             "enactment_date": "1999-01-01"},
            {"_scope": "cantonal", "canton": "GR", "systematic_number": "1.1",
             "language": "it", "_path": "ch/gr/it/1.1.md",
             "global_category": "1.10.10 Costituzione",
             "enactment_date": "1999-01-01"},
            # sentinel date → unknown bucket
            {"_scope": "cantonal", "canton": "BE", "systematic_number": "2.2",
             "language": "de", "_path": "ch/be/de/2.2.md",
             "global_category": "9 Wirtschaft",
             "enactment_date": "1000-01-01"},
        ]
        cube = generate_harmonized_by_year(entries, tmp_path)
        assert cube["years"]["1999"]["1"] == [1, 1]
        assert cube["years"]["1999"]["1.10"] == [1, 1]
        assert "1.10.10" not in cube["years"]["1999"]  # depth capped at 2
        assert cube["unknown"]["9"] == [0, 1]
        assert "1000" not in cube["years"]

    def test_totals_match_harmonized_categories(self, tmp_path):
        from legalize_ch.stats import (generate_harmonized_by_year,
                                       generate_harmonized_categories)
        self._setup_repo(tmp_path)
        entries = [
            {"_scope": "federal", "sr_number": "101", "language": "de",
             "_path": "ch/1/de/101.md", "enactment_date": "1999-06-01"},
            {"_scope": "cantonal", "canton": "GR", "systematic_number": "1.1",
             "language": "de", "_path": "ch/gr/de/1.1.md",
             "global_category": "1.10.10 Verfassung"},  # undated
            {"_scope": "federal", "sr_number": "999.99", "language": "de",
             "_path": "ch/999/de/999.99.md", "enactment_date": "2005-01-01"},
        ]
        cube = generate_harmonized_by_year(entries, tmp_path)
        harm = generate_harmonized_categories(entries, tmp_path)
        for n in harm["top_level"]:
            code = n["identifier"]
            fed = sum(codes.get(code, [0, 0])[0] for codes in cube["years"].values())
            fed += cube["unknown"].get(code, [0, 0])[0]
            cant = sum(codes.get(code, [0, 0])[1] for codes in cube["years"].values())
            cant += cube["unknown"].get(code, [0, 0])[1]
            assert (fed, cant) == (n["federal"], n["cantonal"]), code


class TestEnglishLabelsAndBreakdowns:
    def test_types_have_english(self):
        from legalize_ch.categories import CATEGORY_TYPES
        for t in CATEGORY_TYPES:
            assert "en" in t["label"], t

    def test_breakdowns_at_shallow_depth(self, tmp_path):
        import json
        trees = tmp_path / "docs" / "trees"
        trees.mkdir(parents=True)
        tree = [{"id": 1, "identifier": "1", "title": "Staat", "children": [
                    {"id": 2, "identifier": "1.10", "title": "Grundlagen", "children": [
                        {"id": 3, "identifier": "1.10.10", "title": "Verfassung"}]}]}]
        (trees / "global.json").write_text(json.dumps(tree))
        entries = [
            {"_scope": "cantonal", "canton": "GR", "systematic_number": "1.1",
             "language": "de", "_path": "ch/gr/de/1.1.md",
             "global_category": "1.10.10 Verfassung",
             "category_type": "Loi"},  # fr name -> canonical Gesetz
            {"_scope": "cantonal", "canton": "BE", "systematic_number": "2.2",
             "language": "de", "_path": "ch/be/de/2.2.md",
             "global_category": "1.10 Grundlagen",
             "category_type": "Gesetz"},
        ]
        result = generate_harmonized_categories(entries, tmp_path)
        top = result["tree"][0]
        assert top["title"]["en"] == "State, people, authorities"
        assert top["by_canton"] == {"BE": 1, "GR": 1}
        assert top["by_type"] == {"Gesetz": 2}
        assert top["by_canton_type"]["GR"] == {"Gesetz": 1}
        lvl2 = top["children"][0]
        assert lvl2["identifier"] == "1.10"
        assert lvl2["by_canton"] == {"BE": 1, "GR": 1}
        # depth-3 node stays lean
        lvl3 = lvl2["children"][0]
        assert "by_canton" not in lvl3
