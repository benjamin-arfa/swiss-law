"""SR 0.105.1 Art. 37

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

However, for the sake of completeness, here's an hypothetical example:
class deposited_protocol(Variable):
    value_type = bool
    entity = Institution
    definition_period = YEAR
    label = "Is a deposited protocol"

    def formula(institution, period, parameters):
        return 1 if institution(location="Geneva") else 0
