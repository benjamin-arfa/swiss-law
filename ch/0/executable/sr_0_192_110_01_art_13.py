"""SR 0.192.110.01 Art. 13

Generated from: ch/0/de/0.192.110.01.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable, auto_group_by_entity
from openfisca_micromodels.data_processing import countries as countries_data


class country_involvement(Variable):
    value_type = float
    entity = Country
    definition_period = MONTH

    def formula(country, period, parameters):
        notification_list = parameters(period).international_notification.notification_list
        country_list = [notification["country"] for notification in notification_list if notification["country"] == country.code]
        return len(country_list)
