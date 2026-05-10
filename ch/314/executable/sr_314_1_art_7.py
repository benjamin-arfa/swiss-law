"""SR 314.1 Art. 7

Generated from: ch/314/de/314.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class fahrzeugfuehrer_nicht_angetroffen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Fahrzeugfuehrerin oder der Fahrzeugfuehrer wurde nicht anlaesslich der Widerhandlung angetroffen"
    reference = "SR 314.1 Art. 7 Abs. 1"


class ist_fahrzeughalter(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person ist als Fahrzeughalterin oder Fahrzeughalter eingetragen"
    reference = "SR 314.1 Art. 7 Abs. 1"


class halter_nennt_fahrer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Halterin oder der Halter nennt die Person, die die Widerhandlung begangen hat"
    reference = "SR 314.1 Art. 7 Abs. 4"


class fahrzeug_gegen_willen_benutzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Fahrzeug wurde gegen den Willen der Halterin/des Halters benutzt und konnte trotz Sorgfalt nicht verhindert werden"
    reference = "SR 314.1 Art. 7 Abs. 5"


class halterhaftung_busse(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Busse wird der Fahrzeughalterin oder dem Fahrzeughalter auferlegt (Halterhaftung)"
    reference = "SR 314.1 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        nicht_angetroffen = person('fahrzeugfuehrer_nicht_angetroffen', period)
        ist_halter = person('ist_fahrzeughalter', period)
        nennt_fahrer = person('halter_nennt_fahrer', period)
        gegen_willen = person('fahrzeug_gegen_willen_benutzt', period)
        return nicht_angetroffen * ist_halter * not_(nennt_fahrer) * not_(gegen_willen)
