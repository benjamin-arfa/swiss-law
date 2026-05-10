"""SR 221.213.2 Art. 1

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pacht_grundstueck_landwirtschaftliche_nutzung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pacht von Grundstücken zur landwirtschaftlichen Nutzung"
    reference = "SR 221.213.2 Art. 1 Abs. 1 lit. a"


class pacht_landwirtschaftliches_gewerbe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pacht eines landwirtschaftlichen Gewerbes im Sinne des BGBB"
    reference = "SR 221.213.2 Art. 1 Abs. 1 lit. b"


class pacht_nichtlandwirtschaftliches_nebengewerbe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pacht eines nichtlandwirtschaftlichen Nebengewerbes als wirtschaftliche Einheit mit landwirtschaftlichem Gewerbe"
    reference = "SR 221.213.2 Art. 1 Abs. 1 lit. c"


class lpg_anwendbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesgesetz über die landwirtschaftliche Pacht ist anwendbar"
    reference = "SR 221.213.2 Art. 1"

    def formula(person, period, parameters):
        grundstueck = person('pacht_grundstueck_landwirtschaftliche_nutzung', period)
        gewerbe = person('pacht_landwirtschaftliches_gewerbe', period)
        nebengewerbe = person('pacht_nichtlandwirtschaftliches_nebengewerbe', period)
        return grundstueck + gewerbe + nebengewerbe
