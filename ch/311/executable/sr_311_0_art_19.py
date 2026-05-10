"""SR 311.0 Art. 19

Generated from: ch/fr/311/311.0.md

Art. 19: Irresponsabilite et responsabilite restreinte
  (Schuldunfaehigkeit und verminderte Schuldfaehigkeit)
- Abs. 1: Not punishable if unable to appreciate unlawfulness or act accordingly.
- Abs. 2: Reduced sentence if only partially capable.
- Abs. 4: If self-induced, no mitigation applies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_einsichtsfaehigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Einsichtsfaehigkeit zum Tatzeitpunkt (0=keine, 1=voll)"
    reference = "SR 311.0 Art. 19"


class stgb_steuerungsfaehigkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Steuerungsfaehigkeit zum Tatzeitpunkt (0=keine, 1=voll)"
    reference = "SR 311.0 Art. 19"


class stgb_unzurechnungsfaehigkeit_selbstverschuldet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob die Unzurechnungsfaehigkeit selbstverschuldet ist (actio libera in causa)"
    reference = "SR 311.0 Art. 19 Abs. 4"


class stgb_schuldfaehigkeit_status(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Schuldfaehigkeitsstatus: 0=schuldunfaehig, 1=vermindert, 2=voll"
    reference = "SR 311.0 Art. 19"

    def formula(person, period, parameters):
        einsicht = person('stgb_einsichtsfaehigkeit', period)
        steuerung = person('stgb_steuerungsfaehigkeit', period)
        selbst = person('stgb_unzurechnungsfaehigkeit_selbstverschuldet', period)

        faehigkeit = min_(einsicht, steuerung)

        # Self-induced: full responsibility
        # Otherwise: 0 = incapable, partial = diminished, full = full
        status = where(selbst, 2,
                 where(faehigkeit <= 0, 0,
                 where(faehigkeit < 1, 1, 2)))
        return status
