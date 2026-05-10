"""SR 0.142.116.919 Art. 10

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_foreignnational_transiting(Variable):
    value_type = bool
    entity = ContractingParty
    definition_period = DAY
    label = "Is a foreign national transiting (SR 0.142.116.919 Art. 10)?"

    def formula(contracting_party, period, parameters):
        return False  # Default: No foreign national is transiting (not applicable)
