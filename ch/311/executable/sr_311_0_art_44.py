"""SR 311.0 Art. 44

Generated from: ch/fr/311/311.0.md

Art. 44: Delai d'epreuve (Probezeit / Probation period)
- Abs. 1: Probation period of 2-5 years for suspended sentences.
- Abs. 2: Court may order probation assistance and rules of conduct.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_probezeit_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Probezeit in Jahren (2 bis 5)"
    reference = "SR 311.0 Art. 44 Abs. 1"


class stgb_probezeit_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Probezeit innerhalb des gesetzlichen Rahmens liegt (2-5 Jahre)"
    reference = "SR 311.0 Art. 44 Abs. 1"

    def formula(person, period, parameters):
        probezeit = person('stgb_probezeit_jahre', period)
        return (probezeit >= 2) * (probezeit <= 5)


class stgb_bewaehrungshilfe_angeordnet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob Bewaehrungshilfe angeordnet wurde"
    reference = "SR 311.0 Art. 44 Abs. 2"
