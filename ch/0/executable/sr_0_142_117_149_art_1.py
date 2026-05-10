"""SR 0.142.117.149 Art. 1

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class third_country_national(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Third-country national (SR 0.142.117.149 Art. 1)"

    def formula(person, period, parameters):
        nationality_list = parameters(period).general.nationality.swiss.value | parameters(period).general.nationality.swedish.value
        return not person("nationality_list", period) & sum([person("citizenship.status", time_period="today") == status for status in ["Swiss", "Swedish", "third-country national"]])


class resident_permit(Variable):
    value_type = str
    entity = Person
    definition_period = DAY
    label = "Resident permit (SR 0.142.117.149 Art. 1)"

    def formula(person, period, parameters):
        return person("visum.type", period)
