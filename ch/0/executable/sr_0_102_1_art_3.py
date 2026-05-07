"""SR 0.102.1 Art. 3

Generated from: ch/0/de/0.102.1.md
"""

from openfisca_core.model_api import *

class eligible_entity(Variable):
    value_type = bool
    label = "Eligible entity for Protocol application (SR 0.102.1 Art. 3)"

    def formula(e, period, parameters):
        state = parameters("state")
        # Assuming that parameters('state')[country] contains a list of applicable entities
        return e in list(parameters('state')[state])
