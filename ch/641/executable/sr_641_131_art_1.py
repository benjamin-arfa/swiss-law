"""SR 641.131 Art. 1

Generated from: ch/641/de/641.131.md

Exemption of Swiss franc bonds issued by foreign debtors from turnover tax.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_auslaendischer_schuldner(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Schuldner ein auslaendischer Schuldner ist"
    reference = "SR 641.131 Art. 1"


class gibt_schweizerfranken_anleihe_aus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Schweizerfranken-Anleihe ausgegeben wird"
    reference = "SR 641.131 Art. 1"


class umsatzabgabe_befreit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ausgabe von der Umsatzabgabe ausgenommen ist"
    reference = "SR 641.131 Art. 1"

    def formula(person, period, parameters):
        return (
            person('ist_auslaendischer_schuldner', period) *
            person('gibt_schweizerfranken_anleihe_aus', period)
        )
