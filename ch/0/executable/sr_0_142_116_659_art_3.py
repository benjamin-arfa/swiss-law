"""SR 0.142.116.659 Art. 3

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taken_back_russia(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person taken back by Russia (Art. 3, Bilateral Agreement)"

    def formula(person, period, parameters):
        country_entry = person("country_entry", period)
        visa_status = person("visa_status", period)
        residence_permit = person("residence_permit", period)
        asylum_status_russia = person("asylum_status_in_russia", period)

        conditions = [
            (country_entry == "Russia") & (visa_status == "valid") & ("entered_directly", person("country_entry_mode", period)),
            (country_entry != "Russia") | ((visa_status == "valid") & (residence_permit == "valid")),
            (country_entry == "Russia") & ("enter_without_visa", person("country_entry_mode", period)),
            (asylum_status_in_russia == "asylum_seeker") & (visa_status == "none")
        ]

        # exceptions to be added
        exception1 = (person("transit_through_airport", period))
        exception2 = (person("switzerland_visa", period))
        exception3 = (person("visa_free_access", period))
        return any(conditions) & ~((exception1 | exception2) & ~exception3)
        # add the visa exception specific to Russia
