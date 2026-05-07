"""SR 611.015.3 Art. 7

Generated from: ch/611/de/611.015.3.md

SKB-Verordnung - Art. 7: Konto, Sparen und Zahlen.
Die SKB bietet pro berechtigte Person ein Konto an.
Dienstleistungen: Sparen, Zahlungsverkehr und Debitkarte.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class skb_konto_pro_person(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anzahl SKB-Konten pro berechtigte Person (Art. 7 Abs. 1)"
    reference = "SR 611.015.3 Art. 7 Abs. 1"

    def formula(person, period, parameters):
        # Art. 7 Abs. 1: Die SKB bietet pro berechtigte Person ein Konto an.
        return 1
