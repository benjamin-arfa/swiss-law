"""SR 0.103.2 Art. 50

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import *


class federal_state_boundaries(Variable):
    value_type = bool
    definition_period = YEAR
    label = "Federal state boundaries (Art. 50 SR 0.103.2)"

    def formula(federal_state, period, parameters):
        # Since this article is a general principle without any specific boundaries,
        # every part of a national federal state is considered bound.
        return True
