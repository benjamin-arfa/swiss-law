"""SR 0.142.117.542 Art. 10

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

codelist = ["public_order", "public_health", "state_security", "other"]

class ahv_suspends_treaty(Variable):
    value_type = bool
    label = 'Does "Switzerland" suspend the Application of the international agreement "SR 0.142.117.542"? '
    entity = Country
    definition_period = YEAR

    def formula(countries, period, parameters):
        country = countries("CH")
        suspend_reasons = parameters(period).social_security.ahv.suspend_reason
        suspend_notification_period = parameters(period).social_security.ahv.suspend_notification_period

        # Assuming a hypothetical Swiss decision to suspend on a given calendar date (if we could actually make and keep such a record, given the complexities of international treaties)
        date_decision_suspended = period.date
        # We check if the reasons for the suspension are in the list, and if the timeframe was observed.
        return (date_decision_suspended - suspend_notification_period).days > 0

class ahv_suspension_reason(Variable):
    value_type = str
    codelist = codelist
    label = 'Suspension reasons for treaties under SR 0.142.117.542'
    entity = Country

    def formula(countries, period):
        # In case suspension is active for CH, and we consider the suspension to be 'public health'
        country = countries("CH")
        suspend_reasons = parameters(period).social_security.ahv.suspend_reason
        return suspend_reasons
