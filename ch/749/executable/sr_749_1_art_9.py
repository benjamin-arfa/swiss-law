"""SR 749.1 Art. 9

Generated from: ch/749/fr/749.1.md

Art. 9: Plan approval - covers all required federal authorizations.
al. 6: Approval granted if (a) no overriding public interest opposes it
and (b) the enterprise has sufficient financial capacity.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltsm_pas_interet_public_oppose(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether no overriding public interest opposes the plan approval"
    reference = "SR 749.1 Art. 9 al. 6 let. a"


class ltsm_capacite_financiere_suffisante(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the enterprise has sufficient financial capacity"
    reference = "SR 749.1 Art. 9 al. 6 let. b"


class ltsm_approbation_plans_octroyee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plan approval conditions are met"
    reference = "SR 749.1 Art. 9 al. 6"

    def formula(person, period, parameters):
        pas_interet = person('ltsm_pas_interet_public_oppose', period)
        capacite = person('ltsm_capacite_financiere_suffisante', period)
        return pas_interet * capacite
