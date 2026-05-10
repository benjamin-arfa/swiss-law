"""SR 281.1 Art. 20

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_wechselbetreibung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Es handelt sich um eine Wechselbetreibung"
    reference = "SR 281.1 Art. 20"


class beschwerdefrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Frist in Tagen für Anhebung der Beschwerde"
    reference = "SR 281.1 Art. 17/20"

    def formula(person, period, parameters):
        wechsel = person('ist_wechselbetreibung', period)
        # Wechselbetreibung: 5 Tage, sonst 10 Tage
        return where(wechsel, 5, 10)


class behoerde_erledigungsfrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Frist in Tagen, in der die Behörde die Beschwerde zu erledigen hat"
    reference = "SR 281.1 Art. 20"

    def formula(person, period, parameters):
        wechsel = person('ist_wechselbetreibung', period)
        # Bei Wechselbetreibung innerhalb von 5 Tagen
        return where(wechsel, 5, 0)  # 0 = keine spezifische Frist bei normaler Betreibung
