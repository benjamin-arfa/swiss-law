"""SR 0.101.3 Art. 10

Generated from: ch/0/de/0.101.3.md
"""

import numpy as np
from openfisca_core import periods
from openfisca_core.variables import Variable

class HasContractTerminatedAfterNotification(Variable):
    value_type = bool
    label = "Has contract been terminated?"
    reference = "SR 0.101.3, Art. 10, Section 2-3"
    entity = "Household"
    definition_period = "P10Y"

    def formula(hh, period, **variables):
        # Consider if any party has notified and the contract is already terminated
        has_notified = hh("has_notified_contract_end", period)
        contract_ended = hh("contract_term_date", period) < periods.last_period(period)
        return has_notified & contract_ended

To implement the "has_notified_contract_end" and "contract_term_date" variables, we would assume the following parameter values as defined in YAML snippet.
