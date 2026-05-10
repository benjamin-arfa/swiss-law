"""SR 446.2 Art. 9

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class hat_jugendschutzregelung_film(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es besteht eine fuer verbindlich erklaerte Jugendschutzregelung im Bereich Film"
    reference = "SR 446.2 Art. 9"


class hat_jugendschutzregelung_videospiele(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Es besteht eine fuer verbindlich erklaerte Jugendschutzregelung im Bereich Videospiele"
    reference = "SR 446.2 Art. 9"


class ist_mitglied_branchenorganisation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist Mitglied der Branchenorganisation"
    reference = "SR 446.2 Art. 9"


class jugendschutzregelung_verbindlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die verbindlich erklaerte Jugendschutzregelung gilt auch fuer Nicht-Mitglieder"
    reference = "SR 446.2 Art. 9"

    def formula(person, period, parameters):
        film = person('hat_jugendschutzregelung_film', period)
        videospiele = person('hat_jugendschutzregelung_videospiele', period)
        return film + videospiele >= 1
