"""SR 523.51 Art. 9

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unredlichkeit_bei_leistung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Unredlichkeit bei einer Einzelleistung festgestellt"
    reference = "SR 523.51 Art. 9"


class note_bei_unredlichkeit(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Note bei Unredlichkeit (immer 1.0)"
    reference = "SR 523.51 Art. 9"

    def formula(person, period, parameters):
        return where(person('unredlichkeit_bei_leistung', period), 1.0, 0.0)
