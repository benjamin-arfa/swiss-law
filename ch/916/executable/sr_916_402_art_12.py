"""SR 916.402 Art. 12 – Benotung (Prüfungen Veterinärwesen)

Generated from: ch/916/de/916.402.md

Noten: 1 (sehr schlecht) bis 6 (sehr gut), halbe Noten zulässig.
Prüfung bestanden bei Notendurchschnitt >= 4.0, sofern keine Note
unter 3 und nicht mehr als eine Note unter 4 erteilt wurde.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MINDEST_DURCHSCHNITT = 4.0
MIN_NOTE_ABSOLUT = 3.0
MIN_NOTE_GRENZE = 4.0
MAX_NOTEN_UNTER_4 = 1


class pruefung_notendurchschnitt(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Durchschnittsnote der Einzelfachprüfungen"
    reference = "SR 916.402 Art. 12 Abs. 4"


class pruefung_anzahl_noten_unter_3(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Einzelfachprüfungen mit Note unter 3"
    reference = "SR 916.402 Art. 12 Abs. 5"


class pruefung_anzahl_noten_unter_4(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl Einzelfachprüfungen mit Note unter 4"
    reference = "SR 916.402 Art. 12 Abs. 5"


class pruefung_veterinaerwesen_bestanden(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Prüfung im Veterinärwesen bestanden"
    reference = "SR 916.402 Art. 12 Abs. 5"

    def formula(person, period, parameters):
        durchschnitt = person('pruefung_notendurchschnitt', period)
        unter_3 = person('pruefung_anzahl_noten_unter_3', period)
        unter_4 = person('pruefung_anzahl_noten_unter_4', period)

        # Abs. 5: Durchschnitt >= 4.0, keine Note unter 3,
        # nicht mehr als eine Note unter 4
        return (
            (durchschnitt >= MINDEST_DURCHSCHNITT)
            * (unter_3 == 0)
            * (unter_4 <= MAX_NOTEN_UNTER_4)
        )
