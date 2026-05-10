"""SR 520.20 Art. 11

Generated from: ch/520/de/520.20.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anspruch_entschaedigung_nutzung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eigentuemer haben Anspruch auf angemessene Entschaedigung fuer die Nutzung der Schutzanlagen und Liegestellen"
    reference = "SR 520.20 Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period) * person('ist_eigentuemer_schutzanlage', period)


class anspruch_entschaedigung_uebergabe_kosten(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Eigentuemer haben Anspruch auf Entschaedigung der Kosten fuer Uebergabe und Rueckgabe"
    reference = "SR 520.20 Art. 11 Abs. 2"

    def formula(person, period, parameters):
        return person('requisition_voraussetzungen_erfuellt', period) * person('ist_eigentuemer_schutzanlage', period)


class ist_eigentuemer_schutzanlage(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Ist Eigentuemer einer requirierten Schutzanlage oder Liegestelle"
    reference = "SR 520.20 Art. 11"


class haftung_schaeden_requisition(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Bund oder Kanton haftet fuer Schaeden waehrend der Requisition (sofern nicht normale Abnuetzung und kein Versicherungsschutz)"
    reference = "SR 520.20 Art. 11 Abs. 3"

    def formula(person, period, parameters):
        requisition = person('requisition_voraussetzungen_erfuellt', period)
        nicht_normale_abnuetzung = not_(person('schaden_normale_abnuetzung', period))
        kein_versicherungsschutz = not_(person('versicherungsschutz_besteht', period))
        return requisition * (nicht_normale_abnuetzung + kein_versicherungsschutz)


class schaden_normale_abnuetzung(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Schaden ist auf normale Abnuetzung zurueckzufuehren"
    reference = "SR 520.20 Art. 11 Abs. 3"


class versicherungsschutz_besteht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Versicherungsschutz besteht fuer den Schaden"
    reference = "SR 520.20 Art. 11 Abs. 3"
