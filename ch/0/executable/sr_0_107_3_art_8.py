"""SR 0.107.3 Art. 8

Generated from: ch/0/de/0.107.3.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Country


class article_8_protocol_application(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Application of Art. 8 protocol on message transmission (SR 0.107.3 Art. 8)"

    def formula(countries, period, parameters):
        current_year = period.start.year
        return (current_year >= 2024) & c('country').('has_signed_protocol', period)
