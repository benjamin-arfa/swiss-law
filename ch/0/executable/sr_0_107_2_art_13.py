"""SR 0.107.2 Art. 13

Generated from: ch/0/de/0.107.2.md
"""

from openfisca_core.model_api import *

class ahv_country_status(Variable):
    value_type = bool
    label = "Status regarding AHV/IV/EO for the country of residence (not possible to automatically implement)"

    def formula(person, period, parameters):
        return False  # Not possible to automatically implement
