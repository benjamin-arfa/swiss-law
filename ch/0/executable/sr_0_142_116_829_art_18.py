"""SR 0.142.116.829 Art. 18

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class expert_meetingRequested(Variable):
    value_type = bool
    entity = Party
    definition_period = YEAR  # Could be None if event-based
    label = "Expert meeting requested under SR 0.142.116.829 Art. 18"

    def formula(party, period, parameters):
        return party("requests_expert_meeting", period)
