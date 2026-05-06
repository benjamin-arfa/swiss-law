"""SR 196.1 Art. 11

Generated from: ch/196/de/196.1.md

Grundsatz: Der Bund kann den Herkunftsstaat in dessen Bemuehungen um
Rueckerstattung gesperrter Vermoegenswerte unterstuetzen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 11 is a declaratory principle about support.
# No computable rule.
