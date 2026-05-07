"""SR 0.105 Art. 31

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Institution


class termination_affecting_case_handling(Variable):
    value_type = bool
    entity = Institution
    definition_period = MONTH
    label = "Suspend post-termination case review"

    def formula(institution, period, parameters):
        termination_date = institution("termination_date", period)
        current_date = period.date
        return termination_date <= current_date
