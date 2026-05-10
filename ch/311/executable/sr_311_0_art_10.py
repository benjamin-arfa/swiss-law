"""SR 311.0 Art. 10

Generated from: ch/fr/311/311.0.md

Art. 10: Definitions - crimes vs delits
- Abs. 2: Crimes are offences punishable by >3 years imprisonment.
- Abs. 3: Delits are offences punishable by <=3 years imprisonment or monetary penalty.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_maximale_freiheitsstrafe_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Freiheitsstrafe fuer die Straftat in Jahren"
    reference = "SR 311.0 Art. 10"


class stgb_ist_verbrechen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Tat ein Verbrechen ist (Freiheitsstrafe > 3 Jahre)"
    reference = "SR 311.0 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        max_strafe = person('stgb_maximale_freiheitsstrafe_jahre', period)
        return max_strafe > 3


class stgb_ist_vergehen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Tat ein Vergehen ist (Freiheitsstrafe <= 3 Jahre oder Geldstrafe)"
    reference = "SR 311.0 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        max_strafe = person('stgb_maximale_freiheitsstrafe_jahre', period)
        return (max_strafe > 0) * (max_strafe <= 3)
