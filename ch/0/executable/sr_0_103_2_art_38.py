"""SR 0.103.2 Art. 38

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class committee_membership(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Current member of the committee (SR 0.103.2 Art. 38)"

    def formula(person, period, parameters):
        return person("committee_declaration", period) == 'yes'
