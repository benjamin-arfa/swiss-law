"""SR 0.142.117.589 Art. 19

Generated from: ch/0/de/0.142.117.589.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class expert_committee_meeting_in_switzerland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Meeting of Expert Committee in Switzerland (Art. 19 SR 0.142.117.589)"

    def formula(person, period, parameters):
        met_in_switzerland = 0
        num_commissions = period.length
        if parameters(period).policy_event.expert_committee_meeting_switzerland:
            met_in_switzerland = 1
        return met_in_switzerland

class expert_committee_meeting_in_tunesien(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Meeting of Expert Committee in Tunesien (Art. 19 SR 0.142.117.589)"

    def formula(person, period, parameters):
        met_in_tunesien = 0
        num_commissions = period.length
        if parameters(period).policy_event.expert_committee_meeting_tunesien:
            met_in_tunesien = 1
        return met_in_tunesien
