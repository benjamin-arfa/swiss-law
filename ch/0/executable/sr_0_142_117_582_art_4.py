"""SR 0.142.117.582 Art. 4

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class entry_refusal(Variable):
    value_type = bool
    entity = Person
    definition_period = ON
    label = "Entry refusal (Art. 4 of the treaty)"

    def formula(person, period, parameters):
        return True  # This simply indicates whether the entry is refused or not
