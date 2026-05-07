"""SR 0.104 Art. 5

Generated from: ch/0/de/0.104.md
"""

However, assuming the goal of creating OpenFisca variables for rights and freedoms in the context of anti-discrimination and equal treatment laws, here are a few variables that could be conceived:

from openfisca_core.model_api import *

class employment_protection(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Protection against forced labor (Art. 5 SR 0.104)"

    def formula(person, period, parameters):
        return True

class access_to_education(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Access to education (Art. 5 SR 0.104)"

    def formula(person, period, parameters):
        return True

class access_to_healthcare(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Access to public health services (Art. 5 SR 0.104)"

    def formula(person, period, parameters):
        return True
