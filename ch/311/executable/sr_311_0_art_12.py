"""SR 311.0 Art. 12

Generated from: ch/fr/311/311.0.md

Art. 12: Intention et negligence (Vorsatz und Fahrlaessigkeit)
- Abs. 1: Only intentional acts punishable unless law expressly provides otherwise.
- Abs. 2: Intent: acting with consciousness and will; also dolus eventualis.
- Abs. 3: Negligence: culpable lack of due care.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_handlung_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Handlung vorsaetzlich begangen wurde"
    reference = "SR 311.0 Art. 12 Abs. 2"


class stgb_handlung_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Handlung fahrlaessig begangen wurde"
    reference = "SR 311.0 Art. 12 Abs. 3"


class stgb_fahrlaessigkeit_gesetzlich_strafbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob Fahrlaessigkeit bei dieser Straftat gesetzlich unter Strafe steht"
    reference = "SR 311.0 Art. 12 Abs. 1"


class stgb_strafbarkeit_subjektiv(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die subjektiven Strafbarkeitsvoraussetzungen erfuellt sind"
    reference = "SR 311.0 Art. 12"

    def formula(person, period, parameters):
        vorsatz = person('stgb_handlung_vorsaetzlich', period)
        fahrlaessig = person('stgb_handlung_fahrlaessig', period)
        f_strafbar = person('stgb_fahrlaessigkeit_gesetzlich_strafbar', period)

        # Intentional always punishable; negligent only if expressly so by law
        return vorsatz + (fahrlaessig * f_strafbar)
