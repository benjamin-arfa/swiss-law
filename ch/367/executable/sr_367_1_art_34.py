"""SR 367.1 Art. 34

Generated from: ch/367/de/367.1.md

Finanzielle Folgen des Austritts und der Aufloesung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bilanzkonto_saldo(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Saldo des Bilanzkontos der Partei"
    reference = "SR 367.1 Art. 34 Abs. 2"


class anspruch_auf_positiven_saldo(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat die Partei Anspruch auf einen positiven Saldo bei Austritt/Aufloesung"
    reference = "SR 367.1 Art. 34 Abs. 2"

    def formula(person, period):
        saldo = person('bilanzkonto_saldo', period)
        return saldo > 0


class rueckerstattung_geleisteter_beitraege(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Werden geleistete Beitraege bei Austritt zurueckerstattet"
    reference = "SR 367.1 Art. 34 Abs. 1"

    def formula(person, period):
        # Geleistete Beitraege werden nicht zurueckerstattet
        return False
