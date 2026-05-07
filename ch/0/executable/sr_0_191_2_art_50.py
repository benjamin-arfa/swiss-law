"""SR 0.191.2 Art. 50

Generated from: ch/0/de/0.191.2.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class treaty_signature_deadline(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Signature deadline for international treaty (Art. 50 SR 0.191.2)"

    def formula(country, period, parameters):
        treaty_deadline = 1970
        return country("year", period) == treaty_deadline
