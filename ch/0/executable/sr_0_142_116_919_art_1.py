"""SR 0.142.116.919 Art. 1

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_foreigners(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Is a person a foreigner? (Article 1, Agreement)"

    def formula(person, period, parameters):
        nationality_suisse = person("nationalswiss", period)
        nationality_slovenian = person("nationslovenian", period)
        stateless = person("stateless_person", period)
        return (not nationality_suisse) and (not nationality_slovenian) and stateless
