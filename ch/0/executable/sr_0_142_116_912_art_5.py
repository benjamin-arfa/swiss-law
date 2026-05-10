"""SR 0.142.116.912 Art. 5

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class free_residence(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Right to free residence in Switzerland (SR 0.142.116.912 Art. 5)"

    def formula(person, period, parameters):
        is_swiss_citizen = person("is_swiss_citizen", period)
        is_other_state_citizen = person("is_other_state_citizen", period)
        has_valid_residence_authorization = person("has_valid_residence_authorization", period)
        
        return is_swiss_citizen & is_other_state_citizen & has_valid_residence_authorization
