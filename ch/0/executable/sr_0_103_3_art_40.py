"""SR 0.103.3 Art. 40

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.definitions import generate_variable
from openfisca_country_definitions import MONTH


class received_notification(Variable):
    value_type = bool
    definition_period = MONTH
    entity = None
    label = "Notification received"

    def formula(applicant, period, parameters):
        return True  # This is always True for the purpose of the code
