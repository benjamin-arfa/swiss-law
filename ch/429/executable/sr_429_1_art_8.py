"""SR 429.1 Art. 8

Generated from: ch/429/de/429.1.md

Skipped: Transitional/repeal provision.
Art. 8 repeals prior legislation. No computable rule.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Art. 8 - Aufhebung bisherigen Rechts
# Hebt fruehere Erlasse auf. Keine berechenbare Regel.
