"""SR 981 Art. 11

Generated from: ch/de/981.md

Enforcement: the Federal Council enforces this law and issues
implementing regulations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bundesrat_vollzieht_gesetz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat das Gesetz vollzieht und Ausfuehrungsvorschriften erlaesst"
    reference = "SR 981 Art. 11"
