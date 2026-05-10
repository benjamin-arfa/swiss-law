"""SR 0.132.349.20 Art. 5

Generated from: ch/0/de/0.132.349.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class exchanged_originals(Variable):
    value_type = bool
    entity = Institution
    definition_period = DATE
    label = "Have original copies of the SR 0.132.349.20 treaty been exchanged?"

    def formula(entities, period, parameters):
        institution = entities('institution')
        return institution('treaty_exchanged_originals', period)
