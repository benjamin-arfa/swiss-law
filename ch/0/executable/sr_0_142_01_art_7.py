"""SR 0.142.01 Art. 7

Generated from: ch/0/de/0.142.01.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class dummy_variable(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dummy variable"

    def formula(person, period, parameters):
        return 1
