"""SR 311.1 Art. 4

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tat_vor_10_altersjahr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat das Kind die Tat vor dem vollendeten 10. Altersjahr begangen"
    reference = "SR 311.1 Art. 4"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        return alter < 10


class benachrichtigung_gesetzliche_vertreter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sind die gesetzlichen Vertreter zu benachrichtigen (Tat vor 10. Altersjahr)"
    reference = "SR 311.1 Art. 4"

    def formula(person, period, parameters):
        return person('tat_vor_10_altersjahr', period)
