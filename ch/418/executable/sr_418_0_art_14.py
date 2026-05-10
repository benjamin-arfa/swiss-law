"""SR 418.0 Art. 14

Generated from: ch/418/de/418.0.md

Formen und Voraussetzungen der Unterstuetzung anderer Bildungsformen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class traegerschaft_angemessene_eigenleistung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Traegerschaft erbringt angemessene Eigenleistung"
    reference = "SR 418.0 Art. 14 Abs. 3 Bst. a"


class angebot_angemessener_gesamtbestand(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot weist angemessenen Gesamtbestand auf"
    reference = "SR 418.0 Art. 14 Abs. 3 Bst. b"


class angebot_angemessene_anzahl_ch_schueler(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot weist angemessene Anzahl CH-Schueler auf"
    reference = "SR 418.0 Art. 14 Abs. 3 Bst. c"


class angebot_politisch_religioes_neutral(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot ist politisch und religioes neutral"
    reference = "SR 418.0 Art. 14 Abs. 3 Bst. d"


class angebot_nicht_gewinnorientiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Angebot ermoeglicht nachweislich keinen Gewinn"
    reference = "SR 418.0 Art. 14 Abs. 3 Bst. e"


class unterstuetzung_andere_bildungsformen_berechtigt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Voraussetzungen fuer Bundesunterstuetzung anderer Bildungsformen erfuellt"
    reference = "SR 418.0 Art. 14 Abs. 3"

    def formula(person, period, parameters):
        return (
            person('traegerschaft_angemessene_eigenleistung', period) *
            person('angebot_angemessener_gesamtbestand', period) *
            person('angebot_angemessene_anzahl_ch_schueler', period) *
            person('angebot_politisch_religioes_neutral', period) *
            person('angebot_nicht_gewinnorientiert', period)
        )
