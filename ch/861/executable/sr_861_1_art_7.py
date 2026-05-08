"""SR 861.1 Art. 7

Generated from: ch/861/de/861.1.md

Art. 7: Einrichtungen für die schulergänzende Betreuung - Eligibility:
- At least 10 places
- Open at least 4 days/week and 36 school weeks/year
- Care units: morning min 1h, midday min 2h (incl. meal), afternoon min 2h
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhv_schulerg_anzahl_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Plätze der schulergänzenden Betreuungseinrichtung"
    reference = "SR 861.1 Art. 7 Abs. 2 Bst. a"


class kbfhv_schulerg_oeffnungstage_pro_woche(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Öffnungstage pro Woche der schulergänzenden Betreuungseinrichtung"
    reference = "SR 861.1 Art. 7 Abs. 2 Bst. b"


class kbfhv_schulerg_schulwochen_pro_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Schulwochen pro Jahr, in denen die Einrichtung geöffnet ist"
    reference = "SR 861.1 Art. 7 Abs. 2 Bst. b"


class kbfhv_schulerg_beitragsberechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Schulergänzende Betreuungseinrichtung erfüllt Voraussetzungen für Finanzhilfen"
    reference = "SR 861.1 Art. 7"

    def formula(person, period, parameters):
        plaetze = person('kbfhv_schulerg_anzahl_plaetze', period)
        tage = person('kbfhv_schulerg_oeffnungstage_pro_woche', period)
        wochen = person('kbfhv_schulerg_schulwochen_pro_jahr', period)

        p = parameters(period).sr_861_1
        return (
            (plaetze >= p.schulerg_mindest_plaetze) *
            (tage >= p.schulerg_mindest_tage_pro_woche) *
            (wochen >= p.schulerg_mindest_schulwochen_pro_jahr)
        )
