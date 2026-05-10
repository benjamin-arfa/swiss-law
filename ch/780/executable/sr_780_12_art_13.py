"""SR 780.12 Art. 13

Generated from: ch/780/de/780.12.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ueberwachungsdaten_abruf_verfuegbar(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = (
        "Ueberwachungsdaten stehen den Behoerden mittels Abrufverfahren "
        "mit saemtlichen Bearbeitungsfunktionen zur Verfuegung"
    )
    reference = "SR 780.12 Art. 13 Abs. 1"


class aufbewahrungsfrist_ndb_operation_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = (
        "Aufbewahrungsfrist fuer Daten nach Abschluss einer NDB-Operation "
        "in Monaten (6 Monate)"
    )
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        # Art. 13 Abs. 1 Bst. b: sechs Monate nach Abschluss der Operation
        return person('ist_ndb_operation', period) * 6


class aufbewahrungsfrist_notsuche_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Daten nach Abschluss einer Notsuche in Monaten (6 Monate)"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        return person('ist_notsuche', period) * 6


class aufbewahrungsfrist_fahndung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrungsfrist fuer Daten nach Abschluss einer Fahndung in Monaten (6 Monate)"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. d"

    def formula(person, period, parameters):
        return person('ist_fahndung', period) * 6


class aufbewahrungsfrist_terrorismus_lokalisierung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = (
        "Aufbewahrungsfrist fuer Daten nach Mobilfunklokalisierung einer "
        "terroristischen Gefaehrderin/eines terroristischen Gefaehrders (100 Tage)"
    )
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. dbis"

    def formula(person, period, parameters):
        # Art. 13 Abs. 1 Bst. dbis: 100 Tage nach Abschluss
        return person('ist_terrorismus_lokalisierung', period) * 100


class ist_ndb_operation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten stammen aus einer Operation des Nachrichtendienstes des Bundes"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. b"


class ist_notsuche(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten stammen aus einer Notsuche"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. c"


class ist_fahndung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten stammen aus einer Fahndung"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. d"


class ist_terrorismus_lokalisierung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Daten stammen aus einer Mobilfunklokalisierung gemaess Art. 23q BWIS"
    reference = "SR 780.12 Art. 13 Abs. 1 Bst. dbis"
