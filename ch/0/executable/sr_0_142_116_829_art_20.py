"""SR 0.142.116.829 Art. 20

Generated from: ch/0/de/0.142.116.829.md
"""

Since this article is not directly related to calculating a monetary value, it might be better to consider creating a parameter to describe the availability of repatriation services rather than a variable calculating repatriation costs.

However assuming you still want to create a variable, here is a possible interpretation:

from openfisca_core.model_api import *

# assuming there's a way to store whether an individual can be repatriated
class can_be_repatriated(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Availability for repatriation"

    def formula(person, period, parameters):
        # this variable assumes that some conditions are met for repatriation
        # here a hypothetical function is used, assuming person has a valid citizenship and is registered
        valid_citizenship_and_registration = person("valid_citizenship") & person("registered_with_autorities")
        return valid_citizenship_and_registration
