"""SR 0.105.1 Art. 35

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class art35_privileges(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Art. 35 of law SR 0.105.1 (privileges and immunities for committee and mechanism members)"

    def formula(person, period, parameters):
        role = person("committee_or mekanism_role", period)
        return role == "committee_member" | role == "mechanism_member"
