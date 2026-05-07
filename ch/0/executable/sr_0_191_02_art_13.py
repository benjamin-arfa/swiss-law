"""SR 0.191.02 Art. 13

Generated from: ch/0/de/0.191.02.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class consular_post_head_prelicense(Variable):
    value_type = bool
    default_period = "date"
    unit = "C"
    label = "Head of a consular post with pre-license (Art. 13)"
    
    def formula_2010_01_01(person, period, parameters, international_sector):
        if international_sector == 'Consular':
            return True
        else:
            return False
