"""SR 0.104 Art. 19

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_entry_into_force(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Entry into force of the treaty (Art. 19 SR 0.104)"

    def formula(countries, period, parameters):
        deposit_count = parameters(period).international_agreements.treaty_entry_into_force.deposit_count
        thirty_days_after_deposit = (parameters(period).date - 30).date

        global_entry_into_force = deposit_count == 27
        individual_entry_into_force = countries("deposit_date", period) >= thirty_days_after_deposit

        return global_entry_into_force | individual_entry_into_force
