"""SR 822.11 Art. 19 Abs. 3 & 6 - Sonntagsarbeit: Lohnzuschlag und Verkaufssonntage

Generated from: ch/de/822/822.11.md

Sunday work rules:
- Temporary Sunday work: 50% wage supplement
- Cantons may designate max 4 Sundays per year where retail staff
  can work without permit
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class voruebergehende_sonntagsarbeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob voruebergehende (nicht dauernde) Sonntagsarbeit geleistet wird"
    reference = "SR 822.11 Art. 19 Abs. 3"


class lohnzuschlag_sonntagsarbeit_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Lohnzuschlag bei voruebergehender Sonntagsarbeit in Prozent"
    reference = "SR 822.11 Art. 19 Abs. 3"

    def formula(person, period, parameters):
        vorueber = person('voruebergehende_sonntagsarbeit', period)
        return vorueber * 50.0


class max_verkaufssonntage_pro_jahr(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Anzahl bewilligungsfreier Verkaufssonntage pro Kanton pro Jahr"
    reference = "SR 822.11 Art. 19 Abs. 6"

    def formula(person, period, parameters):
        return 4
