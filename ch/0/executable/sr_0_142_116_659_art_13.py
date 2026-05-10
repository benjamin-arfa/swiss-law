"""SR 0.142.116.659 Art. 13

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_takeover_refusal_reason_provided(Variable):
    value_type = bool
    entity = None
    definition_period = MONTH
    label = "AHV takeover refusal written reason provided (Art. 13 SR 0.142.116.659)"

    def formula(e, period, parameters):
        ahv_takeover_refusal_reason_provided = e('ahv_takeover_refusal_reason_provided', period)
        # Assume that the variable is derived from another input
        # For simplicity, I assume it is already available
        return ahv_takeover_refusal_reason_provided
