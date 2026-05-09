"""SR 641.811 Art. 14 - Tarif fuer leistungsabhaengige Abgabe

Distance-based tax rate per km per tonne of relevant weight:
a. Category 1: 3.26 Rappen (CHF 0.0326)
b. Category 2: 2.82 Rappen (CHF 0.0282)
c. Category 3: 2.39 Rappen (CHF 0.0239)

Category assignment per Annex 1. Default is category 1 if proof
of category 2 or 3 cannot be provided.

Generated from: ch/641/de/641.811.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class svav_abgabekategorie(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Abgabekategorie 1-3 nach Anhang 1 (Art. 14 Abs. 2 SVAV)"
    reference = "SR 641.811 Art. 14 Abs. 2"
    default_value = 1


class svav_gefahrene_km(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gefahrene Kilometer im Inland (Art. 14 SVAV)"
    reference = "SR 641.811 Art. 14"


class svav_tarif_rappen_pro_km_tonne(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Abgabetarif in Rappen pro km und Tonne (Art. 14 Abs. 1 SVAV)"
    reference = "SR 641.811 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        kategorie = person('svav_abgabekategorie', period)
        # a. Category 1: 3.26 Rp, b. Category 2: 2.82 Rp, c. Category 3: 2.39 Rp
        return (
            (kategorie == 1) * 3.26 +
            (kategorie == 2) * 2.82 +
            (kategorie == 3) * 2.39
        )


class svav_leistungsabhaengige_abgabe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Leistungsabhaengige Schwerverkehrsabgabe in CHF (Art. 14 SVAV)"
    reference = "SR 641.811 Art. 14"

    def formula(person, period, parameters):
        km = person('svav_gefahrene_km', period)
        gewicht_t = person('svav_massgebendes_gewicht_kg', period.this_year) / 1000
        tarif_rp = person('svav_tarif_rappen_pro_km_tonne', period.this_year)
        # Convert Rappen to CHF (divide by 100)
        return km * gewicht_t * tarif_rp / 100
