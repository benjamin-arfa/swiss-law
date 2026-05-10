"""SR 981 Art. 14

Generated from: ch/de/981.md

Referendum and entry into force: subject to optional referendum.
Entry into force determined by the Federal Council (1 January 1981).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class entschaedigungsgesetz_fakultatives_referendum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Gesetz dem fakultativen Referendum untersteht"
    reference = "SR 981 Art. 14 Abs. 1"

    def formula(person, period, parameters):
        return True


class entschaedigungsgesetz_inkrafttreten_bundesrat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat das Inkrafttreten bestimmt (1. Januar 1981)"
    reference = "SR 981 Art. 14 Abs. 2"
