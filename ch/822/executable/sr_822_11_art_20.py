"""SR 822.11 Art. 20 - Ersatzruhe bei Sonntagsarbeit

Generated from: ch/de/822/822.11.md

Compensatory rest for Sunday work:
- At least 1 full Sunday as rest day every 2 weeks
- Sunday work <= 5 hours: compensated by free time
- Sunday work > 5 hours: full substitute rest day (min 24h)
  in preceding or following week
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class sonntagsarbeit_dauer_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Dauer der Sonntagsarbeit in Stunden"
    reference = "SR 822.11 Art. 20 Abs. 2"


class ersatzruhetag_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob ein Ersatzruhetag (min 24h) erforderlich ist"
    reference = "SR 822.11 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        dauer = person('sonntagsarbeit_dauer_stunden', period)
        return dauer > 5.0


class ersatzruhetag_mindestdauer_h(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Mindestdauer des Ersatzruhetags in Stunden"
    reference = "SR 822.11 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        erforderlich = person('ersatzruhetag_erforderlich', period)
        return erforderlich * 24.0


class sonntag_als_ruhetag_alle_2_wochen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob mindestens alle 2 Wochen ein ganzer Sonntag als Ruhetag gewaehrt wird"
    reference = "SR 822.11 Art. 20 Abs. 1"
