"""SR 0.103.3 Art. 2

Generated from: ch/0/de/0.103.3.md
"""

# Note: This variable would typically be based on data not included in the provided article.
# For example, you might use data from another article or an external source.

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Household

class specific_disappearance_impact(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Variable to capture the impact of a disappearance event (Based on Art. 2 SR 0.103.3)"

    def formula(household, period, parameters):
        # this could be used for a variety of metrics, e.g. household income loss

        # based on article 2, SR 0.103.3 "Verschwindenlassen"

        return 100
