"""SR 232.16 Art. 48

Generated from: ch/232/de/232.16.md

Art. 48 defines criminal penalties for plant variety protection violations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sortenschutzverletzung_vorsaetzlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Vorsaetzliche Sortenschutzverletzung nach Art. 48 Ziff. 1"
    reference = "SR 232.16 Art. 48 Ziff. 1"

    def formula(person, period, parameters):
        verletzung = person('sortenschutz_verletzt', period)
        vorsaetzlich = person('handelt_vorsaetzlich', period)
        return verletzung * vorsaetzlich


class sortenschutzverletzung_fahrlaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Fahrlaessige Sortenschutzverletzung nach Art. 48 Ziff. 2 (Busse)"
    reference = "SR 232.16 Art. 48 Ziff. 2"

    def formula(person, period, parameters):
        verletzung = person('sortenschutz_verletzt', period)
        vorsaetzlich = person('handelt_vorsaetzlich', period)
        return verletzung * (1 - vorsaetzlich)
