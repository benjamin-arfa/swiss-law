"""SR 0.142.116.659 Art. 6

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class requires_residence_return_request(Variable):
    value_type = bool
    entity = Person
    label = "Should a residence return request be made under Art. 6 (SR 0.142.116.659)"

    def formula(person, period, parameters):
        # condition: does the person NOT require a request to be made?
        national_passport = person("holds_valid_national_passport", period)
        is_foreign_national_or_stateless = person("is_foreign_national_or_stateless", period)

        return (is_foreign_national_or_stateless & national_passport) or (not is_foreign_national_or_stateless & not national_passport)
