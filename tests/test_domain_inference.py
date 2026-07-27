"""Tests for domain inference (title keywords + canton systematics)."""
from __future__ import annotations

import json

from legalize_ch.domain_inference import (
    build_canton_topcode_map,
    classify_title,
    enrich_domains,
    infer_domain,
)


class TestClassifyTitle:
    def test_multilingual(self):
        assert classify_title("Schulgesetz") == "4"
        assert classify_title("Loi sur les impôts") == "6"
        assert classify_title("Concordato sulla pesca") == "9"
        assert classify_title("Interkantonale Vereinbarung über die Spitalplanung") == "8"
        assert classify_title("Convention sur la police du lac") == "5"

    def test_specific_beats_general(self):
        # "Steuer" (6) must win over the generic "Gemeinde" (1)
        assert classify_title("Gemeindesteuergesetz") == "6"

    def test_unknown(self):
        assert classify_title("Lorem ipsum") is None


class TestCantonTopcodeMap:
    def test_maps_by_node_title(self, tmp_path):
        tree = [
            {"identifier": "4", "title": "Schulwesen", "children": []},
            {"identifier": "9", "title": "Volkswirtschaft", "children": []},
            {"identifier": "X", "title": "Diverses", "children": []},  # unmappable
        ]
        (tmp_path / "gr.json").write_text(json.dumps(tree))
        m = build_canton_topcode_map(tmp_path, "gr")
        assert m["4"] == "4" and m["9"] == "9"
        assert "X" not in m

    def test_children_majority_vote(self, tmp_path):
        tree = [{"identifier": "C", "title": "C", "children": [
            {"title": "Ecoles primaires"}, {"title": "Université"},
            {"title": "Divers"}]}]
        (tmp_path / "ge.json").write_text(json.dumps(tree))
        assert build_canton_topcode_map(tmp_path, "ge")["C"] == "4"


class TestInferDomain:
    def test_systematics_beats_title(self):
        fm = {"systematic_number": "413.11", "title": "Loi sur les impôts"}
        assert infer_domain(fm, {"4": "4"}) == ("4", "canton_systematics")

    def test_title_fallback(self):
        fm = {"systematic_number": "999.1", "title": "Spitalvereinbarung"}
        assert infer_domain(fm, {}) == ("8", "title_keywords")

    def test_unknown(self):
        assert infer_domain({"systematic_number": "1", "title": "xyz"}, {}) is None


class TestEnrichDomains:
    def test_writes_inferred_field_only(self, tmp_path):
        trees = tmp_path / "docs" / "trees"
        trees.mkdir(parents=True)
        (trees / "global.json").write_text(json.dumps(
            [{"identifier": "8", "title": "Gesundheit"}]))
        (trees / "gr.json").write_text(json.dumps([]))
        law = tmp_path / "ch" / "gr" / "de" / "800.1.md"
        law.parent.mkdir(parents=True)
        law.write_text("---\ncanton: GR\nsystematic_number: '800.1'\n"
                       "title: Spitalgesetz\nlanguage: de\n---\n\n# T\n")
        stats = enrich_domains(tmp_path, cantons=["gr"])
        assert stats["title_keywords"] == 1
        s = law.read_text()
        assert "global_category_inferred: 8 Gesundheit" in s
        assert "inference_source: title_keywords" in s
        assert "global_category:" not in s.replace("global_category_inferred", "")

    def test_lexfind_value_untouched(self, tmp_path):
        trees = tmp_path / "docs" / "trees"
        trees.mkdir(parents=True)
        (trees / "global.json").write_text("[]")
        (trees / "gr.json").write_text("[]")
        law = tmp_path / "ch" / "gr" / "de" / "800.1.md"
        law.parent.mkdir(parents=True)
        law.write_text("---\ncanton: GR\nsystematic_number: '800.1'\n"
                       "title: Spitalgesetz\nglobal_category: 8.10 Spital\n---\n\n# T\n")
        stats = enrich_domains(tmp_path, cantons=["gr"])
        assert stats["already_classified"] == 1
        assert "global_category_inferred" not in law.read_text()


from legalize_ch.domain_inference import classify_type


class TestClassifyType:
    def test_parliamentary_decrees(self):
        assert classify_type("Kantonsratsbeschluss über X")[0] == "Verordnung des Parlaments (Dekret)"
        assert classify_type("Arrêté du Grand Conseil concernant Y")[0] == "Verordnung des Parlaments (Dekret)"
        assert classify_type("Décret sur les communes")[0] == "Verordnung des Parlaments (Dekret)"

    def test_executive_acts(self):
        assert classify_type("Regierungsratsbeschluss betreffend Z")[0] == "Verordnung"
        assert classify_type("Arrêté concernant les taxes")[0] == "Verordnung"
        assert classify_type("Ausführungsbestimmungen zum Gesetz")[0] == "Verordnung"

    def test_misfiled_basics(self):
        assert classify_type("Reglement über die Prüfungen")[0] == "Reglement"
        assert classify_type("Gesetz über das Bergwesen")[0] == "Gesetz"
        assert classify_type("Konkordat über die Fischerei")[0] == "Interkantonale Vereinbarung"

    def test_vereinbarung_needs_marker(self):
        assert classify_type("Vereinbarung zwischen den Kantonen X und Y")[0] == "Interkantonale Vereinbarung"
        assert classify_type("Vereinbarung über die Nutzung des Saals") is None

    def test_leave_other_honored(self):
        for t in ("Richtlinien für X", "Weisungen über Y", "Verfügung betreffend Z",
                  "Gebührentarif der Gerichte"):
            assert classify_type(t) is None


class TestEnrichTypes:
    def test_writes_inferred_only_for_other(self, tmp_path):
        from legalize_ch.domain_inference import enrich_types
        root = tmp_path / "ch" / "gr" / "de"
        root.mkdir(parents=True)
        other = root / "1.md"
        other.write_text("---\ncanton: GR\nsystematic_number: '1'\n"
                         "title: Kantonsratsbeschluss über X\ncategory_type: Anderes\n---\n\n# T\n")
        typed = root / "2.md"
        typed.write_text("---\ncanton: GR\nsystematic_number: '2'\n"
                         "title: Kantonsratsbeschluss über Y\ncategory_type: Gesetz\n---\n\n# T\n")
        stats = enrich_types(tmp_path, cantons=["gr"])
        assert stats["inferred"] == 1 and stats["typed_by_lexfind"] == 1
        s = other.read_text()
        assert "category_type_inferred: Verordnung des Parlaments (Dekret)" in s
        assert "type_inference_rule: parl_beschluss" in s
        assert "category_type: Anderes" in s  # source untouched
        assert "category_type_inferred" not in typed.read_text()
