"""SR 195.1 Art. 5

Generated from: ch/195/de/195.1.md

Eigenverantwortung.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 5 establishes the principle of personal responsibility.
# Declaratory provision, no computable rule.
