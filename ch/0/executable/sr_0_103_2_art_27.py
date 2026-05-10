"""SR 0.103.2 Art. 27

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class minority_rights(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Protection of minority rights (Art. 27 SR 0.103.2)"

    def formula(person, period, parameters):
        mother_tongue = person("mother_tongue", period)
        minority_language_recognition = parameters(period).cultural_minority_recognition.languages
        is_part_of_country_with_minorities = person("is_part_of_country_with_minorities", period)
        return is_part_of_country_with_minorities & mother_tongue in minority_language_recognition
