"""SR 0.104 Art. 11

Generated from: ch/0/de/0.104.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class state_dispute_resolution_status(Variable):
    value_type = str
    entity = None
    definition_period = DAY
    label = "State dispute resolution status (SR 0.104 Art. 11)"

    def formula(e):
        return "under_review"
