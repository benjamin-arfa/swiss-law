"""SR 0.108.1 Art. 1

Generated from: ch/0/de/0.108.1.md
"""

from openfisca_core.model_api import *


class discrimination_convention_compliance(Variable):
    value_type = bool
    label = "Compliance with the discrimination convention (Art. 1 SR 0.108.1)"

    def formula(__, period, parameters):
        return True
