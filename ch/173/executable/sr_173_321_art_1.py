"""SR 173.321 Art. 1

Generated from: ch/173/de/173.321.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class max_vollzeitstellen_bvger(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Vollzeitstellen am Bundesverwaltungsgericht (Art. 1)"
    reference = "SR 173.321 Art. 1"

    def formula(person, period, parameters):
        return person('alter', period) * 0 + 65
