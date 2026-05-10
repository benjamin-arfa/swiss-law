"""SR 419.11 Art. 10

Generated from: ch/419/de/419.11.md

Programmvereinbarungen - Dauer 4 Jahre, einmal verlaengerbar.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class programmvereinbarung_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Programmvereinbarung in Jahren"
    reference = "SR 419.11 Art. 10 Abs. 2"
    default_value = 4


class programmvereinbarung_bereits_verlaengert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Programmvereinbarung wurde bereits einmal verlaengert"
    reference = "SR 419.11 Art. 10 Abs. 3"


class programmvereinbarung_verlaengerbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Programmvereinbarung kann verlaengert werden"
    reference = "SR 419.11 Art. 10 Abs. 3"

    def formula(person, period, parameters):
        return not_(person('programmvereinbarung_bereits_verlaengert', period))
