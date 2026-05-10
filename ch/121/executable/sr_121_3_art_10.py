"""SR 121.3 Art. 10

Generated from: ch/121/de/121.3.md

Taetigkeiten: UKI reviews signals/cable intelligence orders.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class monate_seit_beginn_kabelaufklaerung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Monate seit Beginn der Kabelaufklaerung"
    reference = "SR 120.73 Art. 10 Abs. 2"


class uki_pruefung_kabelaufklaerung_faellig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die UKI-Pruefung des Kabelaufklaerungsauftrags faellig ist"
    reference = "SR 121.3 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        monate = person('monate_seit_beginn_kabelaufklaerung', period)
        # Pruefung innerhalb von 6 Monaten, danach mindestens jaehrlich
        return monate >= 6
