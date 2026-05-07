"""SR 453.0 Art. 9

Generated from: ch/453/de/453.0.md
Kaviar-Einfuhr: Ausfuhr aus Ursprungsland nicht laenger als 18 Monate.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ist_kaviar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Exemplar ist Kaviar"
    reference = "SR 453.0 Art. 9 Bst. c"


class monate_seit_ausfuhr_ursprungsland(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Monate seit Ausfuhr aus dem Ursprungsland"
    reference = "SR 453.0 Art. 9 Bst. c"


class kaviar_einfuhr_frist_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Kaviar-Einfuhrfrist (18 Monate seit Ausfuhr) eingehalten"
    reference = "SR 453.0 Art. 9 Bst. c"

    def formula(person, period, parameters):
        ist_kav = person('ist_kaviar', period)
        monate = person('monate_seit_ausfuhr_ursprungsland', period)
        return where(ist_kav, monate <= 18, True)
