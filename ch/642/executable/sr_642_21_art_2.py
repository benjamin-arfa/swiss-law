"""SR 642.21 Art. 2 - Kantonsanteil (Cantonal Share)

Generated from: ch/642/de/642.21.md

Art. 2: The cantons receive 10% of the annual net yield of the
withholding tax. This is distributed at the beginning of the
following year based on resident population (last census).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vstg_reinertrag_jaehrlich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher Reinertrag der Verrechnungssteuer (CHF)"
    reference = "SR 642.21 Art. 2 Abs. 1"
    default_value = 0.0


class vstg_kantonsanteil(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anteil der Kantone am Reinertrag der Verrechnungssteuer (CHF)"
    reference = "SR 642.21 Art. 2 Abs. 1"

    def formula(person, period, parameters):
        reinertrag = person('vstg_reinertrag_jaehrlich', period)
        rate = parameters(period).sr_642_21.kantonsanteil_rate
        return reinertrag * rate
