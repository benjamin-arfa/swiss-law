"""SR 0.101.06 Art. 1

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

class DeathPenaltyAbolished(Variable):
    value_type = bool
    variable = "death_penalty_abolished"
    definition_period = MONTH

    def formula_1_1(self, period):
        return 1
