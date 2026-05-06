"""SR 196.1 Art. 28

Generated from: ch/196/de/196.1.md

Zustaendigkeit: Verfolgende und urteilende Behoerde ist das EFD.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 28 regulates jurisdictional competence.
# Procedural provision, no computable rule.
