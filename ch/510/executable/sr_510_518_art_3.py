"""SR 510.518 Art. 3 - Verweilverbot

Generated from: ch/510/de/510.518.md

Wenn die militaerische Sicherheit es erfordert, kann das VBS nach Anhoeren
der Kantons- und Gemeindebehoerden bestimmten Personen das Verweilen in
der Naehe von militaerischen Anlagen untersagen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class militaerische_sicherheit_erfordert_verweilverbot(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die militaerische Sicherheit ein Verweilverbot erfordert"
    reference = "SR 510.518 Art. 3 Abs. 1"


class kantons_gemeindebehoerden_angehoert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Kantons- und Gemeindebehoerden angehoert wurden"
    reference = "SR 510.518 Art. 3 Abs. 1"


class verweilverbot_verfuegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Verweilverbot in der Naehe von militaerischen Anlagen verfuegt wurde"
    reference = "SR 510.518 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('militaerische_sicherheit_erfordert_verweilverbot', period)
            * person('kantons_gemeindebehoerden_angehoert', period)
        )


class verweilverbot_beschwerdefrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Beschwerdefrist gegen Verfuegungen des VBS in Tagen"
    reference = "SR 510.518 Art. 3 Abs. 2"

    def formula(person, period, parameters):
        return 30
