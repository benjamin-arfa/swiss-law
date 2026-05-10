"""SR 311.1 Art. 3

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_bei_tat(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Alter der Person zum Zeitpunkt der Tat (in Jahren)"
    reference = "SR 311.1 Art. 3"


class jstg_persoenlicher_geltungsbereich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Faellt die Person in den persoenlichen Geltungsbereich des JStG (10-18 Jahre)"
    reference = "SR 311.1 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_bei_tat', period)
        return (alter >= 10) * (alter < 18)
