"""SR 721.80 Art. 50

Generated from: ch/721/de/721.80.md

Art. 50 - Wasserzins reductions during and after construction:
1. No Wasserzins shall be levied during the approved construction period.
2. During the first 6 years after the construction deadline, the concessionaire
   may request a reduction proportional to actual vs. conceded capacity,
   but at most to half.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wrg_in_baufrist(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plant is still within the approved construction period"
    reference = "SR 721.80 Art. 50 Abs. 1"


class wrg_jahre_nach_baufrist(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years elapsed since end of construction deadline"
    reference = "SR 721.80 Art. 50 Abs. 2"


class wrg_auslastungsgrad(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Ratio of actually used capacity to conceded capacity (0-1)"
    reference = "SR 721.80 Art. 50 Abs. 2"
    default_value = 1.0


class wrg_wasserzins_ermaessigung_faktor(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reduction factor applied to Wasserzins (0 = fully exempt, 1 = full rate)"
    reference = "SR 721.80 Art. 50"

    def formula(person, period, parameters):
        in_baufrist = person('wrg_in_baufrist', period)
        jahre = person('wrg_jahre_nach_baufrist', period)
        auslastung = person('wrg_auslastungsgrad', period)
        p = parameters(period).sr_721_80

        ermaessigung_jahre = p.wasserzins_baufrist_ermaessigung_jahre
        min_faktor = p.wasserzins_baufrist_ermaessigung_faktor

        # During construction: no Wasserzins
        # First 6 years after: may reduce to proportion of actual/conceded, min 50%
        # After 6 years: full rate
        in_ermaessigung = (jahre > 0) * (jahre <= ermaessigung_jahre)
        ermaessigter_faktor = max_(auslastung, min_faktor)

        return where(in_baufrist, 0,
                     where(in_ermaessigung, ermaessigter_faktor, 1))
