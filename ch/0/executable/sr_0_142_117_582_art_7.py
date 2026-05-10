"""SR 0.142.117.582 Art. 7

Generated from: ch/0/de/0.142.117.582.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_entry_into_force(Variable):
    value_type = date
    entity = None  # No entity
    definition_period = MONTH  # OpenFISCA always uses Months for this kind of rules
    label = "Entry into force of changes to the agreement (Art. 7 SR 0.142.117.582)"

    def formula(agreement, period, parameters):
        return period.date + 30
