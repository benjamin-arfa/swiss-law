"""SR 836.1 Art. 1a

Generated from: ch/836/de/836.1.md

Art. 1a: Bezugsberechtigte Personen - Eligible persons for agricultural
family allowances: employees in agricultural enterprises, family members
working on the farm (with exceptions for relatives in ascending/descending
line and sons/daughters-in-law expected to take over).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_landwirtschaftlicher_arbeitnehmer(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist in einem landwirtschaftlichen Betrieb gegen Entgelt in unselbstständiger Stellung tätig"
    reference = "SR 836.1 Art. 1a Abs. 1"


class ist_familienmitglied_betriebsleiter(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist Familienmitglied des Betriebsleiters und arbeitet im Betrieb mit"
    reference = "SR 836.1 Art. 1a Abs. 2"


class ist_verwandter_auf_absteigend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist Verwandter des Betriebsleiters in auf- oder absteigender Linie"
    reference = "SR 836.1 Art. 1a Abs. 2 lit. a"


class ist_schwiegerkind_mit_uebernahmeaussicht(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person ist Schwiegersohn/-tochter, der/die voraussichtlich den Betrieb übernimmt"
    reference = "SR 836.1 Art. 1a Abs. 2 lit. b"


class familie_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Person hält sich mit Familie in der Schweiz auf"
    reference = "SR 836.1 Art. 1a Abs. 3"


class anspruch_familienzulage_landwirtschaft(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Anspruch auf Familienzulagen als landwirtschaftlicher Arbeitnehmer (Art. 1a FLG)"
    reference = "SR 836.1 Art. 1a"

    def formula(person, period, parameters):
        # Abs. 1: landwirtschaftliche Arbeitnehmer
        arbeitnehmer = person('ist_landwirtschaftlicher_arbeitnehmer', period)
        # Abs. 2: Familienmitglieder, ausser Verwandte auf-/absteigend und
        # Schwiegerkinder mit Übernahmeaussicht
        familienmitglied = person('ist_familienmitglied_betriebsleiter', period)
        verwandter = person('ist_verwandter_auf_absteigend', period)
        schwiegerkind = person('ist_schwiegerkind_mit_uebernahmeaussicht', period)
        familienmitglied_berechtigt = familienmitglied * (1 - verwandter) * (1 - schwiegerkind)
        return arbeitnehmer + familienmitglied_berechtigt > 0
