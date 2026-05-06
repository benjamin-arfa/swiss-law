"""SR 195.1 Art. 2

Generated from: ch/195/de/195.1.md

Zweck: Mit diesem Gesetz will der Bund die Rechte und Pflichten einheitlich
regeln, Beziehungen foerdern, Mobilitaet erleichtern, Praesenz foerdern.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 2 defines the purpose of the law.
# Declaratory provision, no computable rule.
