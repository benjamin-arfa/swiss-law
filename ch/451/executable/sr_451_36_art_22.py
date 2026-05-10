"""SR 451.36 Art. 22

Generated from: ch/451/de/451.36.md
Naturerlebnispark - Flaechen und Standort.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class naturerlebnispark_kernzone_flaeche_km2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Flaeche der Kernzone des Naturerlebnisparks in km2"
    reference = "SR 451.36 Art. 22 Abs. 1"


class naturerlebnispark_kernzone_nicht_zusammenhaengend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kernzone besteht aus nicht zusammenhaengenden Teilflaechen"
    reference = "SR 451.36 Art. 22 Abs. 2"


class naturerlebnispark_distanz_agglomeration_km(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Distanz zum Kern einer Agglomeration in km"
    reference = "SR 451.36 Art. 22 Abs. 4"


class naturerlebnispark_oev_gut_erreichbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Naturerlebnispark ist mit oeffentlichem Verkehr gut erreichbar"
    reference = "SR 451.36 Art. 22 Abs. 5"


class naturerlebnispark_standort_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Naturerlebnispark erfuellt Flaechen- und Standortanforderungen"
    reference = "SR 451.36 Art. 22"

    def formula(person, period, parameters):
        flaeche = person('naturerlebnispark_kernzone_flaeche_km2', period)
        nicht_zusammenhaengend = person('naturerlebnispark_kernzone_nicht_zusammenhaengend', period)
        distanz = person('naturerlebnispark_distanz_agglomeration_km', period)
        oev = person('naturerlebnispark_oev_gut_erreichbar', period)

        # Abs. 1: mindestens 4 km2
        mindest = where(nicht_zusammenhaengend, 4.0 * 1.1, 4.0)
        flaeche_ok = flaeche >= mindest

        # Abs. 4: hoechstens 20 km Umkreis einer Agglomeration
        distanz_ok = distanz <= 20.0

        return flaeche_ok * distanz_ok * oev
