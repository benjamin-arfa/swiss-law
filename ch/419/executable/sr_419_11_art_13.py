"""SR 419.11 Art. 13

Generated from: ch/419/de/419.11.md

Maximale Hoehe der Finanzhilfen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class aufwendungen_kanton_fuer_programm(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Aufwendungen des Kantons fuer das kantonale Programm"
    reference = "SR 419.11 Art. 13"


class finanzhilfe_bund_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Hoehe der Finanzhilfe des Bundes"
    reference = "SR 419.11 Art. 13"


class finanzhilfe_hoehe_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hoehe der Finanzhilfe ist zulaessig (hoechstens kantonale Aufwendungen)"
    reference = "SR 419.11 Art. 13"

    def formula(person, period, parameters):
        bund = person('finanzhilfe_bund_betrag', period)
        kanton = person('aufwendungen_kanton_fuer_programm', period)
        return bund <= kanton
