"""SR 451.1 Art. 24

Generated from: ch/451/de/451.1.md
Organisation der ENHK und der EKD - hoechstens 15 Mitglieder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitglieder_enhk_ekd(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der ENHK bzw. EKD"
    reference = "SR 451.1 Art. 24 Abs. 1"


class anzahl_mitglieder_enhk_ekd_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder der ENHK/EKD ist zulaessig (hoechstens 15)"
    reference = "SR 451.1 Art. 24 Abs. 1"

    def formula(person, period, parameters):
        anzahl = person('anzahl_mitglieder_enhk_ekd', period)
        return anzahl <= 15
