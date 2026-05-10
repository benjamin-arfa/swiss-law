"""SR 818.101.1 Art. 5

Generated from: ch/818/de/818.101.1.md

Meldefrist bei Gefahren fuer die oeffentliche Gesundheit: Unverzuegliche
Meldung bei Hinweisen auf Gefahr fuer die oeffentliche Gesundheit.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_meldepflichtige_kantonale_behoerde(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person eine meldepflichtige kantonale Behoerde vertritt"
    reference = "SR 818.101.1 Art. 5"


class ist_fuehrerin_schiff_luftfahrzeug(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Fuehrerin eines Schiffs oder Luftfahrzeugs im internationalen Verkehr ist"
    reference = "SR 818.101.1 Art. 5"


class beobachtung_deutet_auf_gefahr_oeffentliche_gesundheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Beobachtung auf eine Gefahr fuer die oeffentliche Gesundheit hindeutet"
    reference = "SR 818.101.1 Art. 5"


class meldepflicht_unverzueglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Meldung unverzueglich erfolgen muss"
    reference = "SR 818.101.1 Art. 5"

    def formula(person, period, parameters):
        ist_behoerde = person('ist_meldepflichtige_kantonale_behoerde', period)
        ist_fuehrerin = person('ist_fuehrerin_schiff_luftfahrzeug', period)
        gefahr = person('beobachtung_deutet_auf_gefahr_oeffentliche_gesundheit', period)
        return (ist_behoerde + ist_fuehrerin > 0) * gefahr
