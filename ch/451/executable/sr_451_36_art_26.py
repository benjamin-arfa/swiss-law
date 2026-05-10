"""SR 451.36 Art. 26

Generated from: ch/451/de/451.36.md
Charta - Mindestdauer 10 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class charta_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Park-Charta in Jahren"
    reference = "SR 451.36 Art. 26 Abs. 3"


class charta_dauer_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Charta-Dauer ist zulaessig (mindestens 10 Jahre)"
    reference = "SR 451.36 Art. 26 Abs. 3"

    def formula(person, period, parameters):
        dauer = person('charta_dauer_jahre', period)
        return dauer >= 10
