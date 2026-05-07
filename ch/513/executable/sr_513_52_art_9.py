"""SR 513.52 Art. 9

Generated from: ch/513/de/513.52.md
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class rkd_ist_bewaffnet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "RKD-Angehoerige ist bewaffnet"


class rkd_hat_gesuch_bewaffnung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Hat Gesuch um Bewaffnung mit Pistole gestellt"


class rkd_bewaffnung_grundsatz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "RKD-Angehoerige leisten Dienst grundsaetzlich unbewaffnet (Art. 9 Abs. 1 SR 513.52)"
    reference = "SR 513.52 Art. 9"

    def formula(person, period, parameters):
        # Grundsaetzlich unbewaffnet
        return True


class rkd_darf_pistole_erhalten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "RKD-Angehoerige darf auf Gesuch mit Pistole ausgeruestet werden (Art. 9 Abs. 2 SR 513.52)"
    reference = "SR 513.52 Art. 9"

    def formula(person, period, parameters):
        # Auf Gesuch kann die Armee sie mit der Pistole ausruesten
        return person('rkd_hat_gesuch_bewaffnung', period)


class rkd_ausserdienstliche_schiesspflicht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "RKD-Angehoerige unterstehen der obligatorischen ausserdienstlichen Schiesspflicht (Art. 9 Abs. 3 SR 513.52)"
    reference = "SR 513.52 Art. 9"

    def formula(person, period, parameters):
        # Angehoerige des RKD unterstehen NICHT der obligatorischen
        # ausserdienstlichen Schiesspflicht
        return False
