"""SR 313.32 Art. 8

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class spruchgebuehr_verwaltungsentscheide_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr fuer Verwaltungsentscheide (Art. 27, 29 Abs. 2, 100 Abs. 4, 102 Abs. 2 VStrR) (50 CHF)"
    reference = "SR 313.32 Art. 8"
    default_value = 50.0


class spruchgebuehr_verwaltungsentscheide_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr fuer Verwaltungsentscheide (2000 CHF)"
    reference = "SR 313.32 Art. 8"
    default_value = 2000.0
