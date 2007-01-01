"""SR 429.1 Art. 7

Generated from: ch/429/de/429.1.md

Skipped: Purely procedural article.
Art. 7 assigns enforcement responsibility to the Federal Council.
No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 7 - Vollzug
# Der Bundesrat wird mit dem Vollzug beauftragt. Keine berechenbare Regel.
