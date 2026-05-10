"""SR 0.101 Art. 3

Generated from: ch/0/de/0.101.md

Prohibition of torture: No one shall be subjected to torture or to
inhuman or degrading treatment or punishment.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class emrk_verbot_folter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verbot der Folter oder unmenschlicher oder erniedrigender Behandlung gilt"
    reference = "SR 0.101 Art. 3"

    def formula(person, period, parameters):
        return person('emrk_hoheitsgewalt_unterstellt', period)
