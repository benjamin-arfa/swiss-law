"""SR 0.142.117.147 Art. 1

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_stagiaire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Status as Stagiaire according to SR 0.142.117.147 Art. 1"

    def formula(person, period, parameters):
        return False  # No formula provided due to missing parameterization of the approval conditions
