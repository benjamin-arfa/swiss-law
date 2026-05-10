"""SR 170.512 Art. 8

Generated from: ch/170/de/170.512.md

Rechtswirkungen der Veröffentlichung: Rechtspflichten entstehen erst mit
der Veröffentlichung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class erlass_ist_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Erlass wurde ordnungsgemäss veröffentlicht (Art. 8 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 8 Abs. 1"


class erlass_nach_inkrafttreten_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Erlass wurde erst nach dem Inkrafttreten veröffentlicht (Art. 8 Abs. 2 PublG)"
    reference = "SR 170.512, Art. 8 Abs. 2"


class rechtspflichten_entstanden(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rechtspflichten aus dem Erlass sind entstanden (Art. 8 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 8 Abs. 1"

    def formula(person, period, parameters):
        return person('erlass_ist_veroeffentlicht', period)


class nachweis_unkenntnis_moeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachweis möglich, dass Erlass nicht gekannt und nicht kennen konnte (Art. 8 Abs. 3 PublG)"
    reference = "SR 170.512, Art. 8 Abs. 3"

    def formula(person, period, parameters):
        plattform_down = person('publikationsplattform_nicht_zugaenglich', period)
        return plattform_down
