"""SR 915.1 Art. 7

Generated from: ch/915/fr/915.1.md

Art. 7: Minimum requirements for organizational advisory services.
Financial aid granted when: (a) covers at least one linguistic region,
(b) works in specific domains not covered by cantonal services,
(c) works in agreement with advisory centers and cantonal services.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vulg_org_couvre_region_linguistique(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the organizational advisory service covers at least one linguistic region"
    reference = "SR 915.1 Art. 7 let. a"


class vulg_org_domaine_particulier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the organization works in specific domains not primarily covered by cantonal services"
    reference = "SR 915.1 Art. 7 let. b"


class vulg_org_accord_centrales_cantons(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the organization works in agreement with advisory centers and cantonal services"
    reference = "SR 915.1 Art. 7 let. c"


class vulg_org_eligible_aide(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether an organizational advisory service is eligible for financial aid"
    reference = "SR 915.1 Art. 7"

    def formula(person, period, parameters):
        couvre = person('vulg_org_couvre_region_linguistique', period)
        domaine = person('vulg_org_domaine_particulier', period)
        accord = person('vulg_org_accord_centrales_cantons', period)
        return couvre * domaine * accord
