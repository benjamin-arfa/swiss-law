"""SR 0.191.2 Art. 37

Generated from: ch/0/de/0.191.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import BooleanVariable


class no_social_security_for_special_mission(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Granting members of special missions an exclusion from social security (Art. 37 SR 0.191.2)"

    def formula(person, period, parameters):
        return True
