"""SR 367.1 Art. 26

Generated from: ch/367/de/367.1.md

Abschluss der Vereinbarung und Inkrafttreten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anzahl_signatarkantone(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Kantone, die die Vereinbarung unterzeichnet haben"
    reference = "SR 367.1 Art. 26 Abs. 2"


class bund_hat_unterzeichnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Bund die Vereinbarung unterzeichnet"
    reference = "SR 367.1 Art. 26 Abs. 2"


class vereinbarung_kann_in_kraft_treten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kann die Vereinbarung in Kraft treten (Quorum erreicht)"
    reference = "SR 367.1 Art. 26 Abs. 2"

    def formula(person, period):
        kantone = person('anzahl_signatarkantone', period)
        bund = person('bund_hat_unterzeichnet', period)
        return (kantone >= 18) * bund
