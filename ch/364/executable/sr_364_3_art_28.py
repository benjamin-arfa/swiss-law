"""SR 364.3 Art. 28

Generated from: ch/364/de/364.3.md

Vollzugsstufen fuer die Rueckfuehrungen (Stufen 1-4).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class rueckfuehrung_person_stimmt_zu(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rueckzufuehrende Person hat einer selbstaendigen Rueckreise zugestimmt"
    reference = "SR 364.3 Art. 28 Abs. 1"


class rueckfuehrung_koerperlicher_widerstand_erwartet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Es wird erwartet, dass die Person koerperlichen Widerstand leistet"
    reference = "SR 364.3 Art. 28 Abs. 1"


class rueckfuehrung_starker_widerstand_erwartet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Es wird erwartet, dass die Person starken koerperlichen Widerstand leistet (Sonderflug noetig)"
    reference = "SR 364.3 Art. 28 Abs. 1 Bst. d"


class rueckfuehrung_vollzugsstufe(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Vollzugsstufe der Rueckfuehrung (1-4)"
    reference = "SR 364.3 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        stimmt_zu = person('rueckfuehrung_person_stimmt_zu', period)
        widerstand = person('rueckfuehrung_koerperlicher_widerstand_erwartet', period)
        stark = person('rueckfuehrung_starker_widerstand_erwartet', period)
        # Stufe 1: stimmt zu; Stufe 2: stimmt nicht zu, kein Widerstand;
        # Stufe 3: Widerstand erwartet, Linienflug moeglich; Stufe 4: starker Widerstand, Sonderflug
        return select(
            [stark, widerstand, not_(stimmt_zu), stimmt_zu],
            [4, 3, 2, 1],
            default=2
        )


class rueckfuehrung_mindestbegleitung(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestanzahl Polizeibegleiter fuer die Rueckfuehrung"
    reference = "SR 364.3 Art. 28 Abs. 1"

    def formula(person, period, parameters):
        stufe = person('rueckfuehrung_vollzugsstufe', period)
        return select(
            [stufe == 1, stufe == 2, stufe == 3, stufe == 4],
            [0, 2, 2, 2],
            default=0
        )
