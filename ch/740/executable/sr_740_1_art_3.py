"""SR 740.1 Art. 3 - Verlagerungsziel

Generated from: ch/740/de/740.1.md

Hoechstens 650'000 Fahrten pro Jahr auf Transitstrassen im Alpengebiet.
Zwischenziel ab 2011: hoechstens 1 Million Fahrten pro Jahr.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# Input variables

class anzahl_fahrten_alpenquerender_gueterverkehr(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Fahrten alpenquerender Gueterschwerkehr auf Transitstrassen pro Jahr"
    reference = "SR 740.1 Art. 3 Abs. 1"


class gotthard_basistunnel_in_betrieb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Gotthard-Basistunnel ist in Betrieb"
    reference = "SR 740.1 Art. 3 Abs. 2"


class besonders_starke_wirtschaftsentwicklung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Besonders starke Wirtschafts- und Verkehrsentwicklung in diesem Jahr"
    reference = "SR 740.1 Art. 3 Abs. 3"


# Computed variables

class verlagerungsziel_erreicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Verlagerungsziel von hoechstens 650'000 Fahrten pro Jahr ist erreicht"
    reference = "SR 740.1 Art. 3 Abs. 1"

    def formula(self, period, parameters):
        fahrten = self('anzahl_fahrten_alpenquerender_gueterverkehr', period)
        return fahrten <= 650000


class zwischenziel_eingehalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Zwischenziel von hoechstens 1 Million Fahrten pro Jahr ist eingehalten (ab 2011)"
    reference = "SR 740.1 Art. 3 Abs. 4"

    def formula_2011(self, period, parameters):
        fahrten = self('anzahl_fahrten_alpenquerender_gueterverkehr', period)
        return fahrten <= 1000000


class verlagerungsziel_ueberschreitung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ueberschreitung des Verlagerungsziels zulaessig wegen besonders starker Wirtschaftsentwicklung"
    reference = "SR 740.1 Art. 3 Abs. 3"

    def formula(self, period, parameters):
        return self('besonders_starke_wirtschaftsentwicklung', period)
