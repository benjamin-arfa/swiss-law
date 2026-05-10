"""SR 933.011.3 Art. 2

Generated from: ch/933/de/933.011.3.md

Inkrafttreten: Diese Verordnung tritt am 1. Oktober 2014 in Kraft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_933_011_3_in_kraft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Verordnung SR 933.011.3 in Kraft ist"
    reference = "SR 933.011.3 Art. 2"

    def formula_2014(person, period, parameters):
        """In Kraft seit 1. Oktober 2014."""
        return True
