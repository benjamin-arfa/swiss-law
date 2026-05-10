"""SR 419.11 Art. 4

Generated from: ch/419/de/419.11.md

Gesuch - Anforderungen und Frist.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gesuch_eingereicht_bis_30_april(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesuch bis 30. April des letzten Jahres einer BFI-Periode eingereicht"
    reference = "SR 419.11 Art. 4 Abs. 2"


class gesuch_nachweis_kriterien_art_12_webig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nachweis der Kriterien nach Art. 12 WeBiG und Art. 1 WeBiV erbracht"
    reference = "SR 419.11 Art. 4 Abs. 1 Bst. a Ziff. 1"


class gesuch_jahresbericht_und_rechnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Jahresbericht und genehmigte Jahresrechnung eingereicht"
    reference = "SR 419.11 Art. 4 Abs. 1 Bst. a Ziff. 2"


class gesuch_leistungsbeschreibung_und_budget(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Genaue Beschreibung der Leistungen mit Budget eingereicht"
    reference = "SR 419.11 Art. 4 Abs. 1 Bst. b Ziff. 1"


class gesuch_nachgewiesener_bedarf(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bedarf nachgewiesen"
    reference = "SR 419.11 Art. 4 Abs. 1 Bst. b Ziff. 2"


class gesuch_vollstaendig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Gesuch ist vollstaendig"
    reference = "SR 419.11 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return (
            person('gesuch_eingereicht_bis_30_april', period) *
            person('gesuch_nachweis_kriterien_art_12_webig', period) *
            person('gesuch_jahresbericht_und_rechnung', period) *
            person('gesuch_leistungsbeschreibung_und_budget', period) *
            person('gesuch_nachgewiesener_bedarf', period)
        )
