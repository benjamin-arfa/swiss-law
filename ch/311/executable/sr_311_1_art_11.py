"""SR 311.1 Art. 11

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schuldhaft_gehandelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche schuldhaft gehandelt"
    reference = "SR 311.1 Art. 11 Abs. 2"


class einsichtsfaehigkeit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist der Jugendliche faehig, das Unrecht seiner Tat einzusehen und danach zu handeln"
    reference = "SR 311.1 Art. 11 Abs. 2"


class strafe_anordnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sind die Voraussetzungen fuer die Verhaengung einer Strafe erfuellt"
    reference = "SR 311.1 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        schuld = person('schuldhaft_gehandelt', period)
        einsicht = person('einsichtsfaehigkeit', period)
        return schuld * einsicht
