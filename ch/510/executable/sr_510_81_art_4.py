"""SR 510.81 Art. 4 - Zoll- und steuerfreie Einfuhr von Mineraloelprodukten

Generated from: ch/510/de/510.81.md

Mineraloelprodukte fuer den dienstlichen Gebrauch der Land-, Luft- und
Wasserfahrzeuge der PfP-Truppen und des zivilen Gefolges sind zollfrei.
Die Zollbefreiung schliesst MWST und Mineraloelsteuer ein.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_mineraloelprodukt_pfp_dienstlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um Mineraloelprodukte fuer den dienstlichen Gebrauch der Fahrzeuge von PfP-Truppen handelt"
    reference = "SR 510.81 Art. 4 Abs. 1"


class zollbefreiung_mineraloelprodukte_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Zollbefreiung fuer Mineraloelprodukte der PfP-Truppen besteht (inkl. MWST und Mineraloelsteuer)"
    reference = "SR 510.81 Art. 4"

    def formula(person, period, parameters):
        beguenstigt = person('ist_beguenstigter_pfp_zollbefreiung', period)
        dienstlich = person('ist_mineraloelprodukt_pfp_dienstlich', period)
        return beguenstigt * dienstlich
