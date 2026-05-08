"""SR 861.1 Art. 9

Generated from: ch/861/de/861.1.md

Art. 9: Bemessung und Dauer der Finanzhilfen an schulergänzende Betreuung
- Lump-sum contributions per Anhang 2
- Occupied places: full for 2 years, 50% in year 3
- Unoccupied places: 50% in year 1 only
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhv_schulerg_belegte_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl belegte Plätze schulergänzende Betreuung"
    reference = "SR 861.1 Art. 9 Abs. 3 Bst. a"


class kbfhv_schulerg_nicht_belegte_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl nicht belegte Plätze schulergänzende Betreuung"
    reference = "SR 861.1 Art. 9 Abs. 3 Bst. b"


class kbfhv_schulerg_beitragsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laufendes Beitragsjahr schulergänzende Betreuung (1, 2 oder 3)"
    reference = "SR 861.1 Art. 9 Abs. 3"


class kbfhv_schulerg_pauschalbeitrag_pro_platz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalbeitrag pro Platz gemäss Anhang 2 (CHF)"
    reference = "SR 861.1 Art. 9 Abs. 2"


class kbfhv_schulerg_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe an schulergänzende Betreuungseinrichtung (CHF)"
    reference = "SR 861.1 Art. 9"

    def formula(person, period, parameters):
        belegte = person('kbfhv_schulerg_belegte_plaetze', period)
        nicht_belegte = person('kbfhv_schulerg_nicht_belegte_plaetze', period)
        beitragsjahr = person('kbfhv_schulerg_beitragsjahr', period)
        pauschale = person('kbfhv_schulerg_pauschalbeitrag_pro_platz', period)

        # Art. 9 Abs. 3 Bst. a: full for 2 years, 50% in year 3
        beitrag_belegt = where(
            beitragsjahr <= 2,
            belegte * pauschale,
            where(beitragsjahr == 3, belegte * pauschale * 0.5, 0)
        )

        # Art. 9 Abs. 3 Bst. b: 50% for unoccupied places in year 1 only
        beitrag_nicht_belegt = where(
            beitragsjahr <= 1,
            nicht_belegte * pauschale * 0.5,
            0
        )

        return beitrag_belegt + beitrag_nicht_belegt
