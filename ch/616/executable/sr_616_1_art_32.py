"""SR 616.1 Art. 32

Generated from: ch/616/de/616.1.md
Limitation periods:
- Claims from subsidy relationships: 5 years
- Refund claims: 3 years from knowledge, max 10 years absolute
- If Art. 29(3) reporting omitted: absolute period extends to usage duration
- Criminal conduct: limitation not before criminal limitation
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class subsidy_claim_limitation_years(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Limitation period for subsidy claims (years)"
    reference = "SR 616.1 Art. 32 Abs. 1"

    def formula(person, period, parameters):
        return 5


class subsidy_refund_limitation_years(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Relative limitation period for subsidy refund claims from knowledge (years)"
    reference = "SR 616.1 Art. 32 Abs. 2"

    def formula(person, period, parameters):
        return 3


class subsidy_refund_absolute_limitation_years(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Absolute limitation period for subsidy refund claims (years)"
    reference = "SR 616.1 Art. 32 Abs. 2"

    def formula(person, period, parameters):
        return 10
