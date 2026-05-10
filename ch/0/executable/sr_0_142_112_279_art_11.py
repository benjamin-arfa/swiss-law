"""SR 0.142.112.279 Art. 11

Generated from: ch/0/de/0.142.112.279.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class can_repatriate_by_flight(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Can be repatriated by plane (Art. 11 SR 0.142.112.279)"

    def formula(person, period, parameters):
        num_repatriation_candidates = person("num_repatriation_candidates", period)
        max_flight_capacity = parameters(period).repatriation.max_flight_capacity
        return num_repatriation_candidates >= max_flight_capacity
