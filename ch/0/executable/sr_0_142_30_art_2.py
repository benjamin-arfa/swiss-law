"""SR 0.142.30 Art. 2

Generated from: ch/0/de/0.142.30.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class refugee_general_obligations(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Refugee's general obligations (Art. 2 SR 0.142.30)"

    def formula(person, period, parameters):
        return True  # All refugees have general obligations.
