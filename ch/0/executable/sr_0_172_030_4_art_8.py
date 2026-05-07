"""SR 0.172.030.4 Art. 8

Generated from: ch/0/de/0.172.030.4.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import *
class convention_modification(Variable):
    value_type = bool
    label = "Modifications to AHV due to international agreement (Art. 8)">

    def formula(e, period):
        return False
