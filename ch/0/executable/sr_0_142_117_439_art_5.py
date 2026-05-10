"""SR 0.142.117.439 Art. 5

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class asylum_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Conditions preventing return under AHV Art. 5"

    def formula(person, period, parameters):
        has_valid_residence_permit = person("has_valid_foreign_residence_permit", period)
        has_foreign_residence_permit_after_entry = person("has_foreign_residence_permit_after_entry", period)
        shares_border_with_requesting_country = person("shares_border_with_requesting_country", period)
        has_refugee_status = person("has_refugee_status", period)
        has_international_protection = person("has_international_protection", period)
        is_asylum_seeker = person("is_asylum_seeker", period)
        has_departed_from_requesting_country = person("has_departed_from_requesting_country", period)
        has_reentered_requesting_country = person("has_reentered_requesting_country", period)
        return \
        (has_valid_residence_permit | has_foreign_residence_permit_after_entry | shares_border_with_requesting_country \
         | has_refugee_status | has_international_protection | is_asylum_seeker | has_departed_from_requesting_country & has_reentered_requesting_country)
