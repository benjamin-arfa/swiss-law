"""SR 198.1 Art. 5

Generated from: ch/198/de/198.1.md

Zustaendige Behoerde nach den Anlagen II und V: The EDA authorises:
entering specially protected Antarctic areas, taking or interference with
native fauna/flora, and introducing non-native species/pests/diseases.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betreten_besonders_geschuetztes_gebiet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Betreten eines besonders geschuetzten Gebiets der Antarktis (Art. 7 Anlage V)"
    reference = "SR 198.1 Art. 5 Bst. a"


class entnahme_heimische_tier_pflanzenwelt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Entnahme aus der heimischen Tier- und Pflanzenwelt oder schaedliches Einwirken (Art. 3 Anlage II)"
    reference = "SR 198.1 Art. 5 Bst. b"


class einbringen_nicht_heimische_arten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Einbringen von nicht heimischen Arten, Schaedlingen oder Krankheiten (Art. 4 Abs. 1 Anlage II)"
    reference = "SR 198.1 Art. 5 Bst. c"


class eda_bewilligung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine Bewilligung des EDA ist erforderlich"
    reference = "SR 198.1 Art. 5"

    def formula(person, period, parameters):
        geschuetzt = person('betreten_besonders_geschuetztes_gebiet', period)
        entnahme = person('entnahme_heimische_tier_pflanzenwelt', period)
        einbringen = person('einbringen_nicht_heimische_arten', period)
        return geschuetzt + entnahme + einbringen > 0
