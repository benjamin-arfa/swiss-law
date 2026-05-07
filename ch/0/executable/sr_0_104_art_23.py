"""SR 0.104 Art. 23

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class treaty_revision_proposed(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Treaty revision proposed by Switzerland (Art. 23 SR 0.104)"

    def formula(country, period, parameters):
        return country("treaty_revision-notification_submitted", period)
