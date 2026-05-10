"""SR 451.36 Art. 16

Generated from: ch/451/de/451.36.md
Nationalpark - Mindestflaechen der Kernzone.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nationalpark_biogeographische_region(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Biogeographische Region des Nationalparks (voralpen_alpen, jura_alpensuedflanke, mittelland)"
    reference = "SR 451.36 Art. 16 Abs. 1"
    default_value = "voralpen_alpen"


class nationalpark_kernzone_flaeche_km2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flaeche der Kernzone des Nationalparks in km2"
    reference = "SR 451.36 Art. 16 Abs. 1"


class nationalpark_kernzone_nicht_zusammenhaengend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kernzone besteht aus nicht zusammenhaengenden Teilflaechen"
    reference = "SR 451.36 Art. 16 Abs. 2"


class nationalpark_kernzone_unterhalb_waldgrenze_km2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flaeche der Kernzone unterhalb der Waldgrenze in km2"
    reference = "SR 451.36 Art. 16 Abs. 3"


class nationalpark_mindestflaeche_km2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestflaeche der Kernzone gemaess biogeographischer Region in km2"
    reference = "SR 451.36 Art. 16 Abs. 1"

    def formula(person, period, parameters):
        region = person('nationalpark_biogeographische_region', period)
        return select(
            [region == 'voralpen_alpen', region == 'jura_alpensuedflanke', region == 'mittelland'],
            [100.0, 75.0, 50.0],
        )


class nationalpark_kernzone_flaeche_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kernzone erfuellt die Mindestflaechenanforderung"
    reference = "SR 451.36 Art. 16"

    def formula(person, period, parameters):
        flaeche = person('nationalpark_kernzone_flaeche_km2', period)
        mindest = person('nationalpark_mindestflaeche_km2', period)
        nicht_zusammenhaengend = person('nationalpark_kernzone_nicht_zusammenhaengend', period)
        unterhalb_waldgrenze = person('nationalpark_kernzone_unterhalb_waldgrenze_km2', period)

        # Bei nicht zusammenhaengenden Teilflaechen: +10% Mindestflaeche (Abs. 2a)
        mindest_effektiv = where(nicht_zusammenhaengend, mindest * 1.1, mindest)

        # Abs. 3: mindestens 25 km2 unterhalb der Waldgrenze
        return (flaeche >= mindest_effektiv) * (unterhalb_waldgrenze >= 25.0)
