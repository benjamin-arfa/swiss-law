"""SR 0.142.116.909 Art. 10

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class take_back_individual(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Individual taken back under international extradition agreement (Art. 10 SR 0.142.116.909)"

    def formula(person, period, parameters):
        arrival_date = person("arrival_date", period)
        boarding_refusal = person("boarding_refusal", period)
        take_back_within_24_hrs = person("take_back_within_24_hrs", period)

        return boarding_refusal & boarding_refusal_date_leq_arrival & take_back_within_24_hrs

    boarding_refusal = parameters(period).extradition.boarding_refusal.checks.ensuing_step_count
    boarding_refusal_date_leq_arrival = (boarding_refusal * -1).date_leq(arrival_date)
    take_back_within_24_hrs = (-take_back_within_24_hrs).date_leq(self.period.last_day('P24D'))
