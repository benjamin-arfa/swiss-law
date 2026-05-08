"""SR 705 Art. 12 - Zurverfuegungstellung von Geobasisdaten

Generated from: ch/de/705.md
Cantons must provide the Confederation with current geodata on their
bicycle path networks. The federal office may set quality/technical standards.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class kanton_liefert_velo_geobasisdaten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kanton stellt dem Bund aktuelle Geobasisdaten zu Velowegnetzen zur Verfuegung"
    reference = "SR 705 Art. 12 Abs. 1"
    default_value = False
