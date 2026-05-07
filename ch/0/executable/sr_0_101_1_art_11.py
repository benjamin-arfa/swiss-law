"""SR 0.101.1 Art. 11

Generated from: ch/0/de/0.101.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR

from openfisca-country import Variable

class notification_deposit(Variable):
    value_type = int
    entity = Person
    label = "Deposit of an instrument of ratification"
    definition_period = YEAR

    def formula(person, period, parameters):
        # Define a parameter for the deposit of an instrument of ratification
        contract_deposit = parameters(period).contract_deposit
        
        # Create a boolean variable for each type of notification
        deposit_bool = person("deposit_contract", period) > 0
        return deposit_bool * contract_deposit
