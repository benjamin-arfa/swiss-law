"""SR 451.1 Art. 20

Generated from: ch/451/de/451.1.md
Artenschutz - Verbote fuer geschuetzte Pflanzen und Tiere.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pflanze_geschuetzt_anhang_2(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Pflanze gehoert zu geschuetzter Art nach Anhang 2 NHV"
    reference = "SR 451.1 Art. 20 Abs. 1"


class tier_geschuetzt_anhang_3(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier gehoert zu geschuetzter Art nach Anhang 3 NHV"
    reference = "SR 451.1 Art. 20 Abs. 2"


class hat_ausnahmebewilligung_artenschutz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausnahmebewilligung nach Art. 22 NHG oder Art. 20 Abs. 3 NHV liegt vor"
    reference = "SR 451.1 Art. 20 Abs. 3"


class handlung_pflanze_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handlung an geschuetzter Pflanze ist verboten (Pfluecken, Ausgraben etc.)"
    reference = "SR 451.1 Art. 20 Abs. 1"

    def formula(person, period, parameters):
        geschuetzt = person('pflanze_geschuetzt_anhang_2', period)
        ausnahme = person('hat_ausnahmebewilligung_artenschutz', period)
        return geschuetzt * not_(ausnahme)


class handlung_tier_verboten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Handlung an geschuetztem Tier ist verboten (Toeten, Verletzen, Fangen etc.)"
    reference = "SR 451.1 Art. 20 Abs. 2"

    def formula(person, period, parameters):
        geschuetzt = person('tier_geschuetzt_anhang_3', period)
        ausnahme = person('hat_ausnahmebewilligung_artenschutz', period)
        return geschuetzt * not_(ausnahme)
