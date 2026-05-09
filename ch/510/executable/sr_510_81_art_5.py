"""SR 510.81 Art. 5 - Steuerfreie Lieferung von Treibstoff

Generated from: ch/510/de/510.81.md

Anspruch auf von der Mineraloelsteuer befreiten Treibstoff fuer Land-,
Luft- und Wasserfahrzeuge haben die in der Schweiz befindlichen PfP-Truppen
und das zivile Gefolge fuer ihre dienstlichen Fahrzeuge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_dienstliches_fahrzeug_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein dienstliches Fahrzeug der PfP-Truppen oder des zivilen Gefolges handelt"
    reference = "SR 510.81 Art. 5"


class anspruch_steuerfreier_treibstoff_pfp(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Anspruch auf von der Mineraloelsteuer befreiten Treibstoff fuer PfP-Fahrzeuge besteht"
    reference = "SR 510.81 Art. 5"

    def formula(person, period, parameters):
        beguenstigt = person('ist_beguenstigter_pfp_zollbefreiung', period)
        dienstfahrzeug = person('ist_dienstliches_fahrzeug_pfp', period)
        return beguenstigt * dienstfahrzeug
