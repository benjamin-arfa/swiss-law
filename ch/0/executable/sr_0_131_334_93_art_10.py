"""SR 0.131.334.93 Art. 10

Generated from: ch/0/de/0.131.334.93.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Government


class align_healthcare_agreements(Variable):
    value_type = bool
    entity = Government
    definition_period = YEAR
    label = "Align healthcare agreements with Framework Agreement (Art. 10 SR 0.131.334.93)"

    def formula(government, period, parameters):
        agreement_date = government("agreement_date")
        framework_effective_date = government("framework_effective_date")
        if agreement_date < framework_effective_date:
            return (period.start.year - framework_effective_date.year) <= 2
        else:
            return True
