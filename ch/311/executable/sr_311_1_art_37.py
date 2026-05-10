"""SR 311.1 Art. 37

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ausgesprochener_freiheitsentzug_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Dauer des ausgesprochenen Freiheitsentzugs in Monaten"
    reference = "SR 311.1 Art. 37"


class vollstreckungsverjaehrung_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vollstreckungsverjaehrungsfrist in Jahren"
    reference = "SR 311.1 Art. 37 Abs. 1"

    def formula(person, period, parameters):
        freiheitsentzug = person('ausgesprochener_freiheitsentzug_monate', period)
        return where(
            freiheitsentzug > 6,
            4,
            2
        )


class vollzug_ende_hoechstalter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Spaetestes Alter fuer den Vollzug jeder Strafe (25 Jahre)"
    reference = "SR 311.1 Art. 37 Abs. 2"
    default_value = 25
