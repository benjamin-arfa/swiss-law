"""SR 420.1 Art. 11

Generated from: ch/420/de/420.1.md

Akademien der Wissenschaften Schweiz - Reserven maximal 10 Prozent des jaehrlichen Bundesbeitrags.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class akademien_jaehrlicher_bundesbeitrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an die Akademien der Wissenschaften Schweiz"
    reference = "SR 420.1 Art. 11 Abs. 6bis"


class akademien_reserven_bestand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bestand der Reserven der Akademien"
    reference = "SR 420.1 Art. 11 Abs. 6bis"


class akademien_reserven_hoechstsatz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstsatz fuer Reserven der Akademien (10 Prozent des jaehrlichen Bundesbeitrags)"
    reference = "SR 420.1 Art. 11 Abs. 6bis"

    def formula(person, period, parameters):
        return person('akademien_jaehrlicher_bundesbeitrag', period) * 0.10


class akademien_reserven_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reserven der Akademien sind zulaessig (innerhalb des Hoechstsatzes)"
    reference = "SR 420.1 Art. 11 Abs. 6bis"

    def formula(person, period, parameters):
        return person('akademien_reserven_bestand', period) <= person('akademien_reserven_hoechstsatz', period)
