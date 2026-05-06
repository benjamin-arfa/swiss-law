"""SR 313.32 Art. 15

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class telegramm_zusatzgebuehr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zusatzgebuehr fuer Mitteilung per Fernschreiber/Telegramm (5 CHF)"
    reference = "SR 313.32 Art. 15"
    default_value = 5.0
