"""SR 429.1 Art. 2

Generated from: ch/429/de/429.1.md

Skipped: Purely procedural/organizational article.
Art. 2 designates the responsible administrative units and requires them
to consider the needs of different language regions. No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 2 - Zustaendige Verwaltungseinheiten
# Rein organisatorisch: Der Bundesrat bezeichnet die zustaendigen Verwaltungseinheiten.
# Keine berechenbaren Regeln.
