"""SR 0.142.112.632.2 Art. 7

Generated from: ch/0/de/0.142.112.632.2.md
"""

from openfisca_core.model_api import *

class passport_notification(Variable):
    value_type = bool
    label = "Notification of passport documents (Art. 7 SR 0.142.112.632.2)"

    def formula(self, period):
        # placeholder formula
        return True
