"""SR 705 Art. 9 - Ersatz (Replacement)

Generated from: ch/de/705.md
If planned bicycle paths must be removed, authorities must provide
adequate replacement. Replacement is required when paths are no longer
freely usable, interrupted, unsafe, or lose attractiveness.
Cantons may provide exceptions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class veloweg_nicht_mehr_befahrbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg ist nicht mehr frei befahrbar"
    reference = "SR 705 Art. 9 Abs. 2 lit. a"
    default_value = False


class veloweg_unterbrochen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg ist unterbrochen"
    reference = "SR 705 Art. 9 Abs. 2 lit. b"
    default_value = False


class veloweg_nicht_mehr_sicher(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Veloweg kann nicht mehr sicher befahren werden"
    reference = "SR 705 Art. 9 Abs. 2 lit. c"
    default_value = False


class veloweg_ersatzpflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pflicht zum Ersatz eines aufgehobenen Velowegs"
    reference = "SR 705 Art. 9 Abs. 1-2"

    def formula(person, period, parameters):
        nicht_befahrbar = person('veloweg_nicht_mehr_befahrbar', period)
        unterbrochen = person('veloweg_unterbrochen', period)
        nicht_sicher = person('veloweg_nicht_mehr_sicher', period)
        return nicht_befahrbar + unterbrochen + nicht_sicher
