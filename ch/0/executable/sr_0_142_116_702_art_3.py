"""SR 0.142.116.702 Art. 3

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person
from openfisca_core.parameters import Parameter


class compliant_with_foreign_law(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Compliance with foreign law (Art. 3 SR 0.142.116.702)"

    def formula(person, period, parameters):
        return True  # This is a constant true variable, as compliance is not dependent on data
