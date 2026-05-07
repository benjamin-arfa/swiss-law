"""SR 616.1 Art. 14

Generated from: ch/616/de/616.1.md
Eligible expenses: Only actually incurred expenses that are absolutely necessary
for proper task fulfilment are eligible. Capital interest on buildings is not eligible.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class eligible_subsidy_expenses(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Eligible expenses for subsidy calculation (CHF)"
    reference = "SR 616.1 Art. 14"

    def formula(person, period, parameters):
        total_expenses = person("total_task_expenses", period)
        capital_interest = person("capital_interest_on_buildings", period)
        non_essential = person("non_essential_expenses", period)
        # Only actually incurred and absolutely necessary expenses
        # Capital interest on buildings is explicitly excluded
        return max_(total_expenses - capital_interest - non_essential, 0)
