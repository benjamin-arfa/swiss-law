"""SR 151.342 Art. 8

Generated from: ch/151/de/151.342.md

Billettautomaten und Entwerter: Maximale Hoehe der Bedienungselemente.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class max_hoehe_bedienungselemente_cm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Hoehe der Bedienungselemente von Billettautomaten (130 cm)"
    reference = "SR 151.342 Art. 8 Abs. 2"

    def formula(person, period, parameters):
        return 130.0


class max_hoehe_entwerterschlitz_cm(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Hoehe des Entwerterschlitzes (110 cm)"
    reference = "SR 151.342 Art. 8 Abs. 3"

    def formula(person, period, parameters):
        return 110.0
