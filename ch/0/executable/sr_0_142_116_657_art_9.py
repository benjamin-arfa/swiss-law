"""SR 0.142.116.657 Art. 9

Generated from: ch/0/de/0.142.116.657.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class contract_period(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Contract duration and termination notice period (Art. 9 SR 0.142.116.657)"

    def formula(person, period, parameters):
        contract_start = person("contract_start", period)
        contract_end = person("contract_end", period)
        termination_notice_period = parameters(period).contract_details.termination_notice_period
        termination_date = person("termination_date", period)
        
        # This is very basic example. You will probably have a more complex calculation here.
        if period.index == 0:
            return contract_end - contract_start
        else:
            return abs(contract_end - termination_date) if termination_date else 0
