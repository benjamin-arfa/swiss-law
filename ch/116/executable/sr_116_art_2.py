"""SR 116 Art. 2 - Beschaeftigung am Bundesfeiertag (Working on National Day)

Generated from: ch/de/116.md
Employment on the National Day follows Sunday work rules.
Work up to 5 hours must be compensated with equal time off.
Work over 5 hours must be compensated with a full replacement rest day.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class arbeit_am_bundesfeiertag_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anzahl Arbeitsstunden am Bundesfeiertag"
    reference = "SR 116 Art. 2"
    default_value = 0.0


class bundesfeiertag_ersatzruhetag_anspruch(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf einen ganzen Ersatzruhetag (Arbeit > 5 Stunden am Bundesfeiertag)"
    reference = "SR 116 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        stunden = person('arbeit_am_bundesfeiertag_stunden', period)
        return stunden > 5


class bundesfeiertag_freizeitausgleich_stunden(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Freizeit gleicher Dauer (Arbeit <= 5 Stunden am Bundesfeiertag)"
    reference = "SR 116 Art. 2 Abs. 2"

    def formula(person, period, parameters):
        stunden = person('arbeit_am_bundesfeiertag_stunden', period)
        # If work <= 5 hours: compensated with equal time off
        # If work > 5 hours: full replacement rest day (handled by ersatzruhetag)
        return where(stunden <= 5, stunden, 0)
