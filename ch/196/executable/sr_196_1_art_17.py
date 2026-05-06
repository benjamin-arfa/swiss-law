"""SR 196.1 Art. 17

Generated from: ch/196/de/196.1.md

Grundsatz der Rueckerstattung: Ziel ist die Verbesserung der
Lebensbedingungen oder die Staerkung der Rechtsstaatlichkeit.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 17 defines the purpose of restitution.
# Declaratory provision, no computable rule.
