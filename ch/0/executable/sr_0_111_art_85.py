"""SR 0.111 Art. 85

Generated from: ch/0/de/0.111.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class treaty_authentication(Variable):
    value_type = bool
    definition_period = MONTH
    label = "Treaty authentication status"

    def formula(person, period, parameters):
        return True  # Always authenticated, the treaty exists and the wording is agreed by all states.
