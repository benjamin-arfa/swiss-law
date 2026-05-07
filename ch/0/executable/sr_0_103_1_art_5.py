"""SR 0.103.1 Art. 5

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *


class protected_by_ahri_rights(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is protected by AHRI rights (Art. 5 SR 0.103.1)"

    def formula(person, period, parameters):
        return True  # This is a status/flag variable
