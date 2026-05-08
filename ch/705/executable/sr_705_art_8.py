"""SR 705 Art. 8 - Anlage und Erhaltung (Construction and Maintenance)

Generated from: ch/de/705.md
Authorities must ensure bicycle paths are built, maintained, signposted,
freely and safely usable, and that public use is legally secured.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class veloweg_frei_befahrbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg kann frei und sicher mit dem Velo befahren werden"
    reference = "SR 705 Art. 8 lit. b"
    default_value = True


class veloweg_oeffentliche_benutzung_gesichert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Oeffentliche Benutzung des Velowegs ist rechtlich gesichert"
    reference = "SR 705 Art. 8 lit. c"
    default_value = False
