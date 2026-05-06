"""SR 312.1 Art. 12

Generated from: ch/312/de/312.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ordnungsbusse_gesetzliche_vertretung_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximale Ordnungsbusse bei Nichtbefolgung durch gesetzliche Vertretung (1000 CHF)"
    reference = "SR 312.1 Art. 12 Abs. 2"
    default_value = 1000.0
