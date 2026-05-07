"""SR 0.103.2 Art. 22

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class association_right(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "The right to association (Art. 22 SR 0.103.2)"

    def formula(person, period, parameters):
        return True  # this variable does not change, it's a fundamental right
