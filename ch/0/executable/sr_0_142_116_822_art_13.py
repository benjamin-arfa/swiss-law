"""SR 0.142.116.822 Art. 13

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class data_protection_lawReference(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Data protection law reference (SR 0.142.116.822 Art. 13)"

    def formula(person, period, parameters):
        return "SR 0.142.116.822 Art. 13"
