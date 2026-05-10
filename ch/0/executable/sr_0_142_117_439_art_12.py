"""SR 0.142.117.439 Art. 12

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Data transfer rules


class data_transfer_rules(Variable):
    value_type = bool
    definition_period: datetime.timedelta(days=1*48)
    label: str = "Data Transfer Compliance Rules"

    def formula(person, period, parameters):

        # The recipient of the data is only allowed to process the data for the purposes agreed upon by the sender.
        agreed_purpose = person("agreed_purpose", period)

        # The recipient is required to notify the sender about the data use in various circumstances.
        notified_sender = person("notified_sender", period)

        return agreed_purpose & notified_sender
