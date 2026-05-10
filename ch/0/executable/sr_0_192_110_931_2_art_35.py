"""SR 0.192.110.931.2 Art. 35

Generated from: ch/0/de/0.192.110.931.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class convention_entry_into_force(Variable):
    value_type = date
    entity = Country
    definition_period = MONTH
    label = "Entry into force date of the convention (Art. 35 SR 0.192.110.931.2)"

    def formula(country, period, parameters):
        deposits_dates = country("deposit_date", period)
        deposits = parameters(period).convention.deposits
        deposit_number = country("deposit_rank", period, parameters)

        entry_into_force = deposits_dates[deposit_number] + MONTH if deposit_number == 10 else (None if deposit_number < 10 else deposits_dates[deposit_number] + (MAX(deposits_dates) - deposits_dates[deposit_number])) + MONTH

        return entry_into_force
