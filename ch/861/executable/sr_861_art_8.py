"""SR 861 Art. 8

Generated from: ch/de/861.md

Regular evaluation of the impact of this law.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhg_evaluation_regelmaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auswirkung des KBFHG regelmaessig evaluiert wird"
    reference = "SR 861 Art. 8"

    def formula(person, period, parameters):
        return True
