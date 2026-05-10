"""SR 0.142.116.712 Art. 5

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class passport_template_notification(Variable):
    value_type = bool
    entity = Country
    definition_period = MONTH
    label = "Notification of new passport template (Art. 5, Abkommen)"

    def formula(country, period, parameters):
        sending_date = country("passports_sending_date", period)
        introduction_date = country("passport_introduction_date", period)
        notification_interval = (introduction_date - sending_date).days
        introduction_window = 30

        return before(introduction_window, notification_interval)
