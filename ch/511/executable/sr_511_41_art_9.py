"""SR 511.41 Art. 9 – Übergangsbestimmung

Generated from: ch/511/de/511.41.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class datum_funktionszuteilung(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Datum der Zuteilung der militärischen Funktion (YYYY-MM-DD)"
    reference = "SR 511.41 Art. 9"
    default_value = ""


class uebergangsbestimmung_keine_rueckerstattung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Keine Rückerstattungspflicht aufgrund Übergangsbestimmung (Zuteilung vor 1.6.2026)"
    reference = "SR 511.41 Art. 9"

    def formula(person, period, parameters):
        datum = person('datum_funktionszuteilung', period)
        # Personen mit Funktionszuteilung vor dem 1. Juni 2026
        # haben keine Rückerstattungspflicht
        return datum < '2026-06-01'
