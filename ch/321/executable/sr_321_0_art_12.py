"""SR 321.0 Art. 12

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class angedrohte_freiheitsstrafe_jahre(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Angedrohte Hoechstfreiheitsstrafe fuer die Tat (in Jahren)"
    reference = "SR 321.0 Art. 12"


class ist_verbrechen_mstg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Tat ist ein Verbrechen (Freiheitsstrafe von mehr als drei Jahren angedroht)"
    reference = "SR 321.0 Art. 12 Abs. 2"

    def formula(person, period, parameters):
        strafe = person('angedrohte_freiheitsstrafe_jahre', period)
        return strafe > 3


class ist_vergehen_mstg(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Tat ist ein Vergehen (Freiheitsstrafe bis zu drei Jahren oder Geldstrafe angedroht)"
    reference = "SR 321.0 Art. 12 Abs. 3"

    def formula(person, period, parameters):
        strafe = person('angedrohte_freiheitsstrafe_jahre', period)
        return (strafe > 0) * (strafe <= 3)
