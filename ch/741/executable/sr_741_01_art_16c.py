"""SR 741.01 Art. 16c - Schwere Widerhandlung

Generated from: ch/de/741/741.01.md

Severe traffic violation withdrawal durations:
a) min 3 months (first offense)
abis) min 2 years (vorsaetzlich elementar, Art. 90 Abs. 4)
b) min 6 months (1 prior medium in 5 years)
c) min 12 months (1 prior severe or 2 prior medium in 5 years)
d) indefinite, min 2 years (2 prior severe or 3 prior medium+ in 10 years)
e) permanent (prior d or 16b.2.e in 5 years)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwere_widerhandlung_svg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine schwere Widerhandlung nach Art. 16c SVG vorliegt"
    reference = "SR 741.01 Art. 16c Abs. 1"


class schwere_widerhandlung_art90_abs4(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine besonders krasse Geschwindigkeitsueberschreitung (Art. 90 Abs. 4) vorliegt"
    reference = "SR 741.01 Art. 16c Abs. 2 Bst. abis"


class anzahl_vorentzuege_mittelschwer_5_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Vorentzuege wegen mittelschwerer Widerhandlung in 5 Jahren"
    reference = "SR 741.01 Art. 16c Abs. 2"


class anzahl_vorentzuege_schwer_5_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Vorentzuege wegen schwerer Widerhandlung in 5 Jahren"
    reference = "SR 741.01 Art. 16c Abs. 2"


class anzahl_vorentzuege_schwer_10_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Vorentzuege wegen schwerer Widerhandlung in 10 Jahren"
    reference = "SR 741.01 Art. 16c Abs. 2 Bst. d"


class anzahl_vorentzuege_mittelschwer_plus_10_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Vorentzuege wegen mindestens mittelschwerer Widerhandlung in 10 Jahren"
    reference = "SR 741.01 Art. 16c Abs. 2 Bst. d"


class schwere_widerhandlung_entzugsdauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestentzugsdauer bei schwerer Widerhandlung in Monaten"
    reference = "SR 741.01 Art. 16c Abs. 2"

    def formula(person, period, parameters):
        schwer = person('schwere_widerhandlung_svg', period)
        art90_4 = person('schwere_widerhandlung_art90_abs4', period)
        vor_ms_5j = person('anzahl_vorentzuege_mittelschwer_5_jahre', period)
        vor_s_5j = person('anzahl_vorentzuege_schwer_5_jahre', period)
        vor_s_10j = person('anzahl_vorentzuege_schwer_10_jahre', period)
        vor_ms_10j = person('anzahl_vorentzuege_mittelschwer_plus_10_jahre', period)

        # Cascading from most to least severe
        # d) indefinite min 24 months
        # c) min 12 months
        # b) min 6 months
        # abis) min 24 months (Art. 90 Abs. 4)
        # a) min 3 months
        dauer = (
            where((vor_s_10j >= 2) + (vor_ms_10j >= 3), 24,
            where((vor_s_5j >= 1) + (vor_ms_5j >= 2), 12,
            where(vor_ms_5j >= 1, 6,
            where(art90_4, 24,
            3))))
        )
        return schwer * dauer
