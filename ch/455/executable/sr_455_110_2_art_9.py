"""SR 455.110.2 Art. 9

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class wartungsintervall_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Intervall zwischen Wartungen der Betaeubungsanlagen in Monaten"
    reference = "SR 455.110.2 Art. 9 Abs. 2"


class wartungsintervall_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wartungsintervall der Betaeubungsanlagen ist konform (max 24 Monate) nach Art. 9 Abs. 2 SR 455.110.2"
    reference = "SR 455.110.2 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        intervall = person('wartungsintervall_monate', period)
        return intervall <= 24
