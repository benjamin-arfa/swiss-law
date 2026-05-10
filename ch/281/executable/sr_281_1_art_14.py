"""SR 281.1 Art. 14

Generated from: ch/281/de/281.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class disziplinarmassnahme_ruege(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Disziplinarmassnahme: Rüge"
    reference = "SR 281.1 Art. 14 Abs. 2 Ziff. 1"


class disziplinarmassnahme_geldbusse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Disziplinarmassnahme: Geldbusse"
    reference = "SR 281.1 Art. 14 Abs. 2 Ziff. 2"


class maximale_geldbusse_chf(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Geldbusse in CHF"
    reference = "SR 281.1 Art. 14 Abs. 2 Ziff. 2"

    def formula(person, period, parameters):
        return person.filled_array(1000.0)


class maximale_amtseinstellung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Dauer der Amtseinstellung in Monaten"
    reference = "SR 281.1 Art. 14 Abs. 2 Ziff. 3"

    def formula(person, period, parameters):
        return person.filled_array(6)
