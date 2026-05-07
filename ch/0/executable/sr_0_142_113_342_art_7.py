"""SR 0.142.113.342 Art. 7

Generated from: ch/0/de/0.142.113.342.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class unwanted_person(Variable):
    value_type = bool
    entity = Person
    definition_period = DURATION_INDEFINITE
    label = "Person unwanted for public order and security (Art. 7 SR 0.142.113.342)"

    def formula(person, period, parameters):-
