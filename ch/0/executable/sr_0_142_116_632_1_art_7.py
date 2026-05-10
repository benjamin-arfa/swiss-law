"""SR 0.142.116.632.1 Art. 7

Generated from: ch/0/de/0.142.116.632.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class denied_entry(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Denied entry or stay due to public order, security or health threats (Art. 7 SR 0.142.116.632.1)"

    def formula(person, period, parameters):
        # TO BE IMPLEMENTED USING EXTERNAL INFORMATION
        return False
