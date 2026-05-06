"""SR 235.1 Art. 26b

Generated from: ch/235/de/235.1.md

Nebenbeschaeftigung des Beauftragten: Grundsaetzliches Verbot,
Ausnahme durch Bundesrat.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class dsg_beauftragter_nebenbeschaeftigung_bewilligt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Bundesrat hat Nebenbeschaeftigung des Beauftragten bewilligt"
    reference = "SR 235.1 Art. 26b Abs. 2"


class dsg_nebenbeschaeftigung_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Nebenbeschaeftigung des Beauftragten ist zulaessig"
    reference = "SR 235.1 Art. 26b"

    def formula(person, period, parameters):
        # Grundsaetzlich verboten (Abs. 1), Ausnahme durch BR (Abs. 2)
        return person('dsg_beauftragter_nebenbeschaeftigung_bewilligt', period)
