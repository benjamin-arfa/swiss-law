"""SR 0.103.3 Art. 9

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Since the legal text does not specify a variable formula, we assume a function that takes in jurisdiction conditions as parameters
def art_9_jurisdiction(is_offense_commit_in_territory, is_suspect_state_citizen, is_concealed_person_state_citizen, 
                      is_suspect_present_in_territory, is_state_complying_with_international_obligations):
    # Jurisdiction conditions are not straightforward to implement without a more complex domain-specific understanding.
    # The approach here is simplified, and actual implementation would depend on further analysis or consultation with domain experts.
    return (is_offense_commit_in_territory |
            is_suspect_state_citizen |
            (is_concealed_person_state_citizen & (not is_state_complying_with_international_obligations)) |
            (is_suspect_present_in_territory & (not is_state_complying_with_international_obligations)))

# Variable implementation (note: entity is assumed omitted for simplicity)
class art_9_jurisdiction(Variable):
    value_type = bool
    definition_period = MONTH
    
    def formula(policy, period, parameters):
        is_offense_commit_in_territory = policy("is_offense_commit_in_territory", period)
        is_suspect_state_citizen = policy("is_suspect_state_citizen", period)
        is_concealed_person_state_citizen = policy("is_concealed_person_state_citizen", period)
        is_suspect_present_in_territory = policy("is_suspect_present_in_territory", period)
        is_state_complying_with_international_obligations = policy("is_state_complying_with_international_obligations", period)
        return art_9_jurisdiction(is_offense_commit_in_territory, is_suspect_state_citizen, is_concealed_person_state_citizen, 
                                  is_suspect_present_in_territory, is_state_complying_with_international_obligations)
