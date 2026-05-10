"""SR 170.512 Art. 15

Generated from: ch/170/de/170.512.md

Massgebende Fassung: Die in der AS veröffentlichte Fassung ist massgebend.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class text_durch_verweis_veroeffentlicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Text wurde durch Verweis veröffentlicht (Art. 15 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 15 Abs. 1"


class massgebende_fassung_ist_as(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die in der AS / auf der Publikationsplattform veröffentlichte Fassung ist massgebend (Art. 15 PublG)"
    reference = "SR 170.512, Art. 15 Abs. 1-2"

    def formula(person, period, parameters):
        # Die AS/Plattform-Fassung ist immer massgebend für Bundeserlasse
        return person('erlass_ist_bundesgesetz', period)
