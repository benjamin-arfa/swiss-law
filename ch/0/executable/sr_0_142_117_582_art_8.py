"""SR 0.142.117.582 Art. 8

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class ahv_international_obligations_unaffected(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "International obligations unaffected by the present Agreement (Art. 8 SR 0.142.117.582)"

    def formula(countries, period, parameters):
        return True
