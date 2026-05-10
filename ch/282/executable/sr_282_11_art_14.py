"""SR 282.11 Art. 14 - Verbindung und Verlaengerung von Massnahmen

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class massnahmen_koennen_kombiniert_werden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Mehrere Massnahmen nach Art. 13 koennen miteinander verbunden werden"
    reference = "SR 282.11 Art. 14 Abs. 2"

    def formula(self, period, parameters):
        return 1


class anzahl_verlaengerungen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl bisherige Verlaengerungen der Massnahmen"
    reference = "SR 282.11 Art. 14 Abs. 3"


class verlaengerung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Verlaengerung der Massnahmen ist zulaessig (max zweimal fuer je 5 Jahre)"
    reference = "SR 282.11 Art. 14 Abs. 3"

    def formula(self, period, parameters):
        bisherige = self('anzahl_verlaengerungen', period)
        return bisherige < 2
