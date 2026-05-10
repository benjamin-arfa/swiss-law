"""SR 0.142.116.829 Art. 2

Generated from: ch/0/de/0.142.116.829.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class returned_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person returned from Switzerland to Serbia (SR 0.142.116.829, Art. 2)"

    def formula(person, period, parameters):
        nationality = person("nationality", period)
        has_children = person.has("children")

        # For simplicity and due to a lack of explicit information about spouses and nationality, 
        # we focus on the nationality and have_children conditions. For the exact logic, consult the original text.
        return (nationality == "Serbian") | has_children
