"""SR 272.1 Art. 3

Generated from: ch/272/de/272.1.md

Anerkennungsverfahren: Entscheidgebuehr wird nach Zeitaufwand berechnet,
Stundenansatz 250 Franken.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class zustellplattform_pruefung_stunden(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Zeitaufwand fuer die Pruefung des Anerkennungsgesuchs in Stunden"
    reference = "SR 272.1 Art. 3 Abs. 3"


class stundenansatz_anerkennung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Stundenansatz fuer die Entscheidgebuehr in Franken (250 CHF)"
    reference = "SR 272.1 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        return 250.0


class entscheidgebuehr_anerkennung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Entscheidgebuehr fuer das Anerkennungsverfahren"
    reference = "SR 272.1 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        stunden = person('zustellplattform_pruefung_stunden', period)
        ansatz = person('stundenansatz_anerkennung', period)
        return stunden * ansatz
