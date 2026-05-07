"""SR 0.191.02 Art. 50

Generated from: ch/0/de/0.191.02.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person

class customs_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Customs exemption for consular post and personnel (Art. 50 CDE)

    def formula(person, period, parameters):
        is_consular_official = person("is_consular_official", period)
        is_household_member = person("is_household_member", period)
        good_for_exemption = person("good_for_exemption", period)
        quantity_within_limit = person("quantity_within_limit", period)

        return (is_consular_official | is_household_member) & good_for_exemption & quantity_within_limit
