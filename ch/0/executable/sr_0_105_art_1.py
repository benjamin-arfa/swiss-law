"""SR 0.105 Art. 1

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_subject_to_torture(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Incidents of torture or analogous acts (Art. 1 SR 0.105)"

    def formula(person, period, parameters):
        official_capacity = person("in_official_capacity", period)
        causing_suffering = person("causing_mental_or_physical_suffering", period)
        purpose = person("one_of_five_purposes", period)

        return (official_capacity & causing_suffering) & purpose
