"""SR 0.142.116.909 Art. 6

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transportation_expenses(Variable):
    value_type = int
    entity = None
    definition_period = YEAR
    label = "Expenses for transporting third-state nationals (Art. 6 SR 0.142.116.909)"

    def formula(_):
        # No formula specified, as details would depend on specific agreements or context
        def transport_expense_rule(period, parameters):
            return 1000  # Example value, would replace with relevant data
            
        return transport_expense_rule(_)
