"""SR 251 Art. 54

Generated from: ch/de/251.md

Criminal sanction: intentional violation of consensual agreements
or enforceable orders is punishable by fine up to CHF 100,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vorsaetzliche_widerhandlung_anordnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine vorsaetzliche Widerhandlung gegen eine einvernehmliche Regelung oder Verfuegung vorliegt"
    reference = "SR 251 Art. 54"


class strafbusse_art54_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse nach Art. 54 (CHF)"
    reference = "SR 251 Art. 54"

    def formula(person, period, parameters):
        return person('vorsaetzliche_widerhandlung_anordnung', period) * 100000.0
