"""SR 170.32 Art. 9

Generated from: ch/170/de/170.32.md

Ansprüche des Bundes gegen Beamte - OR-Bestimmungen anwendbar.
Solidarhaftung: Mehrere Beamte haften nur anteilmässig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_mitverantwortliche_beamte(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl der Beamten, die den Schaden gemeinsam verschuldet haben (Art. 9 Abs. 2 VG)"
    reference = "SR 170.32, Art. 9 Abs. 2"


class verschuldensanteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil des Verschuldens des einzelnen Beamten (0.0 bis 1.0) (Art. 9 Abs. 2 VG)"
    reference = "SR 170.32, Art. 9 Abs. 2"


class haftungsanteil_beamter(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteilmässiger Haftungsbetrag des Beamten in CHF (Art. 9 Abs. 2 VG)"
    reference = "SR 170.32, Art. 9 Abs. 2"

    def formula(person, period, parameters):
        schaden = person('schaden_dem_bund_zugefuegt', period)
        anteil = person('verschuldensanteil', period)
        return schaden * anteil
