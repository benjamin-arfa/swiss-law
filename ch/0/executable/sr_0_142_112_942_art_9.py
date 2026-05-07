"""SR 0.142.112.942 Art. 9

Generated from: ch/0/de/0.142.112.942.md
"""

from openfisca_core.model_api import *
from openfisca_core import events


class notification_date_notif(
    events.Event
):
    """
    Notification sent by one (or both) parties.
    """
    definition_period = MONTH
    process_args = {"generate_method": "last_notification_date"}  # last 30 day


class agreement_effective_date_notif(
    events.Event
    ):
    definition_period = MONTH
    process_args = {
        "match": "after",
        "days": 30  # Activation date of the agreement change
    }
