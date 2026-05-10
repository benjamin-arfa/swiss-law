"""SR 272.11 Art. 4

Generated from: ch/272/de/272.11.md

Bericht- und Meldepflichten: Unterlagen sind alle drei Jahre
zu aktualisieren. Aenderungen sind umgehend zu melden.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aktualisierungszyklus_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aktualisierungszyklus fuer die Unterlagen in Jahren (3 Jahre)"
    reference = "SR 272.11 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return 3


class letzte_aktualisierung_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum der letzten Aktualisierung der Unterlagen"
    reference = "SR 272.11 Art. 4 Abs. 1"


class aenderung_an_zustellplattform(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Aenderung an der Zustellplattform vorgenommen wurde"
    reference = "SR 272.11 Art. 4 Abs. 2"


class meldepflicht_ausgeloest(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine umgehende Meldepflicht an das BJ besteht"
    reference = "SR 272.11 Art. 4 Abs. 2"

    def formula(person, period, parameters):
        return person('aenderung_an_zustellplattform', period)
