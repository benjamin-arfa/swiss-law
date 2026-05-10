"""SR 171.13 Art. 15

Generated from: ch/171/de/171.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class max_kommissionen_pro_ratsmitglied(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl ständiger Kommissionen, denen ein Ratsmitglied gleichzeitig angehören darf (Regel)"
    reference = "SR 171.13 Art. 15 Abs. 3"

    def formula(person, period, parameters):
        return 2
