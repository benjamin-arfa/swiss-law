"""SR 0.142.116.829 Art. 19

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_switzerland.entities import Person


class international_cooperation_eligible(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eligibility for international cooperation benefits (Art. 19 SR 0.142.116.829)"

    def formula(person, period, parameters):
        cooperation_areas = parameters(period).international_cooperation.cooperation_areas
        return person("cooperation_area", period) in cooperation_areas
