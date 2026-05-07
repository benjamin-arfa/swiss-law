"""SR 0.142.113.494 Art. 2

Generated from: ch/0/de/0.142.113.494.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Enterprise


class compliant_contract(Variable):
    value_type = bool
    entity = Enterprise
    definition_period = MONTH
    label = "Compliance with SR 0.142.113.494 Article 2"

    def formula(enterprise, period, parameters):
        proposed_contract = enterprise('proposed_contract', period)
        contradictory_terms = parameters(period).contracts.contract_disagreements
        for term in contradictory_terms:
            if term in proposed_contract:
                return False
        return True
