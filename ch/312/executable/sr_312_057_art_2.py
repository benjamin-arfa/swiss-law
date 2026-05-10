"""SR 312.057 Art. 2

Generated from: ch/312/de/312.057.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beschlagnahmte_bargelder_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Betrag der beschlagnahmten Bargelder in CHF"
    reference = "SR 312.057 Art. 2 Abs. 1"


class beschlagnahme_dauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Beschlagnahme in Monaten"
    reference = "SR 312.057 Art. 2 Abs. 1"


class hinterlegungspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Muessen die Bargelder bei der Staatskasse hinterlegt oder angelegt werden"
    reference = "SR 312.057 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        betrag = person('beschlagnahmte_bargelder_betrag', period)
        dauer = person('beschlagnahme_dauer_monate', period)
        return (betrag > 5000) + (dauer > 3) > 0


class hinterlegungspflicht_betrag_schwelle(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwellenwert fuer die Hinterlegungspflicht (5000 CHF)"
    reference = "SR 312.057 Art. 2 Abs. 1"
    default_value = 5000.0


class hinterlegungspflicht_dauer_schwelle_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauerschwelle fuer die Hinterlegungspflicht (3 Monate)"
    reference = "SR 312.057 Art. 2 Abs. 1"
    default_value = 3
