"""SR 641.10 Art. 9

Generated from: ch/641/de/641.10.md

Art. 9 Besondere Fälle (Special cases):
1d. On free-of-charge profit-sharing certificates (Genussscheine): CHF 3 per certificate.
1e. On participation rights from restructuring of unincorporated entities that
    existed for at least 5 years: 1% of nominal value (excess settled later
    if rights sold within 5 years).
2. For cooperatives: levy only on net annual inflows exceeding outflows on
   cooperative capital.
3. For capital band (Kapitalband) issues: levy only on net inflows exceeding
   repayments within the band.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class stg_anzahl_gratisgenussscheine(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Number of free-of-charge profit-sharing certificates issued"
    reference = "SR 641.10 Art. 9 Abs. 1 Bst. d"


class stg_abgabe_gratisgenussscheine(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Stamp duty on free profit-sharing certificates (CHF 3 each)"
    reference = "SR 641.10 Art. 9 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        anzahl = person('stg_anzahl_gratisgenussscheine', period)
        satz = parameters(period).sr_641_10.abgabe_pro_gratisgenussschein
        return anzahl * satz


class stg_genossenschaft_einzahlungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual payments into cooperative capital (CHF)"
    reference = "SR 641.10 Art. 9 Abs. 2"


class stg_genossenschaft_rueckzahlungen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Annual repayments from cooperative capital (CHF)"
    reference = "SR 641.10 Art. 9 Abs. 2"


class stg_genossenschaft_netto_abgabepflichtig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Net amount subject to levy for cooperatives (payments - repayments, min 0)"
    reference = "SR 641.10 Art. 9 Abs. 2"

    def formula(person, period, parameters):
        einzahlungen = person('stg_genossenschaft_einzahlungen', period)
        rueckzahlungen = person('stg_genossenschaft_rueckzahlungen', period)
        return max_(einzahlungen - rueckzahlungen, 0)
