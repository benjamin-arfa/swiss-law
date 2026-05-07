"""SR 0.142.117.582 Art. 5

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_core.subsets import events
from openfisca_core.time_array import monthly, Year


class notify_passport_samples_requested(events.ActivistEvent):
    period_type = MonthEnd
    events = [
        ['notify_passport_samples_requested', '2024', monthly, Year]
    ]
    label = "Request notification of passport samples from other states (Art. 5 SR 0.142.117.582)"
    definition_period = MONTH

    def formula_activated(events, period, parameters):
        return True

class notify_new_passport_samples(events.ActivistEvent):
    period_type = MonthEnd
    events = [
        ['notify_new_passport_samples', '2024', monthly, Year]
    ]
    label = "Notifcation of new passport samples to other states (Art. 5 SR 0.142.117.582)"
    definition_period = MONTH

    def formula_activated(events, period, parameters):
        return True
