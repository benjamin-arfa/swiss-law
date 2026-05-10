"""SR 420.1 Art. 55

Generated from: ch/420/de/420.1.md

Schweizerischer Wissenschaftsrat - Wahl und Organisation, 10-15 Mitglieder.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class swr_anzahl_mitglieder(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Mitglieder des Schweizerischen Wissenschaftsrats"
    reference = "SR 420.1 Art. 55 Abs. 2"


class swr_zusammensetzung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusammensetzung des SWR ist zulaessig (10 bis 15 Mitglieder)"
    reference = "SR 420.1 Art. 55 Abs. 2"

    def formula(person, period, parameters):
        anzahl = person('swr_anzahl_mitglieder', period)
        return (anzahl >= 10) * (anzahl <= 15)
