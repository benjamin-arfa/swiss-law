"""SR 0.101.094 Art. 4

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class Art_4_Structure(Variable):
    value_type = float
    entity = SuperEntity()

    def formula(e, period):
        return None

    def default(e):
        return None
