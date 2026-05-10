"""SR 0.103.3 Art. 23

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aware_of_enforced_disappearance(Variable):
    value_type = bool
    entity = Agent
    definition_period = MONTH
    label = "Aware of enforced disappearance laws (Art. 23 SR 0.103.3)"

    def formula(agent, period, parameters):
        trained = agent("trained_against_enforced_disappearance", period)
        banned_orders = parameters(period).enforced_disappearance.banned_orders
        report_suspects = parameters(period).enforced_disappearance.report_suspects

        return trained & banned_orders & report_suspects
