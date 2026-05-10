"""SR 934.21 Art. 3

Generated from: ch/934/de/934.21.md

Art. 3 Beteiligungsgesellschaft:
1. Federal shares in corporations are held by a holding company
   (private-law Aktiengesellschaft).
1bis. The Federal Council sets strategic objectives for the holding company
     for periods of four years.
1ter. The board of the holding company implements the Federal Council's
     strategic objectives and reports annually on achievement.
3. Transfer of the Confederation's capital or voting majority requires
   approval of the Federal Assembly.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bgrb_strategische_ziele_festgelegt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat strategische Ziele fuer die Beteiligungsgesellschaft festgelegt hat"
    reference = "SR 934.21 Art. 3 Abs. 1bis"


class bgrb_strategische_ziele_periode_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Dauer der strategischen Zielperiode in Jahren"
    reference = "SR 934.21 Art. 3 Abs. 1bis"

    def formula(person, period, parameters):
        return 4


class bgrb_abtretung_kapital_stimmenmehrheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Abtretung der Kapital- oder Stimmenmehrheit an Dritte erfolgt"
    reference = "SR 934.21 Art. 3 Abs. 3"


class bgrb_zustimmung_bundesversammlung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zustimmung der Bundesversammlung erforderlich ist"
    reference = "SR 934.21 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return person('bgrb_abtretung_kapital_stimmenmehrheit', period)
