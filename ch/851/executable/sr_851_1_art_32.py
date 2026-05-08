"""SR 851.1 Art. 32

Generated from: ch/851/de/851.1.md

Art. 32: Abrechnung
- Abs. 1: Rechnung binnen 60 Tagen nach Ablauf jedes Quartals.
- Abs. 4: Begleichung der Rechnung binnen Monatsfrist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class zug_abrechnungsfrist_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Rechnungsstellung nach Quartalsende (Tage)"
    reference = "SR 851.1 Art. 32 Abs. 1"

    def formula(person, period, parameters):
        return parameters(period).zug.abrechnungsfrist_tage


class zug_zahlungsfrist_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Frist fuer Begleichung der Rechnung (Monate)"
    reference = "SR 851.1 Art. 32 Abs. 4"

    def formula(person, period, parameters):
        return parameters(period).zug.zahlungsfrist_monate
