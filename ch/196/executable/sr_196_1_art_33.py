"""SR 196.1 Art. 33

Generated from: ch/196/de/196.1.md

Referendum und Inkrafttreten: 1. Juli 2016.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 33 regulates referendum and entry into force.
# Procedural provision, no computable rule.
