"""SR 142.206 Art. 24

Generated from: ch/142/de/142.206.md

Inkrafttreten: Diese Verordnung tritt am 1. Mai 2022 in Kraft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class eesv_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die EESV in Kraft ist"
    reference = "SR 142.206 Art. 24"

    def formula_2022_05(person, period, parameters):
        return True
