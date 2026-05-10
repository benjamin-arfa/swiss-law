"""SR 281.1 Art. 20a

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class boeswillige_prozessfuehrung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Böswillige oder mutwillige Prozessführung liegt vor"
    reference = "SR 281.1 Art. 20a Abs. 2 Ziff. 5"


class maximale_busse_verfahren_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Busse bei böswilliger Prozessführung in CHF"
    reference = "SR 281.1 Art. 20a Abs. 2 Ziff. 5"

    def formula(person, period, parameters):
        return person.filled_array(1500.0)
