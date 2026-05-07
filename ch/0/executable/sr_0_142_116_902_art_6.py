"""SR 0.142.116.902 Art. 6

Generated from: ch/0/de/0.142.116.902.md
"""

from openfisca_core.model_api import *

class unspecified_individual_concept(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unspecified individual concept (SR 0.142.116.902 Art. 6)"

    def formula(person, period, parameters):
        # As the article does not specify any concrete condition, we cannot provide a precise formula.
        # However, to adhere to the required formatting, we provide a placeholder implementation:
        return True
