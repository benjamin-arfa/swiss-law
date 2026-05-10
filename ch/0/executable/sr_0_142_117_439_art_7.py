"""SR 0.142.117.439 Art. 7

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class re_admitted_30_days_later(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Was the individual re-admitted 30 days later under the specific agreement?"

    def formula(person, period, parameters):
        previous_period = personeriod.period_lag(MONTH)
        previous_re_admission_date = person("previous_re_admission_date", previous_period)
        current_period_start_date = period.start_date

        days_between_events = (current_period_start_date - previous_re_admission_date).days

        return days_between_events <= 30
