"""SR 0.142.116.712 Art. 2

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from dataclasses import dataclass




@dataclass
class Stay(Month):
    max_allowed_days: int = 90
    max_allowed_period_days: int = 180

    def is_overstayed(self) -> bool:
        total_days = self.max_days()
        return total_days > self.max_allowed_days


class non_schengen_eea_travel_days(Variable):
    value_type = columns_module.DayOrPeriodTime
    entity = Person
    definition_period = YEAR
    label = "Days living in an EEA country without Schengen visa"

    def formula(person, period, parameters):
        entry_date = person("first_entry_date_in_eea_country", period)
        exit_date = person("last_exit_date_from_eea_country", period)
        if entry_date is None:
            return 0
        time_period = entry_date + period
        if exit_date is None:
            return time_period - person("birth_date", period)
        return exit_date - entry_date if exit_date < time_period else 0

class schengen_eea_travel_days(Variable):
    value_type = columns_module.DayOrPeriodTime
    entity = Person
    definition_period = YEAR
    label = "Days traveled through the Schengen/EEA zone"

    def formula(person, period, parameters):
        entry_date = person("border_day_after_eea_schengen_zone", period)
        trip_start = max(person("first_entry_date_in_schengen_country", period), entry_date)
        exit_date = person("date_of_border_crossing_after_schengen_eea", period)
        if entry_date is None:
            return 0
        stay = Stay(entry_date, exit_date)
        stay_days = stay.days
        return stay_days

class max_stay_period_from_article(Variable):
    value_type = Stay
    entity = Person
    definition_period = YEAR
    label = "90 days period (art 2 180 day periode)"

    def formula(age_period, period, parameters):
        return Stay(90, 180)
