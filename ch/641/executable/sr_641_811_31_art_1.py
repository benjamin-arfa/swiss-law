"""SR 641.811.31 Art. 1

Generated from: ch/641/de/641.811.31.md

Refund eligibility: transports of unprocessed roundwood, industrial/energy
forest wood, and industrial/energy residual wood qualify for heavy vehicle
tax refunds.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class transport_stammholz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob unverarbeitetes Wald- oder Saegerundholz (Mindestlaenge ca. 1 m) transportiert wird"
    reference = "SR 641.811.31 Art. 1 Bst. a"


class transport_industrie_energie_waldholz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Industrie- und Energie-Waldholz transportiert wird"
    reference = "SR 641.811.31 Art. 1 Bst. b"


class transport_industrie_energie_restholz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Industrie- und Energie-Restholz transportiert wird"
    reference = "SR 641.811.31 Art. 1 Bst. c"


class rueckerstattung_berechtigt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Transport zur Rueckerstattung der Schwerverkehrsabgabe berechtigt"
    reference = "SR 641.811.31 Art. 1"

    def formula(person, period, parameters):
        return (
            person('transport_stammholz', period) +
            person('transport_industrie_energie_waldholz', period) +
            person('transport_industrie_energie_restholz', period)
        ) > 0
