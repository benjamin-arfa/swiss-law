"""SR 0.103.1 Art. 4

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *

class protected_rights(Variable):
    value_type = bool
    entity = Households
    definition_period = YEAR
    label = "Protected rights (Art. 4 SR 0.103.1)"

    def formula(households, period, parameters):
        return True  # Since the article doesn't impose any conditions
