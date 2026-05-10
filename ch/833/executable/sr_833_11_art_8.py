"""SR 833.11 Art. 8

Generated from: ch/833/de/833.11.md

Art. 8: Freiwillige Grundversicherung - Voluntary basic insurance:
1. "Pensionierte" = professionally insured persons who retire normally or early
2. Enrollment: written application during last service year, or within 2 months of retirement
   Admission without reservation from retirement date
3. Exit: any time with written declaration, effective at earliest the month after declaration
   Re-entry is excluded
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class mvv_ist_pensioniert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist pensionierter beruflich Versicherter der Militärversicherung"
    reference = "SR 833.11 Art. 8 Abs. 1"


class mvv_anmeldung_fristgerecht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anmeldung zur freiwilligen Grundversicherung ist fristgerecht (im letzten Dienstjahr oder innert 2 Monaten)"
    reference = "SR 833.11 Art. 8 Abs. 2"


class mvv_freiwillige_grundversicherung_beitritt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Beitritt zur freiwilligen Grundversicherung ist möglich"
    reference = "SR 833.11 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        pensioniert = person('mvv_ist_pensioniert', period)
        fristgerecht = person('mvv_anmeldung_fristgerecht', period)
        # Admission if retired and enrolled in time — without reservation
        return pensioniert * fristgerecht


class mvv_austritt_aus_grundversicherung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Austritt aus freiwilliger Grundversicherung erklärt (Wiedereintritt ausgeschlossen)"
    reference = "SR 833.11 Art. 8 Abs. 3"
