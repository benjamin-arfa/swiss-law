"""SR 0.192.110.942.6 Art. 8

Generated from: ch/0/de/0.192.110.942.6.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Entity


class unrestricted_distribution(Variable):
    value_type = bool
    entity = Entity
    definition_period = MONTH
    label = "Unrestricted distribution of publications and information materials (SR 0.192.110.942.6 Art. 8)"

    def formula(entity, period, parameters):
        return True
