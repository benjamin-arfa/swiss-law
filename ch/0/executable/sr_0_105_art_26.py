"""SR 0.105 Art. 26

Generated from: ch/0/de/0.105.md
"""

# The following code is a simplified representation of how this might be done
from openfisca_core.model_api import *

class is_country_treaty_member(Variable):
    value_type = bool
    definition_period = DAY
    label = "Participation of a country in the Treaty (SR 0.105 Art. 26)"

    def formula(e, period, parameters):
        return e('participates_in_treaty', period)
