"""SR 0.111 Art. 49

Generated from: ch/0/de/0.111.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable


class treaty_deception_impact(Variable):
    value_type = bool
    label = "Impact of deception on treaty validity (Art. 49 SR 0.111)"
    entity = None  # not applicable to treaties
    definition_period = YEAR  # treaties are not typically time-dependent

    def formula(_):
        return True  # the boolean variable directly represents the condition
