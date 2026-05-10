"""SR 0.142.117.542 Art. 9

Generated from: ch/0/de/0.142.117.542.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class entry_into_force_date(Variable):
    value_type = date
    entity = None
    definition_period = DAY
    label = "SR 142.117.542 entry into force date"

    def formula(_):
        return today()
