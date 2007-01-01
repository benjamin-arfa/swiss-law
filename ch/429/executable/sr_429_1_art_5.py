"""SR 429.1 Art. 5

Generated from: ch/429/de/429.1.md

Skipped: Purely procedural/organizational article.
Art. 5 governs cooperation with other organizations and treaty competences.
No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 5 - Zusammenarbeit und Beteiligungen
# Ermaechtigt das Bundesamt zur Zusammenarbeit und den Bundesrat zum Abschluss
# internationaler Abkommen. Rein organisatorisch, keine berechenbare Regel.
