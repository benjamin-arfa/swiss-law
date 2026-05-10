"""SR 362 Art. 4

Generated from: ch/de/362.md

Optional treaty referendum and entry into force provisions for the
Schengen/Dublin federal decree.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class schengen_dublin_fakultatives_referendum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Beschluss dem fakultativen Staatsvertragsreferendum untersteht"
    reference = "SR 362 Art. 4 Abs. 1"

    def formula(person, period, parameters):
        return True


class bundesrat_inkrafttreten_art3_bestimmt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesrat das Inkrafttreten der in Art. 3 aufgefuehrten Bundesgesetze bestimmt"
    reference = "SR 362 Art. 4 Abs. 2"
