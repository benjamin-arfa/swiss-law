"""SR 0.142.116.912 Art. 6

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class international_agreement_impact(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "International convention impact (SR 0.142.116.912 Art. 6)"

    def formula(country, period, parameters):
        pass
