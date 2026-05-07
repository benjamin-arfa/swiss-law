"""SR 531.211.36 Art. 4

Generated from: ch/531/de/531.211.36.md
Contract adjustment: Before removing goods from the mandatory stockpile,
the stockpile contract with the BWL must be adjusted.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class stockpile_contract_adjustment_required(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Whether stockpile contract with BWL must be adjusted before withdrawal"
    reference = "SR 531.211.36 Art. 4"

    def formula(person, period, parameters):
        # Contract adjustment is always required before removal
        return person("intends_to_withdraw_from_stockpile", period)
