"""SR 0.103.22 Art. 9

Generated from: ch/0/de/0.103.22.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Region


class convention_applicability(Variable):
    value_type = bool
    entity = Region
    definition_period = YEAR
    label = "Applicability of the convention to the entire Swiss federal state (Art. 9 SR 0.103.22)"

    def formula(region, period, parameters):
        return True  # The article explicitly states that the convention applies to all parts of the federal state.
