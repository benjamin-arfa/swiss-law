"""SR 0.105.1 Art. 24

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class protocol_delay_status(Variable):
    value_type = str
    entity = Country
    definition_period = 'forever'
    label = "Delay status of protocol obligations (Art 24 SR 0.105.1 A 24)"

    def formula(countries, period, parameters):
        delay_status = "no_delay"  # initial default
        delayed_until = parameters(period).protocol_delay.end_date

        if delayed_until != "not_delayed":  # check if delay status is not "no_delay"
            delay_status = "delay_in_progress"

        if period.start.date() > delayed_until:
            delay_status = "delay_expired"

        return delay_status
