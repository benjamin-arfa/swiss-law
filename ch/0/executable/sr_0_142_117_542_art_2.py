"""SR 0.142.117.542 Art. 2

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class schengen_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Exemption from Schengen visa requirements (Art. 2 Schengen Agreement)"

    def formula(person, period, parameters):
        is_citizen = person("is_citizen_of_eu_switzerland", period)
        has_valid_passport = person("has_diplomatic_official_passport", period)
        is_resident = person("resides_in_host_country", period)
        has_employment = person("has_gainful_employment_in_host_country", period)
        days_stayed = person("days_stayed_in_host_country", period)
        total_days = person("total_days_visited_host_country", period)
        stay_limit_passed = total_days // 180 * 180 <= total_days

        return (is_citizen | has_valid_passport) & not is_resident and not has_employment and (days_stayed < 90 or stay_limit_passed)
