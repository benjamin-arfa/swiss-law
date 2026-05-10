"""SR 311.1 Art. 10

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tat_mit_strafe_bedroht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche eine mit Strafe bedrohte Tat begangen"
    reference = "SR 311.1 Art. 10"


class besondere_betreuung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ergibt die Abklaerung, dass besondere erzieherische Betreuung oder therapeutische Behandlung noetig ist"
    reference = "SR 311.1 Art. 10"


class gewoehnlicher_aufenthalt_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche gewoehnlichen Aufenthalt in der Schweiz"
    reference = "SR 311.1 Art. 10 Abs. 2"


class schutzmassnahme_anordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sind die Voraussetzungen fuer die Anordnung einer Schutzmassnahme erfuellt"
    reference = "SR 311.1 Art. 10"

    def formula(person, period, parameters):
        tat = person('tat_mit_strafe_bedroht', period)
        betreuung = person('besondere_betreuung_erforderlich', period)
        aufenthalt = person('gewoehnlicher_aufenthalt_schweiz', period)
        return tat * betreuung * aufenthalt
