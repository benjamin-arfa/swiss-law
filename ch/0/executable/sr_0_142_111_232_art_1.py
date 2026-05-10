"""SR 0.142.111.232 Art. 1

Generated from: ch/0/de/0.142.111.232.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class exempt_visa_required(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Exemption from visa requirements for diplomatic missions (Art. 1 SR 0.142.111.232)"

    def formula(person, period, parameters):
        is_diplomatic_passport = person("diplomatic_passport", period)
        is_official_mission = person("official_mission", period)
        host_country = person("host_country", period)

        notification_status = person("previous_notification", period)

        is_family_member = person("family_member", period)
        family_passport = person("family_member_passport", period)

        return ((is_diplomatic_passport & is_official_mission & (host_country in parameters(period).foreign_relations.partner_countries)) & notification_status) | (is_family_member & family_passport & (host_country in parameters(period).foreign_relations.partner_countries))
