"""SR 0.142.116.727 Art. 11

Generated from: ch/0/de/0.142.116.727.md
"""

from openfisca_core.model_api import *

class modification_protocol_indicator(Variable):
    value_type = bool
    label = "Protocol regarding modification of existing treaty"
    
    def formula_(rule, period, parameters):
        return True  # Always True as protocol modification is the subject of the variable
