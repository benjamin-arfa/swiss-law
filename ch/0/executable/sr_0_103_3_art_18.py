"""SR 0.103.3 Art. 18

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class access_to_detainee_info(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right to detainee information (Art. 18 SR 0.103.3)"

    def formula(person, period, parameters):

        has_family_member = person("has_family_member", period)
        is_detainee = person("is_detainee", period)

        has_family_member_and_is_detainee = has_family_member & is_detainee

        # ... other access conditions

        return has_family_member_and_is_detainee  # For simplicity, let's focus on this specific scenario.
