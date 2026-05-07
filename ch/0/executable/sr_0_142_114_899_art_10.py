"""SR 0.142.114.899 Art. 10

Generated from: ch/0/de/0.142.114.899.md
"""

from openfisca_core.model_api import *
from openfisca_core.variables import Variable
from openfisca_country_template.entities import Country


class international_commitments(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Country's international human rights commitments (Art. 10)"]

    def formula(countries, period, parameters):
        return True
