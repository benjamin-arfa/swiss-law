"""SR 822.11 Art. 17a - Nachtarbeit: Arbeitszeit

Generated from: ch/de/822/822.11.md

Night work time limits:
- Max 9 hours per day, within 10-hour window
- If max 3 of 7 consecutive nights: max 10 hours, within 12-hour window
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nachtarbeit_geleistet(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob Nachtarbeit geleistet wird"
    reference = "SR 822.11 Art. 17a"


class anzahl_nachtschichten_pro_7_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Nachtschichten in 7 aufeinanderfolgenden Tagen"
    reference = "SR 822.11 Art. 17a Abs. 2"


class nachtarbeit_max_taegliche_arbeitszeit_h(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale taegliche Arbeitszeit bei Nachtarbeit in Stunden"
    reference = "SR 822.11 Art. 17a"

    def formula(person, period, parameters):
        nacht = person('nachtarbeit_geleistet', period)
        naechte_7 = person('anzahl_nachtschichten_pro_7_tage', period)
        # Max 3 of 7 nights: 10h allowed; otherwise: 9h
        max_h = where(naechte_7 <= 3, 10.0, 9.0)
        return nacht * max_h


class nachtarbeit_max_zeitfenster_h(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximales Zeitfenster (inkl. Pausen) bei Nachtarbeit in Stunden"
    reference = "SR 822.11 Art. 17a"

    def formula(person, period, parameters):
        nacht = person('nachtarbeit_geleistet', period)
        naechte_7 = person('anzahl_nachtschichten_pro_7_tage', period)
        # Max 3 of 7 nights: 12h window; otherwise: 10h window
        fenster = where(naechte_7 <= 3, 12.0, 10.0)
        return nacht * fenster
