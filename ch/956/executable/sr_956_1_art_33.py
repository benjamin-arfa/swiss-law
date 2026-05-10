"""SR 956.1 Art. 33-34

Generated from: ch/956/de/956.1.md

Berufsverbot und Veröffentlichung:
- FINMA kann bei schwerer Verletzung Berufsverbot in leitender Stellung aussprechen
- Berufsverbot max. 5 Jahre
- Veröffentlichung der Verfügung bei schwerer Verletzung nach Rechtskraft
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schwere_verletzung_aufsichtsrecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine schwere Verletzung aufsichtsrechtlicher Bestimmungen festgestellt wurde"
    reference = "SR 956.1 Art. 33 Abs. 1"


class hat_leitende_stellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person eine leitende Stellung bei einer Beaufsichtigten hat"
    reference = "SR 956.1 Art. 33 Abs. 1"


class berufsverbot_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Berufsverbot ausgesprochen werden kann"
    reference = "SR 956.1 Art. 33 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('schwere_verletzung_aufsichtsrecht', period) *
            person('hat_leitende_stellung', period)
        )


class berufsverbot_dauer_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Verfügte Dauer des Berufsverbots in Jahren"
    reference = "SR 956.1 Art. 33 Abs. 2"


class berufsverbot_dauer_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Dauer des Berufsverbots zulässig ist (max. 5 Jahre)"
    reference = "SR 956.1 Art. 33 Abs. 2"

    def formula(person, period, parameters):
        dauer = person('berufsverbot_dauer_jahre', period)
        max_dauer = parameters(period).sr_956_1.max_berufsverbot_jahre
        return (dauer > 0) * (dauer <= max_dauer)


class veroeffentlichung_verfuegung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die aufsichtsrechtliche Verfügung veröffentlicht werden kann"
    reference = "SR 956.1 Art. 34 Abs. 1"

    def formula(person, period, parameters):
        return person('schwere_verletzung_aufsichtsrecht', period)
