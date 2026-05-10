"""SR 0.103.2 Art. 41

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class complaint_submission(Variable):
    value_type = bool
    entity = StateParty
    definition_period = MONTH
    label = "Submission of a complaint to the Covenant Committee (Art. 41)"

    def formula(state_party, period, parameters):
        recognized_committee = parameters(period).human_rights.committee.recognized
        submissions = state_party("submissions_to_committee", period)

        domestic_procedures = state_party("domestic_procedures_completed", period)
        committee_exhaustion = domestic_procedures >= parameters(period).human_rights.committee.exhaustion_threshold

        return recognized_committee & (submissions == 1) & committee_exhaustion
