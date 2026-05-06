"""SR 313.32 Art. 16

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class beglaubigung_gebuehr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer eine Beglaubigung oder Bescheinigung (20 CHF)"
    reference = "SR 313.32 Art. 16"
    default_value = 20.0
