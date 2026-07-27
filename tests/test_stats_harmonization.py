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
            assert set(labels) == {"de", "fr", "it"}


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
