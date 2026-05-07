"""SR 0.105.1 Art. 4

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class person_locked_up(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person under detention or imprisonment"

    def formula(person, period, parameters):
        confinement_facilities = parameters(period).institutions.confinement_facilities

        for facility in confinement_facilities:
            if facility == person("current_detention_facility", period):
                return True

        return False
