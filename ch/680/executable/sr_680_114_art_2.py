"""SR 680.114 Art. 2

Generated from: ch/680/de/680.114.md

Berechnung der Fehlmengen und der Verluste: Calculation of shortages and losses.
- Abs. 1: Shortages for spirits are calculated using flat-rate values from the annex.
- Abs. 2: Flat rate for non-verifiable production/storage losses of untaxed ethanol is 2%.
- Abs. 3: No shortages/losses for spirits stored in consumer packaging.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ethanol_inventar_menge_liter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Inventarmenge des unversteuerten Ethanols in Litern"
    reference = "SR 680.114 Art. 2 Abs. 2"


class ethanol_verlust_pauschale_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschale fuer Produktions- und Lagerverluste bei unversteuertem Ethanol (Prozent)"
    reference = "SR 680.114 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        return 2.0  # 2 Prozent


class ethanol_verlust_pauschale_menge(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschale Verlustmenge bei unversteuertem Ethanol in Litern"
    reference = "SR 680.114 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        inventar = person('ethanol_inventar_menge_liter', period)
        pauschale = person('ethanol_verlust_pauschale_prozent', period)
        return inventar * pauschale / 100


class lagerung_in_endkonsumenten_behaeltnissen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die gebrannten Wasser in Endkonsumenten-Behaeltnissen gelagert werden"
    reference = "SR 680.114 Art. 2 Abs. 3"


class fehlmengen_geltend_machbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Fehlmengen oder Verluste geltend gemacht werden koennen"
    reference = "SR 680.114 Art. 2 Abs. 3"

    def formula(person, period, parameters):
        in_endkonsumenten = person('lagerung_in_endkonsumenten_behaeltnissen', period)
        return not_(in_endkonsumenten)
