"""SR 814.01 Art. 1

Generated from: ch/814/de/814.01.md

Zweck: Schutz von Menschen, Tieren, Pflanzen und deren Lebensraeumen
gegen schaedliche oder laestige Einwirkungen (USG).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class usg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Umweltschutzgesetz anwendbar ist"
    reference = "SR 814.01 Art. 1"

    def formula(person, period, parameters):
        return True
