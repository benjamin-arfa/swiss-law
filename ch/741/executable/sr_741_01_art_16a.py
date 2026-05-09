"""SR 741.01 Art. 16a - Leichte Widerhandlung

Generated from: ch/de/741/741.01.md

Light traffic violation: minor danger + minor fault, or
non-qualified BAC without other violations.
Consequences:
- Warning if no prior withdrawal in 2 years
- Min 1 month withdrawal if prior withdrawal in 2 years
- No measures in particularly light cases
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class leichte_widerhandlung_svg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine leichte Widerhandlung nach Art. 16a SVG vorliegt"
    reference = "SR 741.01 Art. 16a Abs. 1"


class ausweisentzug_in_letzten_2_jahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob in den vorangegangenen zwei Jahren der Ausweis entzogen war"
    reference = "SR 741.01 Art. 16a Abs. 2"


class besonders_leichter_fall(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein besonders leichter Fall vorliegt"
    reference = "SR 741.01 Art. 16a Abs. 4"


class leichte_widerhandlung_entzugsdauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestentzugsdauer bei leichter Widerhandlung in Monaten"
    reference = "SR 741.01 Art. 16a Abs. 2-4"

    def formula(person, period, parameters):
        leicht = person('leichte_widerhandlung_svg', period)
        vorher_entzug = person('ausweisentzug_in_letzten_2_jahren', period)
        besonders_leicht = person('besonders_leichter_fall', period)
        # Besonders leichter Fall: keine Massnahme (0)
        # Kein Vorentzug: Verwarnung (0 Monate Entzug)
        # Mit Vorentzug: mindestens 1 Monat
        entzug = leicht * (1 - besonders_leicht) * vorher_entzug * 1
        return entzug


class leichte_widerhandlung_verwarnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob bei leichter Widerhandlung eine Verwarnung ausgesprochen wird"
    reference = "SR 741.01 Art. 16a Abs. 3"

    def formula(person, period, parameters):
        leicht = person('leichte_widerhandlung_svg', period)
        vorher_entzug = person('ausweisentzug_in_letzten_2_jahren', period)
        besonders_leicht = person('besonders_leichter_fall', period)
        return leicht * (1 - vorher_entzug) * (1 - besonders_leicht)
