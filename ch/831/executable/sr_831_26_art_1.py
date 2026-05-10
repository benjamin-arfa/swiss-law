"""SR 831.26 Art. 1

Generated from: ch/831/de/831.26.md

Purpose: This law aims to guarantee disabled persons access to
institutions promoting their integration.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_invalide_person(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als invalide Person gilt"
    reference = "SR 831.26 Art. 1"


class zugang_zu_eingliederungsinstitution(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der invaliden Person der Zugang zu einer Eingliederungsinstitution gewaehrleistet ist"
    reference = "SR 831.26 Art. 1"
