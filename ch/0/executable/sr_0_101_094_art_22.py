"""SR 0.101.094 Art. 22

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class NotificationDateVariable(Variable):
    value_type = date
    default_value = date(1900, 1, 1)
    label = u"Notification date of the Europarat protocol"
    entity = Person
    definition_period = D
    reference = "SR 0.101.094 Art. 22"
    display_with = "person(date)"

    def formula(person, period, parameters):
        # Assume we need the protocol notification date
        protocol_notification_date = parameters(period).protocol_notification_date
        return protocol_notification_date
