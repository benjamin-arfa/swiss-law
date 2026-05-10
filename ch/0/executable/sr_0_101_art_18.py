"""SR 0.101 Art. 18

Generated from: ch/0/de/0.101.md

Limitation on use of restrictions on rights: The restrictions permitted
under the Convention shall not be applied for any purpose other than
those for which they have been prescribed.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_begrenzung_rechtseinschraenkungen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Einschraenkungen nur zu den vorgesehenen Zwecken erfolgen duerfen"
    reference = "SR 0.101 Art. 18"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
