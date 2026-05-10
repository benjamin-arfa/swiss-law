"""SR 0.105.1 Art. 13

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from enum import Enum

class VisitType(Enum):
    REGULAR = 1
    FOLLOW_UP = 2


class subcommittee_visit(Variable):
    value_type = bool
    entity = None
    definition_period = YEAR
    label = "Subcommittee Visit (Art. 13 SR 0.105.1)"

    def formula(terms, period, parameters):
        return terms.first('subcommittee_visit_schedule', period)
