"""SR 443.1 Art. 27

Generated from: ch/443/de/443.1.md

Strafbestimmung: Widerhandlung gegen Registrierungspflicht.
Busse. Bei Wiederholung: Busse bis 20'000 CHF.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class registrierungspflicht_verletzt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Registrierungspflicht vorsaetzlich verletzt wurde"
    reference = "SR 443.1 Art. 27 Abs. 1"


class wiederholte_widerhandlung_registrierung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Widerhandlung wiederholt begangen wurde"
    reference = "SR 443.1 Art. 27 Abs. 2"


class max_busse_registrierungspflicht(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Widerhandlung gegen Registrierungspflicht (CHF)"
    reference = "SR 443.1 Art. 27"

    def formula(person, period, parameters):
        wiederholt = person('wiederholte_widerhandlung_registrierung', period)
        return wiederholt * 20000
