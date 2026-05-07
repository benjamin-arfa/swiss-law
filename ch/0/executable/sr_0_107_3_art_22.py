"""SR 0.107.3 Art. 22

Generated from: ch/0/de/0.107.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import EventVariable


class terminated_convention(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Termination of the European Social Charter Convention (Art. 22)"

    def formula(countries, period, parameters):
        notification_events = countries.any("terminate_convention_notification", period)

        effective_termination_date = (notification_events.first_step.date + relativedelta(months=12))

        is_after_notification = countries("is_after_notification", period, lookup="within_period")
        is_beyond_effective_term_date = countries("is_beyond_effective_term_date", period, lookup="within_period")

        return is_beyond_effective_term_date

class is_after_notification(EventVariable):
    value_type = bool
    reference = "notification_events"

    def formula(countries, period, parameters):
        return countries("notification_events", period)

class is_beyond_effective_term_date(EventVariable):
    value_type = bool
    reference = "notification_events"

    def formula(countries, period, parameters):
        notification_events = countries("notification_events", period)
        is_beyond_effective_term_date = (countries("effective_termination_date", period) > period.date)
        return is_beyond_effective_term_date


class notification_events(EventVariable):
    value_type = bool
    description: Event type for country notification for terminating its terms.

    def formula(country, period, parameters):
        effective_termination_date = country("effective_termination_date", period)
        return country("terminate_convention_notification", period)

class terminate_convention_notification(EventVariable):
    value_type = bool
    reference = "termination_date"

    def formula(country, period, parameters):
        effective_termination_date = country("effective_termination_date", period)
        return country("termination_date") > 0
