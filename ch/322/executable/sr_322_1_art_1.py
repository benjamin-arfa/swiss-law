"""SR 322.1 Art. 1

Generated from: ch/322/de/322.1.md

Unabhaengigkeit: Die Unabhaengigkeit der Militaerjustiz ist gewaehrleistet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class militaerjustiz_unabhaengig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Unabhaengigkeit der Militaerjustiz gewaehrleistet ist"
    reference = "SR 322.1 Art. 1"

    def formula_1979(person, period, parameters):
        """Grundsatz seit Inkrafttreten des MStP 1979."""
        return True
