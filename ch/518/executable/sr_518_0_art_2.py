"""SR 518.0 Art. 2

Generated from: ch/518/de/518.0.md

Inkrafttreten: Dieser Beschluss tritt am 10. September 1952 in Kraft.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 2 contains only the entry-into-force provision (10 September 1952).
# No computable rule.
