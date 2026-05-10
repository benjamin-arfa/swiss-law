"""SR 231.11 Art. 18a

Generated from: ch/231/de/231.11.md

Kleinsendung: Eine Sendung mit hoechstens 3 Einheiten und
einem Bruttogewicht von weniger als 5 Kilogramm.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sendung_anzahl_einheiten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Einheiten in der Sendung"
    reference = "SR 231.11 Art. 18a"


class sendung_bruttogewicht_kg(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Bruttogewicht der Sendung in Kilogramm"
    reference = "SR 231.11 Art. 18a"


class ist_kleinsendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sendung als Kleinsendung gilt (max. 3 Einheiten, unter 5 kg)"
    reference = "SR 231.11 Art. 18a"

    def formula(person, period, parameters):
        anzahl = person('sendung_anzahl_einheiten', period)
        gewicht = person('sendung_bruttogewicht_kg', period)
        return (anzahl <= 3) * (gewicht < 5)
