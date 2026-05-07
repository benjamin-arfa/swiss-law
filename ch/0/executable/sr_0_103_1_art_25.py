"""SR 0.103.1 Art. 25

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import Variable


class general_principle(Variable):
    value_type = bool
    entity = None
    definition_period = YEAR
    label = "Guarantee of free use of natural resources (Art. 25 SR 0.103.1)"

    def formula(__, period, parameters):
        return True  # By law, this principle is true, so there's no calculation needed
