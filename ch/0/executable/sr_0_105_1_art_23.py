"""SR 0.105.1 Art. 23

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class publish_prevention_reports(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Annual reports of national prevention mechanisms published (Art. 23 SR 0.105.1)"

    def formula(country, period, parameters):
        return True
