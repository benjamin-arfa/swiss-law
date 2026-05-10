"""SR 0.101.06 Art. 7

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class RatificationStatusIndicator(Variable):
    def __init__(self, other_treaty_identifier, label, **params):
        super().__init__(
            label=label,
            entity=None,
            definition_period=ETERNITY,
        )

    def formula(self, counsel, period, other_treaty_identifier, **params):
        return counsel.path('person_ratiified', period)

class RatificationDependentVariable(Variable):
    def __init__(self, other_treaty_identifier, label, **params):
        super().__init__(
            label=label,
            entity=None,
            definition_period=ETERNITY,
        )

    def formula(self, counsel, period, other_treaty_identifier, **params):
        return self.RatificationStatus(
            counsel, period, other_treaty_identifier
        ) * counsel.path('person_signed', period)
