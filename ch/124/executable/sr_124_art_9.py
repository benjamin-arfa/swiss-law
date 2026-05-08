"""SR 124 Art. 9 - Polizeilicher Zwang und polizeiliche Massnahmen in der Schweiz

Generated from: ch/de/124.md
The contract may authorize police coercion per ZAG (SR 364) if a legal basis exists.
Personnel must have appropriate training. ZAG provisions apply.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class polizeilicher_zwang_autorisiert_inland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sicherheitspersonal darf polizeilichen Zwang in der Schweiz anwenden (vertraglich und gesetzlich)"
    reference = "SR 124 Art. 9 Abs. 1"
    default_value = False
