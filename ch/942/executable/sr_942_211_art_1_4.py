"""SR 942.211 Art. 1-4

Generated from: ch/942/de/942.211.md

Art. 1: Zweck - Prices must be clear, comparable, and non-misleading

Art. 2: Geltungsbereich - Scope:
- Applies to: a. offer of goods to consumers; b. purchase-like transactions (leasing, etc.);
  c. services listed in Art. 10; d. advertising directed at consumers
- Consumer = person buying for non-commercial/professional purposes

Art. 3: Bekanntgabepflicht - Duty to disclose detail price (actual price in CHF)
- Also applies to purchase-like transactions
- Not applicable to auctions

Art. 4: Public charges, copyright fees, disposal fees must be included in the detail price.
- Shipping costs may be disclosed separately
- VAT rate changes: 3-month adaptation period
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class pbv_ist_konsument(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Konsument (kauft für nicht-gewerbliche/berufliche Zwecke)"
    reference = "SR 942.211 Art. 2 Abs. 2"


class pbv_ware_zum_kauf_angeboten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ware wird zum Kauf an Konsumenten angeboten"
    reference = "SR 942.211 Art. 2 Abs. 1 Bst. a"


class pbv_ist_kaufaehnliches_geschaeft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Rechtsgeschäft mit kaufähnlicher Wirkung (Leasing, Abzahlung, Mietkauf etc.)"
    reference = "SR 942.211 Art. 2 Abs. 1 Bst. b"


class pbv_ist_versteigerung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ware wird an Versteigerung/Auktion verkauft"
    reference = "SR 942.211 Art. 3 Abs. 3"


class pbv_detailpreis_bekanntgabepflicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bekanntgabepflicht für Detailpreis besteht"
    reference = "SR 942.211 Art. 3"

    def formula(person, period, parameters):
        konsument = person('pbv_ist_konsument', period)
        ware = person('pbv_ware_zum_kauf_angeboten', period)
        kaufaehnlich = person('pbv_ist_kaufaehnliches_geschaeft', period)
        versteigerung = person('pbv_ist_versteigerung', period)
        # Duty exists if goods offered to consumers (or purchase-like), except at auctions
        return konsument * (ware + kaufaehnlich) * (1 - versteigerung) > 0


class pbv_oeffentliche_abgaben_im_preis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Überwälzte öffentliche Abgaben sind im Detailpreis inbegriffen"
    reference = "SR 942.211 Art. 4 Abs. 1"


class pbv_mwst_anpassungsfrist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Frist für Preisanpassung bei MwSt-Änderung (Monate)"
    reference = "SR 942.211 Art. 4 Abs. 1bis"

    def formula(person, period, parameters):
        # Fixed 3-month adaptation period
        return person('pbv_ist_konsument', period) * 0 + 3
