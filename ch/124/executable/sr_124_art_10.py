"""SR 124 Art. 10 - Polizeilicher Zwang und polizeiliche Massnahmen im Ausland

Generated from: ch/de/124.md
The Federal Council may authorize police coercion abroad outside self-defense
situations if a legal basis exists. Local law applies.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class polizeilicher_zwang_autorisiert_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Bundesrat hat polizeilichen Zwang im Ausland ausserhalb von Notwehr gestattet"
    reference = "SR 124 Art. 10 Abs. 1"
    default_value = False
