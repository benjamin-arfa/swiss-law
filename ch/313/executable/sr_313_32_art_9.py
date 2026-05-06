"""SR 313.32 Art. 9

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class spruchgebuehr_revisionsablehnung_min(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Minimale Spruchgebuehr fuer Ablehnung eines Revisionsgesuches (50 CHF)"
    reference = "SR 313.32 Art. 9"
    default_value = 50.0


class spruchgebuehr_revisionsablehnung_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Spruchgebuehr fuer Ablehnung eines Revisionsgesuches (5000 CHF)"
    reference = "SR 313.32 Art. 9"
    default_value = 5000.0
