"""SR 514.54 Art. 9b

Generated from: ch/514/de/514.54.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class waffenerwerbsschein_gueltigkeitsdauer_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gueltigkeitsdauer des Waffenerwerbsscheins in Monaten (Art. 9b Abs. 3 SR 514.54)"
    reference = "SR 514.54 Art. 9b"

    def formula(person, period, parameters):
        # Der Waffenerwerbsschein ist sechs Monate gueltig
        return 6


class waffenerwerbsschein_max_verlaengerung_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Verlaengerung des Waffenerwerbsscheins in Monaten (Art. 9b Abs. 3 SR 514.54)"
    reference = "SR 514.54 Art. 9b"

    def formula(person, period, parameters):
        # Die zustaendige Behoerde kann die Gueltigkeit um hoechstens
        # drei Monate verlaengern
        return 3


class waffenerwerbsschein_gilt_fuer_ganze_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Waffenerwerbsschein gilt fuer die ganze Schweiz (Art. 9b Abs. 1 SR 514.54)"
    reference = "SR 514.54 Art. 9b"

    def formula(person, period, parameters):
        return True


class waffenerwerbsschein_berechtigt_zum_erwerb_einer_waffe(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ein Waffenerwerbsschein berechtigt zum Erwerb einer einzigen Waffe (Art. 9b Abs. 1 SR 514.54)"
    reference = "SR 514.54 Art. 9b"

    def formula(person, period, parameters):
        return True
