"""SR 0.105 Art. 4

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class punished_torture(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person punished for torture (Art. 4 CEDAW)"

    def formula(person, period, parameters):
        return True
