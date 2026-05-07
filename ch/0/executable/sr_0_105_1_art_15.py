"""SR 0.105.1 Art. 15

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *


class protected_status(Variable):
    value_type = bool
    variable LegalEntity = Person and Institution
    definition_period = MONTH
    label = "Protection from sanctions for providing information (Art. 15 SR 0.105.1)"

    def formula(entity, period, parameters):
        information_provided = entity("information_provided_to_preventive_subcommittee", period)
        return information_provided
