"""SR 744.10 Art. 12

Generated from: ch/744/de/744.10.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bav_zustaendig_verfolgung_art11_verstoss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das BAV ist zuständig für die Verfolgung und Beurteilung von Verstössen gegen Art. 11 (SR 744.10 Art. 12 Abs. 1)"
    reference = "SR 744.10 Art. 12 Abs. 1"

    def formula(person, period, parameters):
        return person('verstoss_gegen_art11_sr74410', period)


class verfahren_nach_verwaltungsstrafrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Verfahren richtet sich nach dem Bundesgesetz über das Verwaltungsstrafrecht (SR 313.0) (SR 744.10 Art. 12 Abs. 2)"
    reference = "SR 744.10 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        return person('bav_zustaendig_verfolgung_art11_verstoss', period)


class verstoss_gegen_art11_sr74410(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Person hat gegen Artikel 11 SR 744.10 verstossen"
    reference = "SR 744.10 Art. 11"

    def formula(person, period, parameters):
        return person('verstoss_gegen_art11_sr74410', period)
