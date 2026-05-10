"""SR 0.111 Art. 61

Generated from: ch/0/de/0.111.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

def is_contract_terminated(event, parameters):
    was_misconduct = event("is_misconduct", "previous period")
    if was_misconduct:
        required_item_destroyed = event("is_required_item_destroyed", "previous period")
        enduring_loss = event("had_enuring_loss", "previous period")
        return required_item_destroyed or enduring_loss

class contract_termed(Variable):
    value_type = bool
    label = "Contract terminated due to contractual impossibility (Art. 61)"
    entity = None
    definition_period = None

    def formula(aggregate, period, parameters):
        events = aggregate["Contract_A", "termination_date"]
        return is_contract_terminated(events, parameters)
