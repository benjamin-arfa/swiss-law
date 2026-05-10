"""SR 0.142.113.321 Art. 6

Generated from: ch/0/de/0.142.113.321.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gross_benefits(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gross benefits (Art. 6 SR 0.142.113.321)"

    def formula(person, period, parameters):
        # Assume benefits are added to gross_benefits variable
        return person("gross_benefits", period)
