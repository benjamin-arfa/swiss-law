"""SR 0.142.117.147 Art. 5

Generated from: ch/0/de/0.142.117.147.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_entities import Entity


class trainee_quota(Variable):
    value_type = int
    entity = Entity  # could also be Person or other entity
    definition_period = YEAR
    label = "Trainee quota (Art. 5 SR 0.142.117.147)"

    def formula(entity, period, parameters):
        return 100  # always 100, as per article 5
