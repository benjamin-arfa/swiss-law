"""SR 451.36 Art. 19

Generated from: ch/451/de/451.36.md
Regionaler Naturpark - Mindestflaeche.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class regionaler_naturpark_flaeche_km2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flaeche des Regionalen Naturparks in km2"
    reference = "SR 451.36 Art. 19 Abs. 1"


class regionaler_naturpark_flaeche_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Regionaler Naturpark erfuellt die Mindestflaeche von 100 km2"
    reference = "SR 451.36 Art. 19 Abs. 1"

    def formula(person, period, parameters):
        flaeche = person('regionaler_naturpark_flaeche_km2', period)
        return flaeche >= 100.0
