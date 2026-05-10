"""SR 311.1 Art. 19

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_person(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aktuelles Alter der Person"
    reference = "SR 311.1 Art. 19"


class massnahme_ende_hoechstalter(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechstalter fuer das Ende aller Massnahmen (25 Jahre)"
    reference = "SR 311.1 Art. 19 Abs. 2"
    default_value = 25


class massnahme_beendet_wegen_alter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Endet die Massnahme wegen Vollendung des 25. Altersjahres"
    reference = "SR 311.1 Art. 19 Abs. 2"

    def formula(person, period, parameters):
        alter = person('alter_person', period)
        return alter >= 25
