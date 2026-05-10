"""SR 367.1 Art. 31

Generated from: ch/367/de/367.1.md

Austritt - Frist von drei Jahren auf Ende eines Kalenderjahrs.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class austrittsfrist_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kuendigungsfrist fuer den Austritt aus der Vereinbarung in Jahren"
    reference = "SR 367.1 Art. 31 Abs. 1"

    def formula(person, period):
        return 3


class anzahl_verbleibende_parteien(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl verbleibende Parteien nach Austritt"
    reference = "SR 367.1 Art. 31 Abs. 2"


class aufloesung_oder_anpassung_noetig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Muss ueber Aufloesung oder Anpassung entschieden werden (weniger als 10 Parteien)"
    reference = "SR 367.1 Art. 31 Abs. 2"

    def formula(person, period):
        verbleibend = person('anzahl_verbleibende_parteien', period)
        return verbleibend < 10
