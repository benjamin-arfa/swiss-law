"""SR 672.916.31 Art. 3 — Aufhebung und Inkrafttreten

Art. 3: Der Bundesratsbeschluss vom 26. Oktober 1954 wird aufgehoben.
Diese Verordnung tritt am 1. Januar 1975 in Kraft.

Generated from: ch/672/de/672.916.31.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_672_916_31_in_kraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 672.916.31 ist in Kraft (seit 1. Januar 1975)"
    reference = "https://www.fedlex.admin.ch/eli/cc/1975/116_116_116/de#art_3"

    def formula_1975(person, period, parameters):
        return True

    def formula_1974(person, period, parameters):
        return False
