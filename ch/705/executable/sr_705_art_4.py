"""SR 705 Art. 4 - Velowegnetze fuer die Freizeit (Leisure Bicycle Networks)

Generated from: ch/de/705.md
Leisure bicycle networks primarily serve recreation and are typically
outside settlement areas.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class veloweg_ist_freizeitnetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg gehoert zum Freizeitnetz (vorwiegend der Erholung dienend)"
    reference = "SR 705 Art. 4 Abs. 1"
    default_value = False
