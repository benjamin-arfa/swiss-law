"""SR 822.11 Art. 36 - Arbeitszeit Jugendlicher

Generated from: ch/de/822/822.11.md

Working time for young workers (under 18):
- Max daily working time same as other employees in same enterprise
- Max 9 hours per day for workers under 18
- Evening/night work restrictions for young workers
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class taegliche_arbeitszeit_jugendlicher_h(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegliche Arbeitszeit des jugendlichen Arbeitnehmers in Stunden"
    reference = "SR 822.11 Art. 31"


class max_taegliche_arbeitszeit_jugendlicher_h(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale taegliche Arbeitszeit fuer Jugendliche (9 Stunden)"
    reference = "SR 822.11 Art. 31 Abs. 1"

    def formula(person, period, parameters):
        return 9.0


class jugendlicher_arbeitszeit_konform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Arbeitszeit des Jugendlichen innerhalb der Grenzen liegt"
    reference = "SR 822.11 Art. 31"

    def formula(person, period, parameters):
        ist_jugend = person('ist_jugendlicher_arbeitnehmer', period.this_year)
        arbeitszeit = person('taegliche_arbeitszeit_jugendlicher_h', period)
        max_zeit = 9.0
        return (1 - ist_jugend) + (ist_jugend * (arbeitszeit <= max_zeit))
