"""SR 455.102.4 Art. 2

Generated from: ch/455/de/455.102.4.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


# Input variables
class kennt_belastungen_der_zuchtform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuechter kennt die Belastungen der Zuchtform (Art. 2 lit. a SR 455.102.4)"
    reference = "SR 455.102.4 Art. 2 lit. a"


class verfolgt_belastende_zuchtziele(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuechter verfolgt Zuchtziele die mit Schmerzen, Leiden, Schaeden verbunden sind (Art. 2 lit. b SR 455.102.4)"
    reference = "SR 455.102.4 Art. 2 lit. b"


class zuchtpflichten_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuechter erfuellt die Pflichten beim Zuechten nach Art. 2 SR 455.102.4"
    reference = "SR 455.102.4 Art. 2"

    def formula(person, period, parameters):
        kennt_belastungen = person('kennt_belastungen_der_zuchtform', period)
        belastende_ziele = person('verfolgt_belastende_zuchtziele', period)
        return kennt_belastungen * not_(belastende_ziele)
