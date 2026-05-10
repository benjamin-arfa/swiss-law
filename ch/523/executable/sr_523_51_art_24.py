"""SR 523.51 Art. 24

Generated from: ch/523/de/523.51.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufbewahrungspflicht_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestdauer der Aufbewahrungspflicht fuer Pruefungsunterlagen in Jahren"
    reference = "SR 523.51 Art. 24"

    def formula(person, period, parameters):
        # Mindestens zehn Jahre
        return person.filled_array(10)
