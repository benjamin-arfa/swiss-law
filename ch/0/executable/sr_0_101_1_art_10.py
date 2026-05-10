"""SR 0.101.1 Art. 10

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from .identities import PERSON, INDIVIDUAL

class is_withdrawn(Variable):
    value_type = bool
    label = "Withdrawn from the Convention"
    definition_period = ETERNITY

    def formula(self, period, congress):
        # Parameter for list of individuals mentioned in Article 1, paragraph 1
        individuals = congress.params["convention_withdrawal_individuals"]
        return self.congress.member("is_contracting_party") == True  # To be replaced

class withdrawal_effective_date(Variable):
    value_type = int
    label = "Effective date of withdrawal"
    definition_period = ETERNITY

    def formula(self, period, congress):
        # Return date of withdrawal (Hardcoded for illustrative purposes)
        return 2024
