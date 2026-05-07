"""SR 0.102 Art. 15

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class convention_signee(Variable):
    value_type = bool
    entity = Country
    definition_period = CUSTOM
    label = "Member of the Convention on Cybercrime (Art. 15 SR 0.102)"

    def formula(country, period, parameters):
        signed_states = parameters(period).convention_on_cybercrime.signatories
        ratified_states = parameters(period).convention_on_cybercrime.ratified_states
        return country == _find_state_to_approve(signed_states, ratified_states, parameters)

    @staticmethod
    def _find_state_to_approve(signed_states, ratified_states, parameters):
        approved_states = list(set(signed_states) - set(ratified_states))
        return next((state for state in approved_states if len(ratified_states) >= 3), None)


class convention_signature_approver(Variable):
    value_type = str
    entity = Country
    definition_period = CUSTOM
    label = "Convention on Cybercrime signature approver (Art. 15 SR 0.102)"

    def formula(country, period, parameters):
        signed_states = parameters(period).convention_on_cybercrime.signatories
        ratified_states = parameters(period).convention_on_cybercrime.ratified_states
        approving_states = [_find_approving_state(signed_states, ratified_states, parameters) for state in signed_states]
        return next((approver for approver in approving_states if approver), '')

    @staticmethod
    def _find_approving_state(signed_states, ratified_states, parameters):
        min_three = len(ratified_states) >= 3
        recent_states = [state for state in signed_states if (state not in ratified_states and min_three)]
        return next((state for state, date in parameters(period).convention_on_cybercrime.state_dates
                    if state in recent_states), None)


class signature_in-force_date(Variable):
    value_type = date
    entity = Country
    definition_period = CUSTOM
    label = "Date when signature takes effect (Art. 15 SR 0.102)"

    def formula(country, period, parameters):
        approving_date = parameters(period).convention_on_cybercrime.approving_dates[country]
        return approving_date
