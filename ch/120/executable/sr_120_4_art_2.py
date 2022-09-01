"""SR 120.4 Art. 2

Generated from: ch/120/de/120.4.md

Begriffe: Definitions of classified information levels and access zones.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zugang_vertraulich_klassifizierte_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zugang zu VERTRAULICH klassifizierten Informationen oder Material"
    reference = "SR 120.4 Art. 2 lit. a"


class zugang_geheim_klassifizierte_informationen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zugang zu GEHEIM klassifizierten Informationen oder Material"
    reference = "SR 120.4 Art. 2 lit. b"


class zugang_schutzzone_2(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zugang zu Schutzzone 2 einer militaerischen Anlage"
    reference = "SR 120.4 Art. 2 lit. d"


class zugang_schutzzone_3(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Zugang zu Schutzzone 3 einer militaerischen Anlage"
    reference = "SR 120.4 Art. 2 lit. e"
