"""SR 221.213.15 Art. 9

Generated from: ch/221/de/221.213.15.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anhoerungsfrist_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anhörungsfrist in Tagen"
    reference = "SR 221.213.15 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        # Die Behörde setzt eine Anhörungsfrist von 60 Tagen an
        return person.filled_array(60)
