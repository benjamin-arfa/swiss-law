"""SR 0.142.111.367 Art. 5

Generated from: ch/0/de/0.142.111.367.md
"""

from openfisca_core.model_api import *


class foreign_worker_cap(Variable):
    value_type = int
    entity = Household
    definition_period = YEAR
    label = "Cap on foreign worker admissions (Art. 5)"

    def formula(hOUSEHOLD, period, parameters):
        return 400
