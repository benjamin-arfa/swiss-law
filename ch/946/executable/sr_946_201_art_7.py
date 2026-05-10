"""SR 946.201 Art. 7

Generated from: ch/946/de/946.201.md

Strafbestimmungen:
- Vorsaetzliche Widerhandlung: Geldstrafe; bei schwerer: Freiheitsstrafe bis 1 Jahr
- Fahrlaessig: Busse bis 100'000 CHF
- Versuch und Gehilfenschaft strafbar
- Verjaehrung: 7 Jahre
- Faelschung von Ursprungserzeugnissen: Freiheitsstrafe bis 3 Jahre oder Geldstrafe
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aussenwirtschaft_vorsaetzliche_widerhandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine vorsaetzliche Widerhandlung gegen Aussenwirtschaftsvorschriften vorliegt"
    reference = "SR 946.201 Art. 7 Abs. 1"


class aussenwirtschaft_schwere_widerhandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine schwere vorsaetzliche Widerhandlung vorliegt"
    reference = "SR 946.201 Art. 7 Abs. 1"


class aussenwirtschaft_fahrlaessige_widerhandlung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine fahrlaessige Widerhandlung vorliegt"
    reference = "SR 946.201 Art. 7 Abs. 1"


class aussenwirtschaft_maximale_busse(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse bei Widerhandlung gegen Aussenwirtschaftsvorschriften (CHF)"
    reference = "SR 946.201 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        fahrlaessig = person('aussenwirtschaft_fahrlaessige_widerhandlung', period)
        return where(fahrlaessig, 100000, 0)


class aussenwirtschaft_max_freiheitsstrafe_jahre(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Freiheitsstrafe bei Widerhandlung (Jahre)"
    reference = "SR 946.201 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        schwer = person('aussenwirtschaft_schwere_widerhandlung', period)
        return where(schwer, 1, 0)


class aussenwirtschaft_verjaehrungsfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Verjaehrungsfrist fuer Strafverfolgung (Jahre)"
    reference = "SR 946.201 Art. 7 Abs. 3"

    def formula(person, period, parameters):
        return 7
