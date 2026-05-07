"""SR 0.142.116.909 Art. 4

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class has_deportation_initiated(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has deportation from Switzerland initiated or accepted back?"

    def formula(person, period, parameters):
        return False  # default to False
