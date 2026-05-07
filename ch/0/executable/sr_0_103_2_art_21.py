"""SR 0.103.2 Art. 21

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.parameters import time_invariant_parameters


class is_assembly_right_restricted(Variable):
    value_type = bool
    definition_period = YEAR
    label = "Is the right to freedom of assembly restricted?"

    def formula(social, period, parameters):
        return True  # this value is likely fixed and not change dynamically
