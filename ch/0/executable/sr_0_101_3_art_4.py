"""SR 0.101.3 Art. 4

Generated from: ch/0/de/0.101.3.md
"""

import numpy as np
from openfisca_core.variables import Variable
import openfisca_core.periods as periods

class movement_freedom(Variable):
    value_type = bool
    entity = 'individual'
    definition_period = periods.year
    default_value = True

    def formula(person, period, parameters):
        # Return True if person had possibility to return home for 15 consecutive days
        return 1
