"""SR 272.1 Art. 8b

Generated from: ch/272/de/272.1.md

Wahrung einer Frist: Fuer die Fristwahrung ist der Zeitpunkt massgebend,
in dem die Zustellplattform die Abgabequittung ausstellt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class abgabequittung_zeitpunkt(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Zeitpunkt der Abgabequittung der Zustellplattform"
    reference = "SR 272.1 Art. 8b Abs. 1"


class frist_ablauf_datum(Variable):
    value_type = date
    entity_key = 'person'
    definition_period = YEAR
    label = "Datum des Fristablaufs"
    reference = "SR 272.1 Art. 8b"


class frist_gewahrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Frist durch rechtzeitige elektronische Eingabe gewahrt wurde"
    reference = "SR 272.1 Art. 8b Abs. 1"
