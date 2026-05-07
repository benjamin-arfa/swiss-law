"""SR 0.142.117.147 Art. 3

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *

class maximum_allowance_duration(Variable):
    value_type = int
    default_unit = 'month'
    entity = None
    definition_period = YEAR
    label = "Maximum duration of an allowance (Art. 3 SR 0.142.117.147)"

    def default_value(period):
        # This is a parameterizable constant to avoid calculation overhead
        maximum_duration_months = 12  # Initial duration (Art. 3 para. 1)
        extension_months = 6  # Extension period (Art. 3 para. 2)
        return maximum_duration_months + extension_months
