"""SR 0.103.3 Art. 7

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class forced_disappearance_penalty(Variable):
    value_type = float
    definition_period = YEAR
    label = "Penalty for forced disappearance, as per SR 0.103.3 Art. 7"

    def formula(period, parameters):
        return parameters(period).justice.forced_disappearance.penalty
