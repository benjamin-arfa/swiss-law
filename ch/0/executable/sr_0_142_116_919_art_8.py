"""SR 0.142.116.919 Art. 8

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class accommodation_reimbursement(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Accommodation reimbursement for foreigner transit (Art. 8 SR 0.142.116.919)"

    def formula(person, period, parameters):
        has_cost = parameters(period).international_treaty.ahv_foreign_travel.accommodation_reimbursement
        if has_cost:
            return person("accommodated_foreign_nationals", period) * person("cost_per_foreignational", period)
        else:
            return 0
