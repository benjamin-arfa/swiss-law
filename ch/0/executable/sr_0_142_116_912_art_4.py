"""SR 0.142.116.912 Art. 4

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class visa_exemption(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Visa exemption for foreigners working at diplomatic missions or international organizations (Art. 4 SR 0.142.116.912)"

    def formula(person, period, parameters):
        official_notification = person("official_notification", period)
        valid_passport = person("valid_passport", period)
        diplomatic_emp = parameters(period).social_security.international.works_at_diplo_or_international_org

        return (official_notification & valid_passport) & diplomatic_emp
