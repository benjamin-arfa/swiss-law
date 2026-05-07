"""SR 0.132.349.34 Art. 2

Generated from: ch/0/de/0.132.349.34.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class acc_implementation_cost_ratio(Variable):
    value_type = float
    entity = Country
    label = "Share of ACC implementation, monitoring or adjustment costs attributed to Switzerland (Art. 2 SR 0.132.349.34)"

    def formula(country, period, parameters):
        return 0.5
