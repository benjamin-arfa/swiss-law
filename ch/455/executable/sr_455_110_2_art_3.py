"""SR 455.110.2 Art. 3

Generated from: ch/455/de/455.110.2.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class ausladerampe_neigung_grad(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Neigung der Ausladerampe in Grad"
    reference = "SR 455.110.2 Art. 3 Abs. 3"


class ausladerampe_hat_trittsicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausladerampe ist mit Trittsicherung versehen"
    reference = "SR 455.110.2 Art. 3 Abs. 3"


class ausladerampe_neigung_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Neigung der Ausladerampe ist zulaessig (max 20 Grad) nach Art. 3 Abs. 3 SR 455.110.2"
    reference = "SR 455.110.2 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        neigung = person('ausladerampe_neigung_grad', period)
        return neigung <= 20


class ausladerampe_trittsicherung_erforderlich(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Trittsicherung an Ausladerampe erforderlich (Gefaelle ueber 10 Grad) nach Art. 3 Abs. 3 SR 455.110.2"
    reference = "SR 455.110.2 Art. 3 Abs. 3"

    def formula(person, period, parameters):
        neigung = person('ausladerampe_neigung_grad', period)
        return neigung > 10


class ausladerampe_konform(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ausladerampe entspricht den Anforderungen nach Art. 3 SR 455.110.2"
    reference = "SR 455.110.2 Art. 3"

    def formula(person, period, parameters):
        neigung_ok = person('ausladerampe_neigung_zulaessig', period)
        trittsicherung_noetig = person('ausladerampe_trittsicherung_erforderlich', period)
        hat_trittsicherung = person('ausladerampe_hat_trittsicherung', period)
        return neigung_ok * (not_(trittsicherung_noetig) + hat_trittsicherung)
