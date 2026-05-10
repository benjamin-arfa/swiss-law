"""SR 442.133 Art. 6

Generated from: ch/442/de/442.133.md

Voraussetzungen fuer Beitraege an Talente: Alter 4-25, CH-Staatsangehoerig
oder Wohnsitz in der Schweiz, Einstufung als Talent durch Fachgremium.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class alter_talent(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter des Kindes/Jugendlichen"
    reference = "SR 442.133 Art. 6 Abs. 1 Bst. b"


class ist_schweizer_staatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person schweizerische Staatsangehoerigkeit hat"
    reference = "SR 442.133 Art. 6 Abs. 1 Bst. c"


class hat_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person Wohnsitz in der Schweiz hat"
    reference = "SR 442.133 Art. 6 Abs. 1 Bst. c"


class als_talent_eingestuft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vom Kanton als Talent eingestuft wurde"
    reference = "SR 442.133 Art. 6 Abs. 1 Bst. a"


class anspruch_talent_beitrag(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf einen Talent-Beitrag besteht"
    reference = "SR 442.133 Art. 6 Abs. 1"

    def formula(person, period, parameters):
        alter = person('alter_talent', period)
        ch = person('ist_schweizer_staatsangehoeriger', period)
        wohnsitz = person('hat_wohnsitz_schweiz', period)
        talent = person('als_talent_eingestuft', period)
        alter_ok = (alter >= 4) * (alter <= 25)
        nationalitaet_ok = ch + wohnsitz
        return alter_ok * nationalitaet_ok * talent
