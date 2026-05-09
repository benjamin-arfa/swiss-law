"""SR 414.110.21 Art. 2

Generated from: ch/414/de/414.110.21.md

Zusammensetzung und Sitz der ETH-Beschwerdekommission:
1. Die Kommission besteht aus 7 Mitgliedern:
   - Praesidentin/Praesident
   - Vizepraesidentin/Vizepraesident
   - 5 weitere Mitglieder
2. Praesident, Vizepraesident und mindestens 2 der 5 weiteren Mitglieder
   duerfen nicht dem ETH-Bereich angehoeren.
3. Sitz: Bern
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vethbk_ist_kommissionsmitglied(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Mitglied der ETH-Beschwerdekommission ist"
    reference = "SR 414.110.21 Art. 2 Abs. 1"


class vethbk_gehoert_eth_bereich_an(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person dem ETH-Bereich angehoert"
    reference = "SR 414.110.21 Art. 2 Abs. 2"


class vethbk_ist_praesident(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Praesidentin/Praesident der Kommission ist"
    reference = "SR 414.110.21 Art. 2 Abs. 1 Bst. a"


class vethbk_ist_vizepraesident(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person Vizepraesidentin/Vizepraesident der Kommission ist"
    reference = "SR 414.110.21 Art. 2 Abs. 1 Bst. b"


class vethbk_erfuellt_unabhaengigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Mitglied die Unabhaengigkeitsanforderung erfuellt (nicht ETH-Bereich fuer Praesidium)"
    reference = "SR 414.110.21 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        eth_bereich = person('vethbk_gehoert_eth_bereich_an', period)
        ist_praesident = person('vethbk_ist_praesident', period)
        ist_vize = person('vethbk_ist_vizepraesident', period)

        # Praesident und Vize duerfen nicht dem ETH-Bereich angehoeren
        praesidium = ist_praesident + ist_vize > 0
        return where(praesidium, not_(eth_bereich), True)
