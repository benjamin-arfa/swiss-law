"""SR 313.32 Art. 11

Generated from: ch/313/de/313.32.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class barauslagen_meldeschwelle(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Schwellenwert fuer die Auflistung von Barauslagen und Spesen (50 CHF)"
    reference = "SR 313.32 Art. 11 Abs. 2 lit. b"
    default_value = 50.0
