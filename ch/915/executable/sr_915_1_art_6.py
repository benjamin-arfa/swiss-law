"""SR 915.1 Art. 6

Generated from: ch/915/fr/915.1.md

Art. 6: Minimum requirements for advisory centers - financial aid is granted
when activities cover at least one linguistic region. Eligibility condition.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vulg_centrale_couvre_region_linguistique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the advisory center covers at least one linguistic region or the whole country"
    reference = "SR 915.1 Art. 6 al. 1"


class vulg_cooperation_cantons_reglee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether cooperation between advisory centers and cantons is binding"
    reference = "SR 915.1 Art. 6 al. 2"


class vulg_centrale_eligible_aide(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether an advisory center is eligible for financial aid"
    reference = "SR 915.1 Art. 6"

    def formula(person, period, parameters):
        couvre_region = person('vulg_centrale_couvre_region_linguistique', period)
        coop_reglee = person('vulg_cooperation_cantons_reglee', period)
        return couvre_region * coop_reglee
