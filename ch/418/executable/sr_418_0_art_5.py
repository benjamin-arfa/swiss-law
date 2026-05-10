"""SR 418.0 Art. 5

Generated from: ch/418/de/418.0.md

Voraussetzungen fuer die Anerkennung von Angeboten in der beruflichen Grundbildung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class berufsbildung_genuegend_lernende(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebote berufliche Grundbildung weisen genuegend Lernende auf"
    reference = "SR 418.0 Art. 5 Bst. a"


class berufsbildung_anerkannter_abschluss(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot fuehrt zu EFZ/EBA"
    reference = "SR 418.0 Art. 5 Bst. b"


class berufsbildung_gastland_anerkennung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Abschluss im Gastland als Sek-II-Abschluss anerkannt"
    reference = "SR 418.0 Art. 5 Bst. c"


class berufsbildung_schulische_bildung_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Vermittelt schulische Bildung im Sinne der CH-Berufsbildungsgesetzgebung"
    reference = "SR 418.0 Art. 5 Bst. d"


class berufsbildung_zusammenarbeit_verbaende(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zusammenarbeit mit CH-Berufsverbaenden und Unternehmen im Gastland"
    reference = "SR 418.0 Art. 5 Bst. e"


class berufsbildung_beitragsberechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Berufliche Grundbildung als beitragsberechtigt anerkannt"
    reference = "SR 418.0 Art. 5"

    def formula(person, period, parameters):
        return (
            person('berufsbildung_genuegend_lernende', period) *
            person('berufsbildung_anerkannter_abschluss', period) *
            person('berufsbildung_gastland_anerkennung', period) *
            person('berufsbildung_schulische_bildung_konform', period) *
            person('berufsbildung_zusammenarbeit_verbaende', period)
        )
