"""SR 744.21 Art. 8

Generated from: ch/744/de/744.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class verstoss_gegen_bundesgesetz_744_21(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss oder Anordnung des Unternehmens verstösst gegen SR 744.21"
    reference = "SR 744.21 Art. 8"


class verstoss_gegen_internationale_vereinbarungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss oder Anordnung des Unternehmens verstösst gegen internationale Vereinbarungen"
    reference = "SR 744.21 Art. 8"


class verletzung_wichtiger_landesinteressen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschluss oder Anordnung des Unternehmens verletzt wichtige Landesinteressen"
    reference = "SR 744.21 Art. 8"


class bav_aufhebungsbefugnis(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = (
        "BAV ist befugt, Beschlüsse oder Anordnungen von Organen oder Dienststellen "
        "des Unternehmens aufzuheben oder ihre Durchführung zu verhindern (SR 744.21 Art. 8)"
    )
    reference = "SR 744.21 Art. 8"

    def formula(person, period, parameters):
        verstoss_gesetz = person("verstoss_gegen_bundesgesetz_744_21", period)
        verstoss_international = person("verstoss_gegen_internationale_vereinbarungen", period)
        verletzung_landesinteressen = person("verletzung_wichtiger_landesinteressen", period)
        return verstoss_gesetz + verstoss_international + verletzung_landesinteressen
