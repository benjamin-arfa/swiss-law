"""SR 0.142.113.498 Art. 1

Generated from: ch/0/de/0.142.113.498.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class small_border_traffic(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Arbeitskräfte im kleinen Grenzverkehr (Art. 1 SR 0.142.113.498)"

    def formula(person, period, parameters):
        return (person("is_swiss", period) | person("is_french", period)) &
               (person("resident_in_border_zone_switzerland", period) | person("resident_in_border_zone_france", period)) &
               person("daily_commutes", period) &
               person("works_in_neighbor_country", period)
