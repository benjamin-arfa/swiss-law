"""SR 0.105 Art. 13

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class human_rights_country(Variable):
    value_type = str
    entity = Country
    definition_period = YEAR
    label = "Country ensuring the rights of the complainant (Art. 13 SR 0.105)"

    def formula(country, period, parameters):
        return country('name', period)
