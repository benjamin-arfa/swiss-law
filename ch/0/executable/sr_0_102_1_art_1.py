"""SR 0.102.1 Art. 1

Generated from: ch/0/de/0.102.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_cross_national.entities import Person
from enum import Enum


class right_to_participate(Enum):
    VOTE = 1
    RUN_AS_CANDIDATE = 2

class right_to_participate(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Right to participate in local governance (SR 0.102.1 Art. 1)"

    def formula(person, period, parameters):
        country = parameters(period).country
        # check country-specific laws regarding voting rights and candidate eligibility
        if country == "CH":
            return right_to_participate.VOTE | right_to_participate.RUN_AS_CANDIDATE
        else:
            return right_to_participate.VOTE
