"""SR 311.1 Art. 21

Generated from: ch/311/de/311.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bestrafung_gefaehrdet_schutzmassnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wuerde die Bestrafung eine Schutzmassnahme gefaehrden"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. a"


class schuld_und_tatfolgen_gering(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sind Schuld und Tatfolgen gering"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. b"


class wiedergutmachung_geleistet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat der Jugendliche Wiedergutmachung geleistet"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. c"


class schwer_betroffen_durch_tatfolgen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist der Jugendliche durch unmittelbare Tatfolgen schwer betroffen"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. d"


class bereits_genug_bestraft(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wurde der Jugendliche bereits von Eltern oder Dritten genug bestraft"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. e"


class lange_zeit_verstrichen_und_wohlverhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ist verhaeltnismaessig lange Zeit verstrichen und hat sich der Jugendliche wohlverhalten"
    reference = "SR 311.1 Art. 21 Abs. 1 lit. f"


class strafbefreiung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Liegen die Voraussetzungen fuer eine Strafbefreiung vor"
    reference = "SR 311.1 Art. 21"

    def formula(person, period, parameters):
        a = person('bestrafung_gefaehrdet_schutzmassnahme', period)
        b = person('schuld_und_tatfolgen_gering', period)
        c = person('wiedergutmachung_geleistet', period)
        d = person('schwer_betroffen_durch_tatfolgen', period)
        e = person('bereits_genug_bestraft', period)
        f = person('lange_zeit_verstrichen_und_wohlverhalten', period)
        return a + b + c + d + e + f > 0
