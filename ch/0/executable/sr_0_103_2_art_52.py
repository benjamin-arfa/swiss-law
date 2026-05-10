"""SR 0.103.2 Art. 52

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notification_received_switzerland(Variable):
    value_type = bool
    entity = SwitzerlandEntity
    definition_period = YEAR
    label = "Notification received by Switzerland from the UN about CCM ratifications or changes (Art. 52 SR 0.103.2)"

    def formula(suisse, period, parameters):
        return any([
            (parameters(period).un_notification.ratification_year != 0 and parameters(period).un_notification.ratification_year <= period.year),
            (parameters(period).un_notification.amendment_year != 0 and parameters(period).un_notification.amendment_year <= period.year),
        ])
