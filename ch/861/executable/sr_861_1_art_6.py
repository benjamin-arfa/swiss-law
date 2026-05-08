"""SR 861.1 Art. 6

Generated from: ch/861/de/861.1.md

Art. 6: Bemessung und Dauer der Finanzhilfen an Kindertagesstätten
- Lump-sum contributions calculated per Anhang 1
- Occupied places: full contribution for 2 years
- Unoccupied places: 50% of contribution during first year only
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kbfhv_kita_belegte_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl belegte Plätze in der Kindertagesstätte"
    reference = "SR 861.1 Art. 6 Abs. 3 Bst. a"


class kbfhv_kita_nicht_belegte_plaetze(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl nicht belegte Plätze in der Kindertagesstätte"
    reference = "SR 861.1 Art. 6 Abs. 3 Bst. b"


class kbfhv_kita_beitragsjahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Laufendes Beitragsjahr (1, 2 oder 3)"
    reference = "SR 861.1 Art. 6 Abs. 3"


class kbfhv_kita_pauschalbeitrag_pro_platz(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalbeitrag pro Platz gemäss Anhang 1 (CHF)"
    reference = "SR 861.1 Art. 6 Abs. 2"


class kbfhv_kita_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe an Kindertagesstätte (CHF)"
    reference = "SR 861.1 Art. 6"

    def formula(person, period, parameters):
        belegte = person('kbfhv_kita_belegte_plaetze', period)
        nicht_belegte = person('kbfhv_kita_nicht_belegte_plaetze', period)
        beitragsjahr = person('kbfhv_kita_beitragsjahr', period)
        pauschale = person('kbfhv_kita_pauschalbeitrag_pro_platz', period)

        # Art. 6 Abs. 3 Bst. a: full contribution for occupied places in years 1-2
        beitrag_belegt = where(beitragsjahr <= 2, belegte * pauschale, 0)

        # Art. 6 Abs. 3 Bst. b: 50% for unoccupied places in year 1 only
        beitrag_nicht_belegt = where(beitragsjahr <= 1, nicht_belegte * pauschale * 0.5, 0)

        return beitrag_belegt + beitrag_nicht_belegt
