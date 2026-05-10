"""SR 741.01 Art. 90 - Verletzung der Verkehrsregeln

Generated from: ch/de/741/741.01.md

Speed violation thresholds for 'besonders krasse Missachtung' (Art. 90 Abs. 4):
a) +40 km/h where max speed <= 30 km/h
b) +50 km/h where max speed <= 50 km/h
c) +60 km/h where max speed <= 80 km/h
d) +80 km/h where max speed > 80 km/h

Penalties:
- Abs. 1: Busse (simple violation)
- Abs. 2: Freiheitsstrafe bis 3 Jahre / Geldstrafe (grobe Verletzung)
- Abs. 3: Freiheitsstrafe 1-4 Jahre (vorsaetzlich elementar)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class signalisierte_hoechstgeschwindigkeit_kmh(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Signalisierte Hoechstgeschwindigkeit in km/h"
    reference = "SR 741.01 Art. 90 Abs. 4"


class gefahrene_geschwindigkeit_kmh(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tatsaechlich gefahrene Geschwindigkeit in km/h"
    reference = "SR 741.01 Art. 90"


class geschwindigkeitsueberschreitung_kmh(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Geschwindigkeitsueberschreitung in km/h"
    reference = "SR 741.01 Art. 90 Abs. 4"

    def formula(person, period, parameters):
        gefahren = person('gefahrene_geschwindigkeit_kmh', period)
        hoechst = person('signalisierte_hoechstgeschwindigkeit_kmh', period)
        return max_(gefahren - hoechst, 0)


class schwelle_besonders_krass_kmh(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwellenwert fuer besonders krasse Missachtung in km/h"
    reference = "SR 741.01 Art. 90 Abs. 4"

    def formula(person, period, parameters):
        hoechst = person('signalisierte_hoechstgeschwindigkeit_kmh', period)
        # a) max <= 30: threshold +40
        # b) max <= 50: threshold +50
        # c) max <= 80: threshold +60
        # d) max > 80:  threshold +80
        return (
            where(hoechst <= 30, 40,
            where(hoechst <= 50, 50,
            where(hoechst <= 80, 60,
            80)))
        )


class besonders_krasse_geschwindigkeitsmissachtung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine besonders krasse Missachtung der Hoechstgeschwindigkeit vorliegt"
    reference = "SR 741.01 Art. 90 Abs. 4"

    def formula(person, period, parameters):
        ueberschreitung = person('geschwindigkeitsueberschreitung_kmh', period)
        schwelle = person('schwelle_besonders_krass_kmh', period)
        return ueberschreitung >= schwelle


class grobe_verkehrsregelverletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine grobe Verletzung der Verkehrsregeln (Art. 90 Abs. 2) vorliegt"
    reference = "SR 741.01 Art. 90 Abs. 2"


class verkehrsregelverletzung_strafe_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Freiheitsstrafe in Jahren fuer die Verkehrsregelverletzung"
    reference = "SR 741.01 Art. 90"

    def formula(person, period, parameters):
        krass = person('besonders_krasse_geschwindigkeitsmissachtung', period)
        grob = person('grobe_verkehrsregelverletzung', period)
        # Abs. 3: 1-4 Jahre (besonders krass)
        # Abs. 2: bis 3 Jahre (grob)
        # Abs. 1: Busse only (0 Jahre Freiheitsstrafe)
        return where(krass, 4, where(grob, 3, 0))
