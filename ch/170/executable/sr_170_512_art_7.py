"""SR 170.512 Art. 7

Generated from: ch/170/de/170.512.md

Ordentliche, dringliche und ausserordentliche Veröffentlichung.
Frist: Mindestens 5 Tage vor Inkrafttreten.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tage_vor_inkrafttreten_veroeffentlicht(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl Tage vor dem Inkrafttreten, an dem der Text veröffentlicht wurde"
    reference = "SR 170.512, Art. 7 Abs. 1"


class ist_ordentliche_veroeffentlichung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ordentliche Veröffentlichung (mind. 5 Tage vor Inkrafttreten) (Art. 7 Abs. 1 PublG)"
    reference = "SR 170.512, Art. 7 Abs. 1"

    def formula(person, period, parameters):
        tage = person('tage_vor_inkrafttreten_veroeffentlicht', period)
        return tage >= 5


class ist_dringliche_veroeffentlichung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Dringliche Veröffentlichung spätestens am Tag des Inkrafttretens (Art. 7 Abs. 3 PublG)"
    reference = "SR 170.512, Art. 7 Abs. 3"

    def formula(person, period, parameters):
        tage = person('tage_vor_inkrafttreten_veroeffentlicht', period)
        return (tage >= 0) * (tage < 5)


class publikationsplattform_nicht_zugaenglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Publikationsplattform ist nicht zugänglich (Art. 7 Abs. 4 PublG)"
    reference = "SR 170.512, Art. 7 Abs. 4"


class ist_ausserordentliche_veroeffentlichung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausserordentliche Veröffentlichung mit anderen Mitteln (Art. 7 Abs. 4 PublG)"
    reference = "SR 170.512, Art. 7 Abs. 4"

    def formula(person, period, parameters):
        return person('publikationsplattform_nicht_zugaenglich', period)
