"""SR 0.105.1 Art. 1

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *

class anti_torture_protocol_applicability(Variable):
    value_type = bool
    label = "Anti-Torture Protocol applicability (SR 0.105.1 Art. 1)"

    def formula(variables, _, _):
        return True
