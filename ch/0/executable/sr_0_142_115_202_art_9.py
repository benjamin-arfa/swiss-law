"""SR 0.142.115.202 Art. 9

Generated from: ch/0/de/0.142.115.202.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import ContractingParty


template class suspension_can_happen(Variable):
    value_type = bool
    entity = ContractingParty
    definition_period = "
    label = "Agreement can be suspended by any contracting party (Art. 9 SR 0.142.115.202)"

    def formula(contracting_party, period, parameters):
        return True
