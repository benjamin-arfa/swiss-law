"""SR 661.1 Art. 8

Generated from: ch/661/de/661.1.md

Art. 8 Bemessungsperiode (Assessment period):
1. For persons liable for direct federal tax on total income for the full levy
   year: the assessment period equals the federal tax assessment period.
2. If paragraph 1 does not apply: income in the levy year forms the assessment
   basis.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class wpev_bundessteuer_ganzjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the person pays direct federal tax on total income for the full levy year"
    reference = "SR 661.1 Art. 8 Abs. 1"


class wpev_einkommen_ersatzjahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Income in the levy year (CHF)"
    reference = "SR 661.1 Art. 8 Abs. 2"


class wpev_bemessungsgrundlage(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Assessment basis for the substitute levy (CHF)"
    reference = "SR 661.1 Art. 8"

    def formula(person, period, parameters):
        # If full-year federal tax: uses federal tax assessment period income
        # Otherwise: income in the levy year
        # Both resolve to the same variable for modeling purposes
        return person('wpev_einkommen_ersatzjahr', period)
