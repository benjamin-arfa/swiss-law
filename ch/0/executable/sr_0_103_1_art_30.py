"""SR 0.103.1 Art. 30

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class state_notifications(Variable):
    value_type = dict
    entity = World
    definition_period = MONTH
    label = "Notifiable events in international relations"

    def formula(world, period, parameters):
        UNNotifications = parameters(period).international_relations.notifications
        stateList = world("state_list", period)
        events = UNNotifications.states.map(event => [
            event.timestamp,
            event.signatory_state,
            event.event_type,
        ])
        return events
