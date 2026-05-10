"""SR 842.11 Art. 1

Generated from: ch/842/de/842.11.md

Art. 1: Mindestumfang an Investitionen bei Erneuerungen
- Die Investitionen muessen in der Regel bei durchschnittlich 50'000 Franken
  pro Wohnung liegen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wfg_investition_pro_wohnung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Investitionsbetrag pro Wohnung bei Erneuerungen (CHF)"
    reference = "SR 842.11 Art. 1"


class wfg_mindestinvestition_erneuerung_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestumfang an Investitionen bei Erneuerungen erreicht (50'000 CHF pro Wohnung)"
    reference = "SR 842.11 Art. 1"

    def formula(person, period, parameters):
        investition = person('wfg_investition_pro_wohnung', period)
        mindest = parameters(period).wfg.mindestinvestition_erneuerung_pro_wohnung
        return investition >= mindest
