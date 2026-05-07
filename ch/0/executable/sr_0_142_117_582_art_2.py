"""SR 0.142.117.582 Art. 2

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class schengen_stay_eligibility(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Eligibility for a visa-free stay in the other country (Article 2 of the Schengen Association Agreement)"

    def formula(person, period, parameters):
        has_diplomatic_passport = person("has_diplomatic_passport", period)
        has_valid_national_special_passport = person("has_valid_national_special_passport", period)
        is_swiss_citizen = person("is_swiss_citizen", period)
        is_eu_citizen = person("is_eu_citizen", period)

        has_right_to_free_movement = (has_diplomatic_passport | has_valid_national_special_passport)
        or_eu/right = (is_eu_citizen | (not is_swiss_citizen & is_eu_citizen))
        eligible_nationality = has_right_to_free_movement | or_eu/right

        has_been_outside_country_long_enough = (period.date > person("last_exit_date", period))
        was_outside_schengen_region = person("last_entry_date", period) < person("exit_date_from_schengen", period)
        schengen_residency_date = person("schengen_residency_date", period)
        entry_date_after_schengen_residency = person("entry_date_after_schengen_residency", period)

        was_outside_schengen_region_before_sch residency = (schengen_residency_date > person("last_exit_date", period))
        entry_date_before_schengen_residency = period.date >= entry_date_after_schengen_residency
        new_residency_start = (entry_date_before_schengen_residency & was_outside_schengen_region_before_sch residency)
        schengen_count_reset = (new_residency_start | (entry_date_after_schengen_residency <= was_outside_schengen_region_before_sch residency))

        is_eligible = (schengen_count_reset & (eligible_nationality | entry_date_after_schengen_residency))

        return is_eligible
