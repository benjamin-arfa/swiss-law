"""SR 0.142.112.149 Art. 6

Generated from: ch/0/de/0.142.112.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class take_back_request_expenditure(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Costs for transporting third-country nationals and stateless individuals to the airport (SR 0.142.112.149 Art. 6)"

    def formula(person, period, parameters):
        rate = parameters(period).social_security.stateless_individuals_transportation_cost
        return rate
