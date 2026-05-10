"""SR 0.103.2 Art. 26

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class protection_against_discrimination(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Protection against discrimination (Art. 26 BstG)"

    def formula(person, period, parameters):
        protected = True  # Basic assumption in accordance with Art. 26 BstG
        return protected
