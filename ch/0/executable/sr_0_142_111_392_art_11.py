"""SR 0.142.111.392 Art. 11

Generated from: ch/0/de/0.142.111.392.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Institution


class agreement_duration(Variable):
    value_type = int
    entity = Institution
    definition_period = YEAR
    label = "Agreement duration in the OpenFisca framework"

    def formula(agreement, period, parameters):
        # Since there is no available function to bind agreement duration dynamically
        return 5
