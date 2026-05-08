"""SR 124 Art. 6 - Identifizierbarkeit (Identifiability)

Generated from: ch/de/124.md
The deploying authority ensures personnel are identifiable during operations.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class sicherheitspersonal_identifizierbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal ist bei Ausuebung seiner Funktion identifizierbar"
    reference = "SR 124 Art. 6"
    default_value = False
