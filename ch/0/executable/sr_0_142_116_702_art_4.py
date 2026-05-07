"""SR 0.142.116.702 Art. 4

Generated from: ch/0/de/0.142.116.702.md
"""

from openfisca_core.model_api import *

class immigration_refusal_on_public_policy_reason(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY  # this can be any time period as there is no calculation

    def formula(person, period, parameters, **other_arguments):
        # Note: this calculation would typically depend on specific situation or other conditions
        # but as the legal text does not provide such conditions
        # we will assume it is always True or False as defined in the parameter
        return True  # or any other value as per parameter definition
