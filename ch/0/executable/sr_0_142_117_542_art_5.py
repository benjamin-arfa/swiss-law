"""SR 0.142.117.542 Art. 5

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person, Authority


class can_send_notification(AuthorityStatus)
    domain = AuthorityRoles


class send_notification(Variable):
    value_type = bool
    def formula(authority, period, parameters):
        sender = authority("sender", period)
        recipient = authority("recipient", period)
        notification_date = authority("notification_date", period)
        notification_description = authority("notification_description", period)

        sender_can_send_notification = sender.has_role(can_send_notification(domain))
        has_required_info = sender["sender_exists"] & recipient["recipient_exists"] & notification_date["exists"] & notification_description["exists"]

        return sender_can_send_notification & has_required_info
