"""SR 705 Art. 3 - Velowegnetze fuer den Alltag (Everyday Bicycle Networks)

Generated from: ch/de/705.md
Everyday bicycle networks are typically within or between settlement areas.
They include roads with bike lanes, cycle highways, bike paths, parking facilities, etc.
They connect residential areas, workplaces, schools, public transport stops, etc.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class veloweg_ist_alltagsnetz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg gehoert zum Alltagsnetz (in oder zwischen Siedlungsgebieten)"
    reference = "SR 705 Art. 3 Abs. 1"
    default_value = False
