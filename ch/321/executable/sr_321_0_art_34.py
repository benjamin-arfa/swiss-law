"""SR 321.0 Art. 34

Generated from: ch/321/de/321.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class freiheitsstrafe_min_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Mindestdauer der Freiheitsstrafe (3 Tage)"
    reference = "SR 321.0 Art. 34 Abs. 1"
    default_value = 3


class freiheitsstrafe_max_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Hoechstdauer der Freiheitsstrafe (20 Jahre, sofern nicht lebenslaenglich)"
    reference = "SR 321.0 Art. 34 Abs. 2"
    default_value = 20


class lebenslaengliche_freiheitsstrafe_angedroht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Gesetz sieht ausdruecklich lebenslaengliche Freiheitsstrafe vor"
    reference = "SR 321.0 Art. 34 Abs. 2"
