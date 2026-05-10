"""SR 311.0 Art. 47

Generated from: ch/fr/311/311.0.md

Art. 47: Fixation de la peine - Principe (Strafzumessung)
- Abs. 1: The court fixes the sentence according to the culpability of the offender,
  considering prior record and personal circumstances, and effect on future.
- Abs. 2: Culpability determined by: gravity of harm/danger, reprehensibility,
  motives, goals, and avoidability.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class stgb_schwere_der_rechtsgutverletzung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Schwere der Rechtsgutverletzung oder -gefaehrdung (Skala 0-10)"
    reference = "SR 311.0 Art. 47 Abs. 2"


class stgb_verwerflichkeit_des_handelns(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Verwerflichkeit des Handelns (Skala 0-10)"
    reference = "SR 311.0 Art. 47 Abs. 2"


class stgb_beweggruende_und_ziele(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Bewertung der Beweggruende und Ziele des Taeters (Skala 0-10)"
    reference = "SR 311.0 Art. 47 Abs. 2"


class stgb_vermeidbarkeit(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Vermeidbarkeit der Tat (Skala 0-10)"
    reference = "SR 311.0 Art. 47 Abs. 2"


class stgb_verschulden_gesamtbewertung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtbewertung des Verschuldens (gewichteter Durchschnitt, 0-10)"
    reference = "SR 311.0 Art. 47"

    def formula(person, period, parameters):
        schwere = person('stgb_schwere_der_rechtsgutverletzung', period)
        verwerflichkeit = person('stgb_verwerflichkeit_des_handelns', period)
        beweggruende = person('stgb_beweggruende_und_ziele', period)
        vermeidbarkeit = person('stgb_vermeidbarkeit', period)

        # Weighted average of culpability factors
        return (schwere * 0.35 + verwerflichkeit * 0.25 +
                beweggruende * 0.20 + vermeidbarkeit * 0.20)
