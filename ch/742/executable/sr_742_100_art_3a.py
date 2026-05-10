"""SR 742.100 Art. 3a

Generated from: ch/742/fr/742.100.md

Art. 3a - Financing of RAIL 2000:
1. The Confederation provides resources to railway companies as conditionally
   repayable loans (at market or variable rates) or non-repayable contributions.
2. Market-rate loans may be granted up to 25% of total project cost
   (including capital costs). These loans are recorded on the balance sheet.
   Interest is capitalized and remunerated until track sections enter service.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rail2000_cout_projet_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total RAIL 2000 project cost including capital costs (CHF)"
    reference = "SR 742.100 Art. 3a Abs. 2"


class rail2000_pret_marche_max_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximum market-rate loan amount (CHF) - 25% of project cost"
    reference = "SR 742.100 Art. 3a Abs. 2"

    def formula(person, period, parameters):
        cout = person('rail2000_cout_projet_chf', period)
        p = parameters(period).sr_742_100
        return cout * p.pret_marche_max_pct / 100


class rail2000_contribution_fonds_perdu_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Non-repayable contribution amount (CHF)"
    reference = "SR 742.100 Art. 3a Abs. 1"


class rail2000_pret_conditionnel_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Conditionally repayable loan amount (CHF)"
    reference = "SR 742.100 Art. 3a Abs. 1"
