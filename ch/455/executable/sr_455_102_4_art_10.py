"""SR 455.102.4 Art. 10

Generated from: ch/455/de/455.102.4.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Enum for prohibited breed forms
VERBOTENE_ZUCHTFORMEN = [
    'tanzmaeuse',
    'goldfisch_blasenaugen',
    'goldfisch_himmelsgucker',
    'goldfisch_teleskopaugen',
    'zwerghund_unter_1500g',
    'kaenguru_katze',
    'reptil_enigma_syndrom',
    'blauweisse_belgier_reinzucht',
]


class ist_tanzmaus(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier ist eine Tanzmaus (Art. 10 lit. a SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. a"


class ist_goldfisch_verbotene_zuchtform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Goldfisch der Zuchtform Blasenaugen, Himmelsgucker oder Teleskopaugen (Art. 10 lit. b SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. b"


class ist_zwerghund_unter_1500g(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zwerghund der ausgewachsen weniger als 1500 Gramm wiegt (Art. 10 lit. c SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. c"


class gewicht_ausgewachsen_gramm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gewicht des ausgewachsenen Tieres in Gramm"
    reference = "SR 455.102.4 Art. 10 lit. c"


class ist_kaenguru_katze(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Katze mit extrem verkuerzten Vorderbeinen (Kaenguru-Katze) (Art. 10 lit. d SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. d"


class ist_reptil_mit_enigma_syndrom(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Reptil mit Enigma-Syndrom (Art. 10 lit. e SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. e"


class ist_blauweisse_belgier_reinzucht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Rind der Rasse Blauweisse Belgier in Reinzucht (Art. 10 lit. f SR 455.102.4)"
    reference = "SR 455.102.4 Art. 10 lit. f"


class ist_verbotene_zuchtform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier gehoert zu einer verbotenen Zuchtform nach Art. 10 SR 455.102.4"
    reference = "SR 455.102.4 Art. 10"

    def formula(person, period, parameters):
        return (
            person('ist_tanzmaus', period)
            + person('ist_goldfisch_verbotene_zuchtform', period)
            + person('ist_zwerghund_unter_1500g', period)
            + person('ist_kaenguru_katze', period)
            + person('ist_reptil_mit_enigma_syndrom', period)
            + person('ist_blauweisse_belgier_reinzucht', period)
        )
