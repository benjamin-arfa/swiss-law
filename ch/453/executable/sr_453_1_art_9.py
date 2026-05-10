"""SR 453.1 Art. 9

Generated from: ch/453/de/453.1.md
Souvenirs und deren Hoechstmengen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kaviar_menge_g(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Menge Kaviar in Gramm"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. a"


class krokodil_erzeugnisse_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Erzeugnisse von Krokodilarten"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. b"


class queen_conch_gehaeuse_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Gehaeuse der Fechterschnecke"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. c"


class moerdermuschel_kg(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gewicht Moerdermuschel-Schalen in kg"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. d"


class seepferdchen_anzahl(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Seepferdchen"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. e"


class kaviar_souvenir_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Kaviar-Souvenir innerhalb Hoechstmenge (125g pro Person/Tag)"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. a"

    def formula(person, period, parameters):
        menge = person('kaviar_menge_g', period)
        return menge <= 125.0


class krokodil_souvenir_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Krokodil-Souvenir innerhalb Hoechstmenge (2 pro Person/Tag)"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. b"

    def formula(person, period, parameters):
        anzahl = person('krokodil_erzeugnisse_anzahl', period)
        return anzahl <= 2


class seepferdchen_souvenir_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Seepferdchen-Souvenir innerhalb Hoechstmenge (4 pro Person/Tag)"
    reference = "SR 453.1 Art. 9 Abs. 2 Bst. e"

    def formula(person, period, parameters):
        anzahl = person('seepferdchen_anzahl', period)
        return anzahl <= 4
