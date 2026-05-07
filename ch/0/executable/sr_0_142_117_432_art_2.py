"""SR 0.142.117.432 Art. 2

Generated from: ch/0/de/0.142.117.432.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class exempt_from_visa(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Exemption from the visa requirement (Art. 2 SR 0.142.117.432)"

    def formula(person, period, parameters):
        has_valid_pass = person("has_valid_diplomatic_pass", period)
        is_diplomat_or_representative = person("is_diplomat_or_representative", period)
        is_family_member = person("is_family_member_of_diplomat_or_representative", period)

        return (
            (has_valid_pass & (is_diplomat_or_representative | is_family_member))
            | has_valid_pass
        )
