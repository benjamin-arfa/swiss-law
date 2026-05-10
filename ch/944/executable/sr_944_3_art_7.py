"""SR 944.3 Art. 7-8

Generated from: ch/944/de/944.3.md

Preiserhoehungen und wesentliche Vertragsaenderungen bei Pauschalreisen.
Price increases only permitted under specific conditions and at least
3 weeks before departure. An increase >10% is a material contract change.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pauschalreise_preis_original(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Urspruenglich vertraglich festgelegter Preis der Pauschalreise (CHF)"
    reference = "SR 944.3 Art. 7"
    default_value = 0.0


class pauschalreise_preis_neu(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Neuer Preis nach Erhoehung (CHF)"
    reference = "SR 944.3 Art. 7"
    default_value = 0.0


class pauschalreise_erhoehung_mindestens_3_wochen_vor_abreise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Preiserhoehung mindestens 3 Wochen vor Abreise erfolgt"
    reference = "SR 944.3 Art. 7 Bst. b"
    default_value = False


class pauschalreise_erhoehung_gruende_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob zulaessige Gruende fuer die Erhoehung vorliegen (Befoerderungskosten, Abgaben, Wechselkurse)"
    reference = "SR 944.3 Art. 7 Bst. c"
    default_value = False


class pauschalreise_vertrag_sieht_erhoehung_vor(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Vertrag die Moeglichkeit einer Preiserhoehung ausdruecklich vorsieht"
    reference = "SR 944.3 Art. 7 Bst. a"
    default_value = False


class pauschalreise_preiserhoehung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Preiserhoehung zulaessig ist"
    reference = "SR 944.3 Art. 7"

    def formula(person, period, parameters):
        vertrag = person('pauschalreise_vertrag_sieht_erhoehung_vor', period)
        frist = person('pauschalreise_erhoehung_mindestens_3_wochen_vor_abreise', period)
        gruende = person('pauschalreise_erhoehung_gruende_zulaessig', period)
        return vertrag * frist * gruende


class pauschalreise_preiserhoehung_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Preiserhoehung in Prozent"
    reference = "SR 944.3 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        import numpy as np
        original = person('pauschalreise_preis_original', period)
        neu = person('pauschalreise_preis_neu', period)
        return np.where(original > 0, (neu - original) / original * 100, 0)


class pauschalreise_wesentliche_vertragsaenderung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine wesentliche Vertragsaenderung vorliegt (Preiserhoehung >10%)"
    reference = "SR 944.3 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        erhoehung = person('pauschalreise_preiserhoehung_prozent', period)
        return erhoehung > 10
