"""SR 837.0 Art. 24

Generated from: ch/837/de/837.0.md

Art. 24: Anrechnung von Zwischenverdienst (Interim earnings credit)
- Abs. 1: Any income from employment (employed or self-employed) earned
  during a control period is interim earnings. The insured person is entitled
  to compensation for the loss of earnings, with the rate per Art. 22.
- Abs. 3: The loss of earnings is the difference between the interim earnings
  (at least the customary local/professional rate) and the insured income.
- Abs. 4: Compensation for loss of earnings lasts at most 12 months; for
  persons with child support obligations (children under 25) or persons
  over 45, until end of framework period.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class alv_zwischenverdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Zwischenverdienst in der Kontrollperiode (CHF)"
    reference = "SR 837.0 Art. 24 Abs. 1"


class alv_verdienstausfall_zwischenverdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Verdienstausfall bei Zwischenverdienst (CHF)"
    reference = "SR 837.0 Art. 24 Abs. 3"

    def formula(person, period, parameters):
        verdienst = person('alv_versicherter_verdienst', period.this_year)
        zwischenverdienst = person('alv_zwischenverdienst', period)

        # Monthly insured income approximation
        monatlicher_verdienst = verdienst / 12

        # Loss = insured income - interim earnings (floored at 0)
        ausfall = monatlicher_verdienst - zwischenverdienst
        return max_(ausfall, 0)


class alv_kompensation_zwischenverdienst(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Kompensationszahlung bei Zwischenverdienst (CHF)"
    reference = "SR 837.0 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        ausfall = person('alv_verdienstausfall_zwischenverdienst', period)
        satz = person('alv_taggeld_satz', period)
        return ausfall * satz
