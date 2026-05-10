"""SR 0.142.116.919 Art. 17

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class foreigner_transit_denied(Variable):
    value_type = bool
    definition_period = DAY
    label = "Foreigner transit denied (Art. 17, SR 0.142.116.919)"

    def formula(variables, period, parameters):
        # assume foreigner_specific_risks and criminal_history variables are defined elsewhere
        return (foreigner_specific_risks(variables, period, parameters) | criminal_history(variables, period, parameters))

class foreigner_specific_risks(Variable):
    value_type = bool
    definition_period = DAY
    label = "Specific risks for foreigner (Art. 17, SR 0.142.116.919)"

    def formula(variables, period, parameters):
        # Assume race, religion, nationality, social_group, and political_views variables are defined elsewhere
        return ((race(variables, period) == 1) | (religion(variables, period) == 1) | 
                (nationality(variables, period) == 1) | (social_group(variables, period) == 1) | 
                (political_views(variables, period) == 1))

class criminal_history(Variable):
    value_type = bool
    definition_period = DAY
    label = "Criminal history of foreigner (Art. 17 SR 0.142.116.919)"

    def formula(variables, period, parameters):
        # assume past_crimes variable is defined elsewhere
        return (past_crimes(variables, period) != 0)
