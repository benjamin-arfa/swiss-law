"""SR 0.142.116.919 Art. 21

Generated from: ch/0/de/0.142.116.919.md
"""

Here's a hypothetical implementation of a variable within OpenFisca focused on repatriation and onward transfer:
from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class return_protocol_notification(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Notification about the protocol for the implementation of this agreement"

    def formula(person, period, parameters):
        last_notification = person("last_protocol_notification", period)
        next_notification_threshold = parameters(period).return_protocol.protocol_notification_threshold
        return (period.date - last_notification) > next_notification_threshold
Note: Please note this is a hypothetical adaptation for educational purposes, as the original article is related to an international agreement and its implementation might not fit directly into the OpenFisca framework without significant context and adjustments.
