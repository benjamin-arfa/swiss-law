"""SR 321.0 Art. 49b

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fruehere_landesverweisung_angeordnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gegen die Person wurde bereits eine Landesverweisung angeordnet"
    reference = "SR 321.0 Art. 49b Abs. 1"


class fruehere_landesverweisung_noch_wirksam(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die fruehere Landesverweisung ist noch wirksam (nicht abgelaufen)"
    reference = "SR 321.0 Art. 49b Abs. 2"


class landesverweisung_wiederholungsfall_dauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer der Landesverweisung im Wiederholungsfall (20 Jahre oder lebenslaenglich)"
    reference = "SR 321.0 Art. 49b"

    def formula(person, period, parameters):
        fruehere = person('fruehere_landesverweisung_angeordnet', period)
        noch_wirksam = person('fruehere_landesverweisung_noch_wirksam', period)

        # Abs. 1: Wiederholungsfall → 20 Jahre
        # Abs. 2: Wenn fruehere noch wirksam → lebenslänglich (codiert als 99)
        return where(
            fruehere * noch_wirksam,
            99,  # lebenslänglich
            where(fruehere, 20, 0)
        )
