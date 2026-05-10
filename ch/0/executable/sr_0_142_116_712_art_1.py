"""SR 0.142.116.712 Art. 1

Generated from: ch/0/de/0.142.116.712.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class accredited_diplomatic_residency(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Residency for accredited diplomatic and consular staff (Art. 1 SR 0 142 115 712)"

    def formula(person, period, parameters):
        dipomat_passported = person("has_diplomatic_passport", period)
        eligible_country = person("citizenship") == parameters(period).globalisation.eligible_country_for_diplomatic_residency
        notified_by_host = person("notified_residency_status", period)
        return dipomat_passported & eligible_country & notified_by_host

class family_member_residency(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Residency for accredited diplomatic and consular staff family members (Art. 1 SR 0 142 115 712)"

    def formula(person, period, parameters):
        dipomat_passported = person("has_diplomatic_passport", period)
        eligible_country = person("citizenship") == parameters(period).globalisation.eligible_country_for_diplomatic_residency
        notified_by_host = person("notified_residency_status", period)
        co_resident_family_member = person("family_member_of_eligible_diplomat", period)
        return dipomat_passported & eligible_country & notified_by_host & co_resident_family_member
