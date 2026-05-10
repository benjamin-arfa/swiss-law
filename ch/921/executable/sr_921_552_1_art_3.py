"""SR 921.552.1 Art. 3

Generated from: ch/921/de/921.552.1.md

Nachgewiesene Herkunft und Herkunftszeugnisse: Die Herkunft gilt fuer
ausgewaehltes, geprueftes und quellengesichertes Vermehrungsgut als
nachgewiesen. Kantonale Forstbehoerde stellt Herkunftszeugnisse aus.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vermehrungsgut_herkunft_nachgewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Herkunft des forstlichen Vermehrungsguts nachgewiesen ist"
    reference = "SR 921.552.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        ist_ausgewaehlt = person('vermehrungsgut_ist_ausgewaehlt', period)
        ist_geprueft = person('vermehrungsgut_ist_geprueft', period)
        ist_quellengesichert = person('vermehrungsgut_ist_quellengesichert', period)
        return ist_ausgewaehlt + ist_geprueft + ist_quellengesichert


class vermehrungsgut_ist_ausgewaehlt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermehrungsgut als 'ausgewaehlt' klassifiziert ist"
    reference = "SR 921.552.1 Art. 2"


class vermehrungsgut_ist_geprueft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermehrungsgut als 'geprueft' klassifiziert ist"
    reference = "SR 921.552.1 Art. 2"


class vermehrungsgut_ist_quellengesichert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vermehrungsgut als 'quellengesichert' klassifiziert ist"
    reference = "SR 921.552.1 Art. 2"
