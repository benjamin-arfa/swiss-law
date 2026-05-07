"""SR 0.142.116.909 Art. 20

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class new_york_statelessness(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD(yearly)
    label = "New York Convention on statelessness status"

    def formula(person, period, parameters):
        is_stateless_person = parameters(period).switzerland.statelessness.is_stateless_person
        special_status_recieved = parameters(period).switzerland.statelessness.special_status_recieved
        new_york_convention_citizenship = parameters(period).switzerland.statelessness.new_york_convention_citizenship

        foreign_stay = person("foreign_stay", period)
        foreign_nationality = person("foreign_nationalship", period)

        foreign_travel_documents = foreign_stay & foreign_nationality

        if (is_stateless_person == True) | foreign_travel_documents:
            return True
        else:
            return special_status_recieved & new_york_convention_citizenship
