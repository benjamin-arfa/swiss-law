"""SR 0.142.116.702 Art. 1

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class diplomatic_residence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Diplomatic residence status (Art. 1 SR 0.142.116.702)"

    def formula(person, period, parameters):
        diplomatic_mission = person("diplomatic_mission", period)
        family_member = (person("family_status", period) == "family_member")
        foreign_passport = person("resides_outside_ch", period)

        sending_state_citizen = person("citizenship", period)
        diplomatic_passport = person("diplomatic_passport", period)

        # condition from paragraph 2
        lives_with_par1_member = person("lives_with_diplomatic_member", period)
        residence_status = person("diplomatic_residence", period)
        is_family_member = person("is_family_of_sent_dpl_person", period)

        # only apply logic for family members if both living conditions are met and sent_dpl_person does exist 
        return (diplomatic_passport & foreign_passport & diplomatic_mission) | (family_member & residence_status & lives_with_par1_member & is_family_member)
