"""SR 0.101.09 Art. 4

Generated from: ch/0/de/0.101.09.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ProtocolEntryIntoForce(variables.Variable):
    label = "Protocol entry into force"
    definition_period = "P1Y"
    default_value = -1  # to indicate no entry into force

    def formula_2020_01_01(awg, period, parameters):
        all_contracts_agreed_on = awg(parameters.period('2020-01-01').start_date, "2020-01-01", "all_contracts_agreed")
        return awg(
            parameters.period(period.start_date.add_months(1, period.start_date.year % 12)), 
            "ProtocolEntryIntoForce"
        ) if all_contracts_agreed_on(period.start_date, "2020-01-01") else -1
