"""SR 915.1 Art. 10

Generated from: ch/915/fr/915.1.md

Art. 10: Financial aid for preliminary studies for innovative project
development in agriculture.
- al. 3: Aid amounts to at most 50% of the responsible organization's
  costs for the preliminary study, but no more than CHF 20,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vulg_couts_etude_preliminaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Costs of the responsible organization for the preliminary study (CHF)"
    reference = "SR 915.1 Art. 10 al. 3"


class vulg_aide_etude_preliminaire(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Financial aid for preliminary study of an innovative agricultural project (CHF)"
    reference = "SR 915.1 Art. 10 al. 3"

    def formula(person, period, parameters):
        p = parameters(period).sr_915_1
        couts = person('vulg_couts_etude_preliminaire', period)
        aide_pct = couts * p.aide_etude_preliminaire_taux
        return min_(aide_pct, p.aide_etude_preliminaire_plafond)
