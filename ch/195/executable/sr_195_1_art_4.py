"""SR 195.1 Art. 4

Generated from: ch/195/de/195.1.md

Rechtsvorschriften des Empfangsstaates.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 4 is a general principle about respecting host state law.
# Declaratory provision, no computable rule.
