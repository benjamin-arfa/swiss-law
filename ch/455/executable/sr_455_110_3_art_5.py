"""SR 455.110.3 Art. 5

Generated from: ch/455/de/455.110.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class tier_wird_regelmaessig_in_manege_eingesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Wildtier wird haeufig und regelmaessig in der Manege ausgebildet, trainiert oder vorgefuehrt"
    reference = "SR 455.110.3 Art. 5 Abs. 1"


class innengehege_mindestflaeche_m2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Mindestflaeche des Innengeheges nach Anhang 2 TSchV in m2"
    reference = "SR 455.110.3 Art. 5 Abs. 1"


class innengehege_tatsaechliche_flaeche_m2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tatsaechliche Flaeche des Innengeheges in m2"
    reference = "SR 455.110.3 Art. 5 Abs. 1"


class aussengehege_tatsaechliche_flaeche_m2(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Tatsaechliche Flaeche des Aussengeheges in m2"
    reference = "SR 455.110.3 Art. 5 Abs. 2"


class beschaeftigung_mindestens_3_mal_taeglich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tier wird mindestens 3x taeglich art- und beduerfnisgerecht beschaeftigt"
    reference = "SR 455.110.3 Art. 5 Abs. 3"


class zirkustier_innengehege_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Innengehege fuer Zirkustier konform (max 30% Unterschreitung) nach Art. 5 Abs. 1 SR 455.110.3"
    reference = "SR 455.110.3 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        in_manege = person('tier_wird_regelmaessig_in_manege_eingesetzt', period)
        mindest = person('innengehege_mindestflaeche_m2', period)
        tatsaechlich = person('innengehege_tatsaechliche_flaeche_m2', period)
        # Darf max 30% unter Mindestflaeche liegen wenn regelmaessig in Manege
        min_erlaubt = mindest * 0.7
        return where(in_manege, tatsaechlich >= min_erlaubt, tatsaechlich >= mindest)


class zirkustier_aussengehege_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Aussengehege fuer Zirkustier konform (min = Innengehege nach Abs.1) nach Art. 5 Abs. 2 SR 455.110.3"
    reference = "SR 455.110.3 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        innen = person('innengehege_tatsaechliche_flaeche_m2', period)
        aussen = person('aussengehege_tatsaechliche_flaeche_m2', period)
        return aussen >= innen


class zirkustier_beschaeftigungspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Beschaeftigungspflicht erfuellt bei unterschrittener Mindestflaeche nach Art. 5 Abs. 3 SR 455.110.3"
    reference = "SR 455.110.3 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        mindest = person('innengehege_mindestflaeche_m2', period)
        tatsaechlich = person('innengehege_tatsaechliche_flaeche_m2', period)
        unterschritten = tatsaechlich < mindest
        beschaeftigt = person('beschaeftigung_mindestens_3_mal_taeglich', period)
        return not_(unterschritten) + (unterschritten * beschaeftigt)
