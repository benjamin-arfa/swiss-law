"""SR 151.3 Art. 10

Generated from: ch/151/de/151.3.md

Unentgeltlichkeit des Verfahrens.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class mutwillige_prozessfuehrung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich eine Partei mutwillig oder leichtsinnig verhaelt"
    reference = "SR 151.3 Art. 10 Abs. 2"


class verfahren_unentgeltlich_behig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Verfahren unentgeltlich ist nach BehiG Art. 10"
    reference = "SR 151.3 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        mutwillig = person('mutwillige_prozessfuehrung', period)
        return 1 - mutwillig
