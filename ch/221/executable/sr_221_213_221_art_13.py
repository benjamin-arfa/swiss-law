"""SR 221.213.221 Art. 13 – Zuschlag für längere Pachtdauer

Generated from: ch/221/de/221.213.221.md

Verabreden die Parteien eine Fortsetzungsdauer, welche die gesetzliche
Fortsetzungsdauer um mindestens drei Jahre übersteigt, ist ein Zuschlag
von 15 Prozent zum Pachtzins zulässig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

ZUSCHLAG_LAENGERE_PACHTDAUER = 0.15  # 15%
MINDEST_UEBERSTEIGUNG_JAHRE = 3


class vereinbarte_fortsetzungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vereinbarte Fortsetzungsdauer (Jahre)"
    reference = "SR 221.213.221 Art. 13"


class gesetzliche_fortsetzungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Fortsetzungsdauer (Jahre)"
    reference = "SR 221.213.221 Art. 13"


class zuschlag_laengere_pachtdauer_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuschlag für längere Pachtdauer ist zulässig"
    reference = "SR 221.213.221 Art. 13"

    def formula(person, period, parameters):
        vereinbart = person('vereinbarte_fortsetzungsdauer_jahre', period)
        gesetzlich = person('gesetzliche_fortsetzungsdauer_jahre', period)
        return vereinbart >= gesetzlich + MINDEST_UEBERSTEIGUNG_JAHRE


class zuschlag_laengere_pachtdauer_betrag(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zuschlag für längere Pachtdauer (CHF)"
    reference = "SR 221.213.221 Art. 13"

    def formula(person, period, parameters):
        import numpy as np
        pachtzins = person('hoechstzulaessiger_pachtzins_gewerbe', period)
        zulaessig = person('zuschlag_laengere_pachtdauer_zulaessig', period)
        return np.where(zulaessig, pachtzins * ZUSCHLAG_LAENGERE_PACHTDAUER, 0)
