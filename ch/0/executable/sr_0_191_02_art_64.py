"""SR 0.191.02 Art. 64

Generated from: ch/0/de/0.191.02.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class consular_officer_protection(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Presence of protection for honorary consular officer (Art. 64 SR 0.191.02)"

    def formula(person, period, parameters):
        # Only provide basic implementation; protection specifics depend on country/official position
        return True
