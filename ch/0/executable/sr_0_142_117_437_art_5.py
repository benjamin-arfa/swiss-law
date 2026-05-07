"""SR 0.142.117.437 Art. 5

Generated from: ch/0/de/0.142.117.437.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class allowed_employment_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is trainee allowed to engage in other employment activities (Art. 5 SR 0.142.117.437)?"

    def formula(person, period, parameters):
        return person("has_trainee_status", period)


class has_trainee_status(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is this person a trainee (Art. 5 SR 0.142.117.437)?"

    def formula(person, period, parameters):
        return False  # This variable is likely not needed since it's always False
