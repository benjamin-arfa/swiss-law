"""SR 170.321 Art. 2

Generated from: ch/170/de/170.321.md

Zuständigkeit für Verfügungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schadenersatzanspruch_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betrag des Schadenersatzanspruchs in CHF"
    reference = "SR 170.321, Art. 2 Abs. 2"


class ist_geschaeftsbereich_bazg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fall liegt im Geschäftsbereich des Bundesamtes für Zoll und Grenzsicherheit"
    reference = "SR 170.321, Art. 2 Abs. 2"


class bazg_ist_zustaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "BAZG ist zuständig für die Verfügung (Art. 2 Abs. 2 VV-VG)"
    reference = "SR 170.321, Art. 2 Abs. 2"

    def formula(person, period, parameters):
        ist_bazg = person('ist_geschaeftsbereich_bazg', period)
        betrag = person('schadenersatzanspruch_betrag', period)
        # BAZG zuständig bei Ansprüchen unter 10'000 CHF in seinem Bereich
        return ist_bazg * (betrag < 10000)
