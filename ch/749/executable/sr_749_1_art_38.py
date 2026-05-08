"""SR 749.1 Art. 38

Generated from: ch/749/fr/749.1.md

Art. 38: Criminal penalties for plan approval violations:
- al. 1: Intentional construction without plan approval or non-compliance:
  up to 3 years imprisonment or monetary penalty.
- al. 2: Negligent violation: monetary penalty.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltsm_infraction_approbation_intentionnelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether intentional plan approval violation occurred"
    reference = "SR 749.1 Art. 38 al. 1"


class ltsm_infraction_approbation_negligence(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether negligent plan approval violation occurred"
    reference = "SR 749.1 Art. 38 al. 2"


class ltsm_peine_privative_liberte_max_ans(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximum imprisonment for intentional plan approval violation (years)"
    reference = "SR 749.1 Art. 38 al. 1"

    def formula(person, period, parameters):
        intentionnelle = person('ltsm_infraction_approbation_intentionnelle', period)
        return intentionnelle * parameters(period).sr_749_1.peine_max_emprisonnement_ans
