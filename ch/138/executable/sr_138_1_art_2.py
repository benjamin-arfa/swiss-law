"""SR 138.1 Art. 2

Generated from: ch/138/de/138.1.md

Zweck der Mitwirkung: The participation of cantons in foreign policy shall
ensure cantonal interests are considered, preserve cantonal competences in
treaty matters, and provide domestic support for federal foreign policy.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kantonale_interessen_beruecksichtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Interessen der Kantone werden bei aussenpolitischen Entscheiden beruecksichtigt"
    reference = "SR 138.1 Art. 2 Bst. a"


class kantonale_zustaendigkeiten_gewahrt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Zustaendigkeiten der Kantone beim Abschluss voelkerrechtlicher Vertraege werden gewahrt"
    reference = "SR 138.1 Art. 2 Bst. b"


class aussenpolitik_innenpolitisch_abgestuetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aussenpolitik des Bundes ist innenpolitisch abgestuetzt"
    reference = "SR 138.1 Art. 2 Bst. c"


class zweck_mitwirkung_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Zweck der kantonalen Mitwirkung an der Aussenpolitik ist erfuellt"
    reference = "SR 138.1 Art. 2"

    def formula(self, period, parameters):
        interessen = self('kantonale_interessen_beruecksichtigt', period)
        zustaendigkeiten = self('kantonale_zustaendigkeiten_gewahrt', period)
        abstuetzung = self('aussenpolitik_innenpolitisch_abgestuetzt', period)
        return interessen * zustaendigkeiten * abstuetzung
