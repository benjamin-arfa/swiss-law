"""SR 0.101.094 Art. 15

Generated from: ch/0/de/0.101.094.md
"""

from sympy import symbols
from openfisca_core import periods

# Define the variable amicable_settlement_status as a dummy for what to do
class AmicableSettlementStatus(Variable):
    value_type = symbols.Boolean

    def formula(person, period, parameters):
        # Add the concrete logic here to determine the settlement status,
        # this part can use parameters and existing defined variables
        # (currently available_variables is empty and no specific rates or thresholds are mentioned)
        return True

    def default_period():
        return periods.ALL

    def default_value(period):
        return False
