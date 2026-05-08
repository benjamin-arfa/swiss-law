"""SR 919.118 Art. 6

Generated from: ch/919/de/919.118.md

Vergleichseinkommen.

Abs. 1: Berechnung auf Grundlage der BFS-Lohnstrukturerhebung (alle 2 Jahre)
und der Entwicklung des Lohnindexes.

Abs. 2: Vergleichseinkommen = Zentralwert der Loehne aller Angestellten im
Sekundaer- und Tertiaersektor. Umfasst standardisierten Jahresbruttolohn
sowie besondere Verguetungen und den 13. Monatslohn.

Abs. 3: Teilzeitloehne werden in Vollzeitaequivalente umgerechnet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vergleichseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vergleichseinkommen (Zentralwert Loehne Sekundaer-/Tertiaersektor, CHF)"
    reference = "SR 919.118 Art. 6 Abs. 2"

    def formula(person, period, parameters):
        return parameters(period).sr_919_118.vergleichseinkommen_zentralwert


class arbeitsverdienst_vergleich_ratio(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Verhaeltnis Arbeitsverdienst zu Vergleichseinkommen"
    reference = "SR 919.118 Art. 5-6"

    def formula(person, period, parameters):
        arbeitsverdienst = person('landwirtschaftlicher_arbeitsverdienst', period)
        vergleich = person('vergleichseinkommen', period)
        return where(vergleich > 0, arbeitsverdienst / vergleich, 0)
