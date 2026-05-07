"""SR 0.142.116.919 Art. 11

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core periods import MONTH,
from openfisca_switzerland.entities import Person


class ahv_staff_supervision_duration(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Staff supervision duration after airport arrival under Art. 11 SR 0.142.116.919"

    def formula(person, period, parameters):
        arrival_time = person("arrival_time", period)
        threshold = parameters(period).max_supervision_duration
        supervision_duration = min((arrival_time // 86400) , threshold)
        return supervision_duration
