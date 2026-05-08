"""SR 731.31 Art. 6

Generated from: ch/731/de/731.31.md

Loan recipient, purpose, and currency.
- Recipient: systemically critical company (Art. 2)
- Purpose: exclusively to cover liquidity shortfall
- Currency: exclusively Swiss Francs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class firevo_darlehen_waehrung_chf(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Darlehen wird ausschliesslich in CHF gewaehrt"
    reference = "SR 731.31 Art. 6 Abs. 3"
    default_value = True
