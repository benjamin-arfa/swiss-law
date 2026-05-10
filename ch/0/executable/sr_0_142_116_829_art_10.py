"""SR 0.142.116.829 Art. 10

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class asylum_return_request_deadline(Variable):
    value_type = date
    entity = Government
    definition_period = DAY
    label = "Asylum return request deadline (Art. 10 SR 0.142.116.829)"

    def formula(government, period, parameters):

        first_notification = government("first_asylum_return_request_notification_date", period)
        last_notification = government("last_asylum_return_request_notification_date", period)
        initial_deadline = first_notification + Duration(days=365)

        return initial_deadline

class asylum_request_answer_deadline(Variable):
    value_type = date
    entity = Government
    definition_period = DAY
    label = "Asylum request answer deadline (Art. 10 SR 0.142.116.829)"

    def formula(government, period, parameters):
        initial_deadline = government("asylum_request_received_date", period) + Duration(days=15)
        return initial_deadline

class asylum_return_deadline_extension(Variable):
    value_type = int
    entity = Government
    definition_period = DAY
    label = "Extend asylum return deadline by (Art. 10 SR 0.142.116.829)"

    def formula(government, period, parameters):
        initial_extension_request = government("initial_asylum_return_deadline_extension_request_date", period)
        if initial_extension_request == period.start_date:
            return 6
