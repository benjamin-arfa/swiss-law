"""SR 0.142.116.909 Art. 5

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_exempt_transfer_obligation(Variable):
    value_type = bool
    entity = Person
    definition_period = PERIOD
    label = "Exemption from transfer obligation (Art. 5 SR 0.142.116.909)"

    def formula(person, period, parameters):
        visa = person("has_valid_travel_document", period)
        entry_age = person("age_at_entry", period)

        is_eu_country = person("country_of_residence", period) == "EU"
        is_bordering_sovereign_state = person("country_of_residence", period) == "CH"
        is_fleeing_person = (person("recognized_as_refugee", period) & person("valid_refugee_status", period))
        deportation_decision = person("has_deportation_decision", period)
        transit_visa = person("has_transit_visa", period)

        time_since_entry = (period.start.date - person("date_of_entry", period)).days / 365.25

        return (visa | (entry_age < 12)) | \
               ((isin_ch_bordering_country() | deportation_decision) | \
               is_eu_country | is_bordering_sovereign_state | is_fleeing_person | \
               (time_since_entry > 1))

# Assuming the necessary functions and variables from the available_variables
