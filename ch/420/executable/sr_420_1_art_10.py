"""SR 420.1 Art. 10

Generated from: ch/420/de/420.1.md

Schweizerischer Nationalfonds - Reserven maximal 15 Prozent des jaehrlichen Bundesbeitrags.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class snf_jaehrlicher_bundesbeitrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrlicher Bundesbeitrag an den SNF"
    reference = "SR 420.1 Art. 10 Abs. 6"


class snf_reserven_bestand(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bestand der Reserven des SNF"
    reference = "SR 420.1 Art. 10 Abs. 6"


class snf_reserven_hoechstsatz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoechstsatz fuer Reserven des SNF (15 Prozent des jaehrlichen Bundesbeitrags)"
    reference = "SR 420.1 Art. 10 Abs. 6"

    def formula(person, period, parameters):
        return person('snf_jaehrlicher_bundesbeitrag', period) * 0.15


class snf_ausnahme_ueberschreitung_reserven(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat hat befristete Ausnahme fuer Ueberschreitung des Reserven-Hoechstsatzes bewilligt"
    reference = "SR 420.1 Art. 10 Abs. 6"


class snf_reserven_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reserven des SNF sind zulaessig (innerhalb des Hoechstsatzes oder Ausnahme bewilligt)"
    reference = "SR 420.1 Art. 10 Abs. 6"

    def formula(person, period, parameters):
        innerhalb_limit = person('snf_reserven_bestand', period) <= person('snf_reserven_hoechstsatz', period)
        ausnahme = person('snf_ausnahme_ueberschreitung_reserven', period)
        return innerhalb_limit + ausnahme * not_(innerhalb_limit)
