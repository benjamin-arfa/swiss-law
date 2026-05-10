"""SR 453.0 Art. 13

Generated from: ch/453/de/453.0.md
Bescheinigungen fuer mehrmalige Grenzuebertritte - Befristung auf 3 Jahre.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bescheinigung_ausstellungsdatum_jahr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Jahr der Ausstellung der Bescheinigung fuer mehrmalige Grenzuebertritte"
    reference = "SR 453.0 Art. 13 Abs. 6"


class hat_wohnsitz_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wohnsitz oder Geschaeftssitz in der Schweiz"
    reference = "SR 453.0 Art. 13 Abs. 3"


class tiere_individuell_gekennzeichnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tiere sind individuell gekennzeichnet"
    reference = "SR 453.0 Art. 13 Abs. 1"


class bescheinigung_mehrmalige_grenzuebertritte_gueltig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bescheinigung fuer mehrmalige Grenzuebertritte ist noch gueltig (max 3 Jahre)"
    reference = "SR 453.0 Art. 13 Abs. 6"

    def formula(person, period, parameters):
        ausstellung = person('bescheinigung_ausstellungsdatum_jahr', period)
        aktuelles_jahr = period.start.year
        wohnsitz = person('hat_wohnsitz_schweiz', period)
        return ((aktuelles_jahr - ausstellung) <= 3) * wohnsitz
