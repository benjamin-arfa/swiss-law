"""SR 0.101.1 Art. 6

Generated from: ch/0/de/0.101.1.md
"""

import numpy as np

from openfisca_core.variables import Variable


class PersonBindedByConvention(Variable):
    value_type = bool
    entity = 'Person'
    label = 'Is the person bound by the convention?'
    definition_period = 'year'

    def formula(person, period, parameters):
        # This variable is set based on the convention.
        return person('is_party_to_convention'), period
