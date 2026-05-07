"""SR 0.103.2 Art. 13

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class deportation_conditions_met(Variable):
    value_type = bool
    entity = Person
    label = "Conditions for deportation (Art. 13 SR 0.103.2)"

    def formula(person, period, parameters):
        valid_residence = person.has_residence_in ContractingState
        lawful_decree = ...  # implement check for lawful decision
        opportunity_to_present_arguments = ...  # implement check for opportunity to present arguments
        zving_gründe_nationale_sicherheit = ...  # implement check for overriding security concerns

        return lawful_decree and opportunity_to_present_arguments and not zving_gründe_nationale_sicherheit
