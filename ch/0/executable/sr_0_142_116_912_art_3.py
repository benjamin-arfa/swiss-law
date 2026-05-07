"""SR 0.142.116.912 Art. 3

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *

class has_valid_reisdence_visa(Variable):
    value_type = bool
    entity = Person
    default_value = False
    label = "Has a valid residence visa (SR 0.142.116.912 Art. 3)"

    def formula(_, _, __):
        return True  # The actual logic for obtaining a valid visa can't be implemented here, as it's not a direct calculation of existing variables
