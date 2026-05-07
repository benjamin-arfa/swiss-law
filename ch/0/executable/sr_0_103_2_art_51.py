"""SR 0.103.2 Art. 51

Generated from: ch/0/de/0.103.2.md
"""

import openfisca_core.model_api
from openfisca_core.periods import YEAR
from openfisca_core.variables import Variable
from openfisca_core.priors import Prior


class has_accepted_asas_amendment(Variable):
    value_type = bool
    entity = openfisca_core.entities.Economy
    definition_period = YEAR
    label = "Status of ASAS amendment acceptance"
    default_value = False

    def formula(economy, period, parameters):
        # Prior is not used here but could be a good place to define the initial state
        return economy.has_accepted_asas_amendment
