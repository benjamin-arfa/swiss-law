"""SR 0.103.2 Art. 46

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class respects_un_charter(Variable):
    value_type = bool
    entity = Person
    definition_period = LIFE
    label = "Respect for the United Nations Charter (Art. 46 SR 0.103.2)"

    def formula(person, period, parameters):
        return True  # always returns True since this is a principle
