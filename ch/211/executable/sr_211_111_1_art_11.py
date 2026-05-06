"""SR 211.111.1 Art. 11

Generated from: ch/211/de/211.111.1.md

Referendum und Inkrafttreten: 1. Juli 2005.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 11 regulates referendum and entry into force.
# Procedural provision, no computable rule.
