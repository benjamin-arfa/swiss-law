"""SR 705 Art. 6 - Planungsgrundsaetze (Planning Principles)

Generated from: ch/de/705.md
Authorities must ensure networks are coherent, have adequate density,
direct routes, safe, separated from motor traffic where possible,
homogeneous quality, and attractive.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class veloweg_zusammenhaengend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Velowege sind zusammenhaengend und durchgehend"
    reference = "SR 705 Art. 6 lit. a"
    default_value = False


class veloweg_sicher(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Velowege sind sicher, Veloverkehr wo moeglich getrennt vom motorisierten Verkehr"
    reference = "SR 705 Art. 6 lit. c"
    default_value = False


class veloweg_homogener_standard(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Velowege weisen einen homogenen Ausbaustandard auf"
    reference = "SR 705 Art. 6 lit. d"
    default_value = False
