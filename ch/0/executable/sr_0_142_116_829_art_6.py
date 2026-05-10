"""SR 0.142.116.829 Art. 6

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_return_application_required(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AHV return application required (Art. 6)"

    def formula(person, period, parameters):
        has_ch_passport = person("has_ch_national_passport", period)
        nationality = person("country_of_nationality", period)

        has_valid_visa_or_residence = (person.exists("has_valid_non_Ch_visum", period) | person.exists("has_valid_non_CH_residence_permit", period))

        return has_ch_passport & ((nationality == parameters(period).socioeconomic.non_ch_nationality) | has_valid_visa_or_residence)
