"""SR 235.1 Art. 20

Generated from: ch/235/de/235.1.md

Sperrung der Bekanntgabe: Betroffene kann Sperrung verlangen,
Bundesorgan kann verweigern/aufheben.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dsg_sperrung_verlangt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Betroffene Person hat Sperrung der Bekanntgabe verlangt"
    reference = "SR 235.1 Art. 20 Abs. 1"


class dsg_schutzwuerdiges_interesse_glaubhaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schutzwuerdiges Interesse an der Sperrung ist glaubhaft gemacht"
    reference = "SR 235.1 Art. 20 Abs. 1"


class dsg_rechtspflicht_bekanntgabe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rechtspflicht zur Bekanntgabe besteht"
    reference = "SR 235.1 Art. 20 Abs. 2 lit. a"


class dsg_aufgabenerfuellung_gefaehrdet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufgabenerfuellung des Bundesorgans waere durch Sperrung gefaehrdet"
    reference = "SR 235.1 Art. 20 Abs. 2 lit. b"


class dsg_sperrung_bekanntgabe_gewaehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Sperrung der Bekanntgabe wird gewaehrt"
    reference = "SR 235.1 Art. 20"

    def formula(person, period, parameters):
        verlangt = person('dsg_sperrung_verlangt', period)
        interesse = person('dsg_schutzwuerdiges_interesse_glaubhaft', period)
        rechtspflicht = person('dsg_rechtspflicht_bekanntgabe', period)
        gefaehrdet = person('dsg_aufgabenerfuellung_gefaehrdet', period)
        return verlangt * interesse * not_(rechtspflicht) * not_(gefaehrdet)
