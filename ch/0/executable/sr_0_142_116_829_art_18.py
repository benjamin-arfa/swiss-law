"""SR 0.142.116.829 Art. 18

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Party


class expert_meetingRequested(Variable):
    value_type = bool
    entity = Party
    definition_period = YEAR  # Could be None if event-based
    label = "Expert meeting requested under SR 0.142.116.829 Art. 18"

    def formula(party, period, parameters):
        return party("requests_expert_meeting", period)
