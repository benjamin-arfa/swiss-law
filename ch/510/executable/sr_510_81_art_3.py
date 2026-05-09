"""SR 510.81 Art. 3 - Zoll- und steuerfreie Einfuhr von Ausruestung und Verpflegung

Generated from: ch/510/de/510.81.md

PfP-Truppen koennen voruebergehend ihre Ausruestung zollfrei einfuehren.
Angemessene Mengen von Verpflegung und Versorgungsguetern koennen zollfrei
eingefuehrt werden, sofern ausschliesslich von PfP-Truppen, ihren Mitgliedern
und dem zivilen Gefolge verwendet.
Die Zollbefreiung schliesst MWST und Automobilsteuer ein.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_ausruestung_pfp_truppe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um Ausruestung einer PfP-Truppe handelt (voruebergehende Einfuhr)"
    reference = "SR 510.81 Art. 3 Abs. 1"


class ist_verpflegung_versorgungsgut_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um Verpflegung, Versorgungsgueter oder sonstige Waren fuer PfP-Truppen handelt"
    reference = "SR 510.81 Art. 3 Abs. 2"


class ausschliesslich_pfp_verwendung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Waren ausschliesslich von den PfP-Truppen, ihren Mitgliedern und dem zivilen Gefolge verwendet werden"
    reference = "SR 510.81 Art. 3 Abs. 2"


class zollbefreiung_ausruestung_verpflegung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Zollbefreiung fuer Ausruestung und Verpflegung der PfP-Truppen besteht (inkl. MWST und Automobilsteuer)"
    reference = "SR 510.81 Art. 3"

    def formula(person, period, parameters):
        ausruestung = person('ist_ausruestung_pfp_truppe', period)
        verpflegung = person('ist_verpflegung_versorgungsgut_pfp', period) * person('ausschliesslich_pfp_verwendung', period)
        return (ausruestung + verpflegung) > 0
