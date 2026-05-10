"""SR 367.1 Art. 30

Generated from: ch/367/de/367.1.md

Aenderung dieser Vereinbarung - Zwei-Drittel-Mehrheit und Ratifikation.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_stimmberechtigte_strategische_versammlung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl stimmberechtigte Mitglieder der strategischen Versammlung"
    reference = "SR 367.1 Art. 30 Abs. 1"


class ja_stimmen_aenderung(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ja-Stimmen fuer die Aenderung"
    reference = "SR 367.1 Art. 30 Abs. 1"


class anzahl_parteien(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamtzahl der Parteien der Vereinbarung"
    reference = "SR 367.1 Art. 30 Abs. 2"


class anzahl_ratifikationen(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Ratifikationen der Aenderung"
    reference = "SR 367.1 Art. 30 Abs. 2"


class aenderung_beschlossen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Aenderung durch die strategische Versammlung beschlossen (2/3-Mehrheit)"
    reference = "SR 367.1 Art. 30 Abs. 1"

    def formula(person, period):
        ja = person('ja_stimmen_aenderung', period)
        total = person('anzahl_stimmberechtigte_strategische_versammlung', period)
        return ja * 3 >= total * 2


class aenderung_ratifiziert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist die Aenderung ratifiziert (2/3 der Parteien)"
    reference = "SR 367.1 Art. 30 Abs. 2"

    def formula(person, period):
        ratifikationen = person('anzahl_ratifikationen', period)
        parteien = person('anzahl_parteien', period)
        return ratifikationen * 3 >= parteien * 2
