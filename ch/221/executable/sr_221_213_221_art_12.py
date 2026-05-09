"""SR 221.213.221 Art. 12 – Pachtzinsreduktion bei Mehrleistung des Pächters

Generated from: ch/221/de/221.213.221.md

Übernimmt der Pächter Nebenleistungen über das gesetzliche Mass hinaus,
ist die Abgeltung der Verpächterlasten anteilmässig herabzusetzen.
Bei Gebäuden auf einzelnen Grundstücken max 50% Reduktion.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MAX_REDUKTION_GEBAEUDE = 0.50  # max 50%


class paechter_nebenleistung_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anteil der Nebenleistungen des Pächters über gesetzliches Mass hinaus (0-1)"
    reference = "SR 221.213.221 Art. 12"
    default_value = 0.0


class ist_einzelnes_grundstueck_gebaeude(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pacht betrifft Gebäude auf einzelnen Grundstücken (Art. 10)"
    reference = "SR 221.213.221 Art. 12"


class pachtzinsreduktion_mehrleistung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Pachtzinsreduktion aufgrund Mehrleistung des Pächters (CHF)"
    reference = "SR 221.213.221 Art. 12"

    def formula(person, period, parameters):
        import numpy as np
        verpaechterlasten = person('abgeltung_verpaechterlasten_total', period)
        anteil = person('paechter_nebenleistung_anteil', period)
        ist_gebaeude = person('ist_einzelnes_grundstueck_gebaeude', period)

        # Reduktion: anteilmässige Herabsetzung der Verpächterlasten
        reduktion = verpaechterlasten * anteil

        # Bei Gebäuden auf einzelnen Grundstücken: max 50% des höchstzulässigen Pachtzinses
        max_reduktion = np.where(
            ist_gebaeude,
            verpaechterlasten * MAX_REDUKTION_GEBAEUDE,
            verpaechterlasten  # kein besonderes Maximum bei Gewerbe
        )

        return np.minimum(reduktion, max_reduktion)
