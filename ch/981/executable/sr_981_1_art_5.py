"""SR 981.1 Art. 5 - Schadensbewertung

Generated from: ch/981/de/981.1.md

Ist die Anspruchsberechtigung festgestellt, wird der Schaden bewertet.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class schaden_bewertbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Schadensbewertung ist aufgrund der Beweismittel moeglich"
    reference = "SR 981.1 Art. 5 Abs. 2"


class schadenshoehe(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bewerteter oder geschaetzter Schaden (CHF)"
    reference = "SR 981.1 Art. 5"
