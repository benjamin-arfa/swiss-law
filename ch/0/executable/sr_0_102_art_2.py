"""SR 0.102 Art. 2

Generated from: ch/0/de/0.102.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Municipality


class municipality(Variable):
    value_type = bool
    entity = Municipality
    definition_period = DAY
    label = "Is the entity a municipality?"
    default_value = True
