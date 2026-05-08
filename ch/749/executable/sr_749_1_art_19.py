"""SR 749.1 Art. 19

Generated from: ch/749/fr/749.1.md

Art. 19: Validity of plan approval:
- al. 3: Approval lapses if construction not begun within 5 years of
  the decision becoming final.
- al. 4: OFT may extend validity by up to 3 years if justified.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltsm_annees_depuis_approbation(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Years since plan approval became final"
    reference = "SR 749.1 Art. 19 al. 3"


class ltsm_construction_commencee(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether construction has begun"
    reference = "SR 749.1 Art. 19 al. 3"


class ltsm_prolongation_accordee_annees(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of years of extension granted by OFT (max 3)"
    reference = "SR 749.1 Art. 19 al. 4"


class ltsm_approbation_caduque(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the plan approval has lapsed"
    reference = "SR 749.1 Art. 19 al. 3-4"

    def formula(person, period, parameters):
        p = parameters(period).sr_749_1
        annees = person('ltsm_annees_depuis_approbation', period)
        commencee = person('ltsm_construction_commencee', period)
        prolongation = person('ltsm_prolongation_accordee_annees', period)

        delai_total = p.delai_caducite_approbation + min_(prolongation, p.prolongation_max)
        return (1 - commencee) * (annees >= delai_total)
