"""SR 455.110.2 Art. 12

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class grundlaermpegel_dezibel(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Grundlaermpegel im Zutriebsbereich in Dezibel"
    reference = "SR 455.110.2 Art. 12"


class laermpegel_zutrieb_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Grundlaermpegel im Zutriebsbereich konform (max 85 dB) nach Art. 12 SR 455.110.2"
    reference = "SR 455.110.2 Art. 12"

    def formula(person, period, parameters):
        return person('grundlaermpegel_dezibel', period) <= 85.0
