"""SR 0.101 Art. 17

Generated from: ch/0/de/0.101.md

Prohibition of abuse of rights: Nothing in the Convention may be
interpreted as implying any right to engage in any activity aimed at
the destruction of Convention rights or at their limitation to a greater
extent than is provided for.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_verbot_rechtsmissbrauch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verbot des Missbrauchs der Konventionsrechte gilt"
    reference = "SR 0.101 Art. 17"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
