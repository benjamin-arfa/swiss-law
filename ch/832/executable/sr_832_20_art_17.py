"""SR 832.20 Art. 17

Generated from: ch/832/de/832.20.md

Art. 17: Hoehe (Daily allowance amount)
- Abs. 1: The daily allowance is 80% of the insured income at full incapacity.
  For partial incapacity, it is reduced proportionally.
- Abs. 2: For unemployed persons, the daily allowance corresponds to the
  net unemployment benefit per Art. 22/22a AVIG, converted to calendar days.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class uvg_versicherter_verdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Versicherter Verdienst UVG (letzter Lohn vor Unfall, jaehrlich CHF)"
    reference = "SR 832.20 Art. 15"


class uvg_arbeitsunfaehigkeit_grad(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Arbeitsunfaehigkeit in Prozent (0-100)"
    reference = "SR 832.20 Art. 16 Abs. 1"


class uvg_taggeld_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoehe des UVG-Taggeldes (CHF pro Tag)"
    reference = "SR 832.20 Art. 17 Abs. 1"

    def formula(person, period, parameters):
        verdienst = person('uvg_versicherter_verdienst', period.this_year)
        grad = person('uvg_arbeitsunfaehigkeit_grad', period)
        satz = parameters(period).uvg.taggeld_satz

        # Daily rate = annual insured income / 365 * rate * incapacity fraction
        taggeld = verdienst / 365 * satz * (grad / 100)
        return taggeld
