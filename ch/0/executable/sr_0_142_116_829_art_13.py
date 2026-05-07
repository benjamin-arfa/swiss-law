"""SR 0.142.116.829 Art. 13

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class stc_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MAX
    label = "Safe third country eligibility (Art. 13)"

    def formula(person, period, parameters):
        current_location = person("current_location", period)

        is_third_country = person("is_third_country_national", period) | person("is Stateless", period)
        is_return_or_continuing = (is_third_country) & person("is_returning_from_third_country", period) | person("has_continued_through_third_country", period)
        third_country_location = person("third_country_location", period)

        is_return_not_impossible = third_country_location != "unreachable"
        is_return_or_continuing_not_forbidden = (
          # Protection
          not (third_country_location == "risky_torture") & 
          not (third_country_location == "risky_cruel_inhuman_degrading_punishment") & 
          not (third_country_location == "risky_death_penalty") & 
          not (third_country_location == "risky_persecution"),
          # Prosecution history
          not (third_country_location == "risky_prosecution"),
          # Public order concerns
          not (third_country_location == "risky_public_health") & 
          not (third_country_location == "risky_internal_security") & 
          not (third_country_location == "risky_public_order") & 
          not (third_country_location == "risky_national_interests")) & 
        is_return_not_impossible

        return (current_location == "requested_state") | (is_return_or_continuing_not_forbidden)
