"""SR 0.142.111.638.1 Art. 1

Generated from: ch/0/de/0.142.111.638.1.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class exemption_from_residence_permit(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Exemption from residence permit for Austrian/Swiss citizens (Art. 1 SR 0.142.111.638.1)"

    def formula(person, period, parameters):
        is_austrian_or_swiss_citizen = person("is_austrian_or_swiss_citizen", period)
        gainful_employment_in_host_country = person("gainful_employment_in_host_country", period)
        temporary_stay_length = 3
        return is_austrian_or_swiss_citizen & ~gainful_employment_in_host_country & (period.duration == temporary_stay_length)
