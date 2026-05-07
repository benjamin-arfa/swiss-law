"""SR 513.75 Art. 10

Generated from: ch/513/de/513.75.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class katastrophenhilfe_ist_unentgeltlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Militaerische Katastrophenhilfe ist in der Regel unentgeltlich (Art. 10 SR 513.75)"
    reference = "SR 513.75 Art. 10"

    def formula(person, period, parameters):
        # Art. 10 Abs. 1: Die Katastrophenhilfe ist in der Regel unentgeltlich.
        # Abs. 2: Das VBS entscheidet ueber Ausnahmen.
        return True
