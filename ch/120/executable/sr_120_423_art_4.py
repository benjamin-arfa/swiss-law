"""SR 120.423 Art. 4

Generated from: ch/120/de/120.423.md

Inkrafttreten: Diese Verordnung tritt am 1. April 2012 in Kraft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pspv_vbs_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die PSPV-VBS in Kraft ist"
    reference = "SR 120.423 Art. 4"

    def formula_2012_04(person, period, parameters):
        return True
