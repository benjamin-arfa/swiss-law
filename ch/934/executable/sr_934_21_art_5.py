"""SR 934.21 Art. 5

Generated from: ch/934/de/934.21.md

Art. 5 Ueberfuehrung bestehender Betriebe:
1. Existing armament operations of the Armament Group are converted into
   private-law corporations (Aktiengesellschaften).
2. Assets, liabilities, and contractual rights/obligations are transferred
   to the corporations following recognized valuation principles.
3. The Federal Council regulates the details.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgrb_betrieb_ueberfuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein bestehender Ruestungsbetrieb in eine Aktiengesellschaft ueberfuehrt wurde"
    reference = "SR 934.21 Art. 5 Abs. 1"


class bgrb_bewertungsgrundsaetze_beachtet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob anerkannte Bewertungsgrundsaetze bei der Ueberfuehrung beachtet wurden"
    reference = "SR 934.21 Art. 5 Abs. 2"
