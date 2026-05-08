"""SR 749.1 Art. 3

Generated from: ch/749/fr/749.1.md

Art. 3: Ownership requirements - capital and voting rights must be held
in majority by Swiss natural or legal persons.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ltsm_part_capital_suisse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Share of capital held by Swiss persons (0-1)"
    reference = "SR 749.1 Art. 3 al. 1"


class ltsm_part_droits_vote_suisse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Share of voting rights held by Swiss persons (0-1)"
    reference = "SR 749.1 Art. 3 al. 1"


class ltsm_condition_propriete_remplie(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the Swiss majority ownership and voting rights condition is met"
    reference = "SR 749.1 Art. 3 al. 1"

    def formula(person, period, parameters):
        capital = person('ltsm_part_capital_suisse', period)
        votes = person('ltsm_part_droits_vote_suisse', period)
        seuil = parameters(period).sr_749_1.seuil_majorite
        return (capital > seuil) * (votes > seuil)
