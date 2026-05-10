"""SR 741.01 Art. 16b - Mittelschwere Widerhandlung

Generated from: ch/de/741/741.01.md

Medium traffic violation withdrawal durations:
a) min 1 month (first offense)
b) min 4 months (1 prior medium/severe in 2 years)
c) min 9 months (2 prior medium+ in 2 years)
d) min 15 months (2 prior severe in 2 years)
e) indefinite, min 2 years (3 prior medium+ in 10 years)
f) permanent (prior e or 16c.2.d in 5 years)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mittelschwere_widerhandlung_svg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine mittelschwere Widerhandlung nach Art. 16b SVG vorliegt"
    reference = "SR 741.01 Art. 16b Abs. 1"


class anzahl_vorentzuege_mittelschwer_2_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Ausweisentzuege wegen mittelschwerer/schwerer Widerhandlung in 2 Jahren"
    reference = "SR 741.01 Art. 16b Abs. 2"


class anzahl_vorentzuege_schwer_2_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Ausweisentzuege wegen schwerer Widerhandlung in 2 Jahren"
    reference = "SR 741.01 Art. 16b Abs. 2"


class anzahl_vorentzuege_mittelschwer_10_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Ausweisentzuege wegen mittelschwerer+ Widerhandlung in 10 Jahren"
    reference = "SR 741.01 Art. 16b Abs. 2 Bst. e"


class mittelschwere_widerhandlung_entzugsdauer_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestentzugsdauer bei mittelschwerer Widerhandlung in Monaten"
    reference = "SR 741.01 Art. 16b Abs. 2"

    def formula(person, period, parameters):
        mittelschwer = person('mittelschwere_widerhandlung_svg', period)
        vor_ms_2j = person('anzahl_vorentzuege_mittelschwer_2_jahre', period)
        vor_s_2j = person('anzahl_vorentzuege_schwer_2_jahre', period)
        vor_ms_10j = person('anzahl_vorentzuege_mittelschwer_10_jahre', period)

        # Cascading: check from most severe to least severe
        # f) permanent -> encoded as 9999 months
        # e) min 24 months (3+ prior medium+ in 10 years)
        # d) min 15 months (2 prior severe in 2 years)
        # c) min 9 months (2 prior medium+ in 2 years)
        # b) min 4 months (1 prior medium/severe in 2 years)
        # a) min 1 month (first offense)
        dauer = (
            where(vor_ms_10j >= 3, 24,
            where(vor_s_2j >= 2, 15,
            where(vor_ms_2j >= 2, 9,
            where(vor_ms_2j >= 1, 4,
            1))))
        )
        return mittelschwer * dauer
