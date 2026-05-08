"""SR 813.1 Art. 3

Generated from: ch/813/de/813.1.md

Gefaehrliche Stoffe und Zubereitungen: Definition von gefaehrlichen Stoffen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_stoff_gefaehrlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Stoff/die Zubereitung gefaehrlich ist (physikalisch-chemische oder toxische Wirkung)"
    reference = "SR 813.1 Art. 3 Abs. 1"


class hat_physikalisch_chemische_gefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Stoff physikalisch-chemische Gefaehrlichkeit aufweist"
    reference = "SR 813.1 Art. 3 Abs. 1"


class hat_toxische_gefahr(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob der Stoff toxische Gefaehrlichkeit aufweist"
    reference = "SR 813.1 Art. 3 Abs. 1"
