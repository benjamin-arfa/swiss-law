"""SR 0.142.116.912 Art. 14

Generated from: ch/0/de/0.142.116.912.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_liechtenstein_resident(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Residency in the Principality of Liechtenstein (Art. 14 SR 0.142.116.912)"

    def formula(person, period, parameters):
        return person("nationality") == "Liechtenstein"

class is_liechtenstein_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Citizenship of the Principality of Liechtenstein (Art. 14 SR 0.142.116.912)"

    def formula(person, period, parameters):
        return person("birth_country") == "Liechtenstein"
