"""SR 282.11 Art. 30 - Dauer der Beiratschaft

Generated from: ch/282/de/282.11.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class beiratschaft_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Angeordnete Dauer der Beiratschaft in Jahren"
    reference = "SR 282.11 Art. 30 Abs. 1"


class beiratschaft_maximale_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der Beiratschaft in Jahren"
    reference = "SR 282.11 Art. 30 Abs. 1"

    def formula(self, period, parameters):
        return 3


class beiratschaft_verlaengerung_maximale_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer einer Verlaengerung der Beiratschaft in Jahren"
    reference = "SR 282.11 Art. 30 Abs. 2"

    def formula(self, period, parameters):
        return 3


class beiratschaft_dauer_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Dauer der Beiratschaft ist zulaessig"
    reference = "SR 282.11 Art. 30 Abs. 1"

    def formula(self, period, parameters):
        dauer = self('beiratschaft_dauer_jahre', period)
        max_dauer = self('beiratschaft_maximale_dauer_jahre', period)
        return dauer <= max_dauer
