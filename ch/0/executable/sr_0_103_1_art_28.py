"""SR 0.103.1 Art. 28

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *

class applies_to_entire_federal_state(Variable):
    value_type = bool
    label = "Applies to entire federal state (Art. 28 SR 0.103.1)"

    def formula_affected_entities_(variable, period, parameters):
        return True
