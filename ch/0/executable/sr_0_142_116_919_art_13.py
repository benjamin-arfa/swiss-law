"""SR 0.142.116.919 Art. 13

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class notify_during_transit(Variable):
    value_type = bool
    entity = Institution
    label = "Notification of authorities during transit (SR 0.142.116.919 Art. 13)"

    def formula(institution, period, parameters):
        return 1
