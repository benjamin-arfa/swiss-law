"""SR 131.214 Art. 1

Generated from: ch/131/de/131.214.md

Souveränität: Der Kanton Uri ist ein souveräner Stand der Schweizerischen
Eidgenossenschaft. Er arbeitet mit Bund und Kantonen zusammen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kanton_uri_souveraen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Uri ein souveräner Stand der Eidgenossenschaft ist"
    reference = "SR 131.214 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return True


class kanton_uri_zusammenarbeit_bund(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Kanton Uri mit Bund und Kantonen zusammenarbeitet"
    reference = "SR 131.214 Art. 1 Abs. 2"

    def formula(person, period, parameters):
        return True
