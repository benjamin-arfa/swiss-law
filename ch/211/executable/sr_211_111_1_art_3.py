"""SR 211.111.1 Art. 3

Generated from: ch/211/de/211.111.1.md

Sterilisation von Personen unter 18 Jahren: Verboten (Art. 7 vorbehalten).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der Person in Jahren"
    reference = "SR 211.111.1 Art. 3"


class sterilisation_unter_18_verboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Sterilisation verboten ist weil die Person unter 18 Jahre alt ist"
    reference = "SR 211.111.1 Art. 3"

    def formula(person, period, parameters):
        return person('alter', period) < 18
