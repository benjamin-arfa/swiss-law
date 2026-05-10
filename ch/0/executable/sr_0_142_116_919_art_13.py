"""SR 0.142.116.919 Art. 13

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notify_during_transit(Variable):
    value_type = bool
    entity = Institution
    label = "Notification of authorities during transit (SR 0.142.116.919 Art. 13)"

    def formula(institution, period, parameters):
        return 1
