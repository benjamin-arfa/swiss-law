"""SR 0.105 Art. 23

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_membership_benefits(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Committee membership benefits (Art. 23 SR 0.105)"

    def formula(person, period, parameters):
        committees = [
            'committee_a',
            'committee_b',
            # Add other committees as needed
        ]
        committee_member = person(any_of([f"is_member_of_{committee}" for committee in committees]), period)
        return committee_member
