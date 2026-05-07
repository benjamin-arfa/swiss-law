"""SR 0.111 Art. 26

Generated from: ch/0/de/0.111.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person, Agreement


class contract_active(Variable):
    value_type = bool
    entity = Agreement
    definition_period = YEAR
    label = "Is contract active (Art. 26 SR 0.111)"

    def formula(agreement, period, parameters):
        return True  # Simplification: we are not modeling 'is active' through parameters or computations
