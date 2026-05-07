"""SR 0.142.112.913 Art. 7

Generated from: ch/0/de/0.142.112.913.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class collaboration_with_switzerland(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Collaboration between Switzerland and [partner country] according to Art. 7 of the treaty"

    def formula(country, period, parameters):
        return True  # This is more of a conceptual representation rather than a calculation
