"""SR 916.402 Art. 13 – Wiederholung (Prüfungen Veterinärwesen)

Generated from: ch/916/de/916.402.md

Eine nicht bestandene Einzelfachprüfung kann zweimal wiederholt werden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

MAX_WIEDERHOLUNGEN = 2


class einzelfachpruefung_versuche(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Anzahl bisheriger Versuche für eine Einzelfachprüfung"
    reference = "SR 916.402 Art. 13"


class einzelfachpruefung_wiederholung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Wiederholung der Einzelfachprüfung ist noch zulässig"
    reference = "SR 916.402 Art. 13"

    def formula(person, period, parameters):
        versuche = person('einzelfachpruefung_versuche', period)
        # Erstversuch + max 2 Wiederholungen = max 3 Versuche total
        return versuche <= MAX_WIEDERHOLUNGEN
