"""SR 121.3 Art. 7

Generated from: ch/121/de/121.3.md

Zusammensetzung: UKI consists of 3-5 federal admin members with expertise.
VBS must not hold chair or majority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class uki_anzahl_mitglieder(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Mitglieder der UKI"
    reference = "SR 121.3 Art. 7 Abs. 1"


class uki_zusammensetzung_gueltig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zusammensetzung der UKI den Anforderungen entspricht"
    reference = "SR 121.3 Art. 7"

    def formula(person, period, parameters):
        anzahl = person('uki_anzahl_mitglieder', period)
        # Abs. 1: 3-5 Mitglieder
        return (anzahl >= 3) * (anzahl <= 5)
