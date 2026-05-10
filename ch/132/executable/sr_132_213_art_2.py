"""SR 132.213 Art. 2 - Referendum und Inkrafttreten

Generated from: ch/132/de/132.213.md

Dieser Beschluss untersteht dem fakultativen Referendum.
Inkrafttreten: 1. Januar 2026.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class moutier_beschluss_referendum_unterstellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beschluss ueber den Kantonswechsel Moutier dem fakultativen Referendum untersteht"
    reference = "SR 132.213 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        return True


class moutier_beschluss_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beschluss ueber den Kantonswechsel Moutier in Kraft ist"
    reference = "SR 132.213 Art. 2 Abs. 2"

    def formula_2026_01_01(person, period, parameters):
        return True
