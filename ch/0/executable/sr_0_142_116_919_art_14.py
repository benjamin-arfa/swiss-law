"""SR 0.142.116.919 Art. 14

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *

class is_escort_personnel(Variable):
    value_type = bool
    definition_period = YEAR
    label = "Indicator for escort personnel (Art. 14 SR 0.142.116.919)"

    def formula(individual, period, parameters):
        return individual("is_escort_personnel", period)
