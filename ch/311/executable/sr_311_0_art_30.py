"""SR 311.0 Art. 30-33

Generated from: ch/fr/311/311.0.md

Art. 30: Droit de plainte (Antragsrecht / Right to file complaint)
- Abs. 1: If offence only punishable on complaint, any injured party may file.
- Abs. 2: Legal representative may file if injured lacks capacity.
Art. 31: Prescription of right to file: 3 months from knowing the offender.
Art. 33: Withdrawal of complaint before second-instance cantonal judgment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_antragsdelikt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob es sich um ein Antragsdelikt handelt"
    reference = "SR 311.0 Art. 30 Abs. 1"


class stgb_strafantrag_gestellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    default_value = False
    label = "Ob ein Strafantrag gestellt wurde"
    reference = "SR 311.0 Art. 30 Abs. 1"


class stgb_tage_seit_taeterkenntnis(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Tage seit Kenntnis des Taeters durch den Geschaedigten"
    reference = "SR 311.0 Art. 31"


class stgb_strafantragsfrist_abgelaufen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die dreimonatige Strafantragsfrist abgelaufen ist"
    reference = "SR 311.0 Art. 31"

    def formula(person, period, parameters):
        tage = person('stgb_tage_seit_taeterkenntnis', period)
        # 3 months ~ 90 days
        return tage > 90


class stgb_strafverfolgung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Strafverfolgung zulaessig ist (Antrag gestellt und fristgerecht)"
    reference = "SR 311.0 Art. 30-31"

    def formula(person, period, parameters):
        antragsdelikt = person('stgb_antragsdelikt', period)
        antrag = person('stgb_strafantrag_gestellt', period)
        frist_abgelaufen = person('stgb_strafantragsfrist_abgelaufen', period)

        # Not an Antragsdelikt: always prosecutable
        # Antragsdelikt: needs complaint filed within time
        return not_(antragsdelikt) + (antragsdelikt * antrag * not_(frist_abgelaufen))
