"""SR 170.32 Art. 21

Generated from: ch/170/de/170.32.md

Verjährung des Rückgriffsanspruchs des Bundes gegen einen Beamten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class datum_anerkennung_schadenersatzpflicht(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Datum der Anerkennung oder rechtskräftigen Feststellung der Schadenersatzpflicht des Bundes"
    reference = "SR 170.32, Art. 21"


class datum_schaedigendes_verhalten(Variable):
    value_type = date
    entity = Person
    definition_period = YEAR
    label = "Datum, an dem das schädigende Verhalten erfolgte oder aufhörte"
    reference = "SR 170.32, Art. 21"


class rueckgriff_verjaehrungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Absolute Verjährungsfrist des Rückgriffsanspruchs in Jahren (Art. 21 VG)"
    reference = "SR 170.32, Art. 21"

    def formula(person, period, parameters):
        toetung = person('toetung_eingetreten', period)
        verletzung = person('koerperverletzung_eingetreten', period)
        # 20 Jahre bei Tötung oder Körperverletzung, sonst 10 Jahre
        return where(toetung + verletzung > 0, 20, 10)


class rueckgriff_relative_verjaehrungsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Relative Verjährungsfrist ab Anerkennung der Schadenersatzpflicht (Art. 21 VG)"
    reference = "SR 170.32, Art. 21"

    def formula(person, period, parameters):
        # 3 Jahre ab Anerkennung/Feststellung
        return person('datum_anerkennung_schadenersatzpflicht', period) * 0 + 3
