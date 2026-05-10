"""SR 442.130 Art. 9

Generated from: ch/442/de/442.130.md

Finanzierung kulturelle Teilhabe: Max 50% Kosten, max 100'000 CHF pro Vorhaben.
Freiwilligenarbeit max 10% Gesamtkosten. Vorhaben mit Modellcharakter max 3x.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_vorhaben_teilhabe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten des Vorhabens zur kulturellen Teilhabe (CHF)"
    reference = "SR 442.130 Art. 9 Abs. 1"


class hat_modellcharakter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Vorhaben Modellcharakter hat"
    reference = "SR 442.130 Art. 6"


class bisherige_unterstuetzungen_modellvorhaben(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl bisheriger Unterstuetzungen dieses Modellvorhabens"
    reference = "SR 442.130 Art. 9 Abs. 3"


class max_finanzhilfe_teilhabe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Finanzhilfe kulturelle Teilhabe (max 50%, max 100'000 CHF)"
    reference = "SR 442.130 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('kosten_vorhaben_teilhabe', period)
        import numpy as np
        return np.minimum(kosten * 0.50, 100000)


class modellvorhaben_weitere_unterstuetzung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Modellvorhaben nochmals unterstuetzt werden kann (max 3x)"
    reference = "SR 442.130 Art. 9 Abs. 3"

    def formula(person, period, parameters):
        bisherig = person('bisherige_unterstuetzungen_modellvorhaben', period)
        modell = person('hat_modellcharakter', period)
        return modell * (bisherig < 3)
