"""SR 0.142.117.542 Art. 7

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *

class treaty_effective_date(Variable):
    value_type = date
    default_value = date.today()
    entity = World
    definition_period = 'forever'
    label = "Effective date of the bilateral treaty (SR 0.142.117.542 Art. 7)"

    def formula(world, period, parameters):
        last_notification_date = world("last_treaty_notification", period)
        return last_notification_date + parameters(period).international_affairs.treaty_implementation.notification_delay
