"""SR 0.105 Art. 14

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class has_right_to_rehabilitation(Variable):
    value_type = bool
    entity = Victim
    definition_period = "forever"  # Assuming this right does not expire.
    label = "Has the right to rehabilitation and compensation for torture (Art. 14 IPRG)"

    def formula(victim, period, parameters):
        was_victim_of_torture = victim("is_victim_of_torture", period)
        torture_lead_to_death = victim("torture_lead_to_death", period)
        return (was_victim_of_torture & torture_lead_to_death)
