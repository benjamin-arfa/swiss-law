"""SR 0.142.117.149 Art. 3

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class re_admission_required(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD
    label = "Re-admission required (SR 0.142.117.149 Art. 3)"

    def formula(person, period, parameters):
        return True  # Replace with actual conditions
