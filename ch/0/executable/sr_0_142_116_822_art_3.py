"""SR 0.142.116.822 Art. 3

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_schengen_country(Variable):
    value_type = bool
    label = "Whether a country is a Schengen country (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        return instance("is_schengen_country", period)

class is_swiss_citizen(Variable):
    value_type = bool
    label = "Whether a person is a Swiss citizen (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        return instance("is_swiss_citizen", period)

class national_of_serbia(Variable):
    value_type = bool
    label = "Whether a person is a Serbian citizen (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        return instance("is_national_of_serbia", period)

class residence_status(Variable):
    value_type = bool
    label = "Whether a person resides lawfully (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        is_srb_citizen = instance.national_of_serbia(period)
        has_authorization = instance("has_authorization_to_reside", period)
        is_resident_lawfully = is_srb_citizen & has_authorization
        return is_resident_lawfully

class is_visum_required(Variable):
    value_type = bool
    label = "Whether a visa is required for entry (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        is_resident_lawfully = instance.residence_status(period)
        has_permit_to_reside_for_more_than_90_days = instance("has_permit_to_reside_for_more_than_90_days", period)
        is_visum_required = (~is_resident_lawfully) & has_permit_to_reside_for_more_than_90_days
        return is_visum_required

class has_authorization_to_reside(Variable):
    value_type = bool
    label = "Whether a person has authorization to reside (Art. 3 SR 0.142.116.822)"

    def formula(instance, period, parameters):
        permitted_stay = instance("permitted_stay", period)
        is_stay_permitted_for_less_than_90_days = (permitted_stay <= 90)
        has_authorization_to_reside = ~is_stay_permitted_for_less_than_90_days
        return has_authorization_to_reside
