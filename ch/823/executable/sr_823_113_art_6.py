"""SR 823.113 Art. 6

Generated from: ch/823/de/823.113.md

Kaution zulasten von Verleihbetrieben:
- Grundkaution: 50'000 CHF pro Verleiher
- Bei > 60'000 Einsatzstunden/Jahr: 100'000 CHF
- Zusätzlicher Auslandsverleih: +50'000 CHF
- Höchstkaution (Hauptsitz + Zweigniederlassungen): 1'000'000 CHF
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class einsatzstunden_vorjahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Einsatzstunden im abgelaufenen Kalenderjahr"
    reference = "SR 823.113 Art. 6 Abs. 2"


class verleiht_ins_ausland(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Verleiher zusätzlich ins Ausland verleiht"
    reference = "SR 823.113 Art. 6 Abs. 3"


class anzahl_zweigniederlassungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Zweigniederlassungen des Hauptsitzes"
    reference = "SR 823.113 Art. 6 Abs. 4"


class kaution_verleiher(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kaution zulasten von Verleihbetrieben"
    reference = "SR 823.113 Art. 6"

    def formula(person, period, parameters):
        import numpy as np
        stunden = person('einsatzstunden_vorjahr', period)
        ausland = person('verleiht_ins_ausland', period)
        params = parameters(period).sr_823_113

        # Base deposit depends on hours
        kaution = np.where(
            stunden > params.kaution_stunden_schwelle,
            params.kaution_hoch,
            params.kaution_basis
        )

        # Additional deposit for foreign placement
        kaution = np.where(
            ausland,
            kaution + params.kaution_ausland_zuschlag,
            kaution
        )

        # Cap at maximum
        kaution = np.minimum(kaution, params.kaution_max)

        return kaution
