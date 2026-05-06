"""SR 211.111.1 Art. 1

Generated from: ch/211/de/211.111.1.md

Gegenstand: Dieses Gesetz regelt die Voraussetzungen, unter denen eine
Sterilisation zu Verhuetungszwecken zulaessig ist.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 1 defines the subject matter of the law.
# Declaratory provision, no computable rule.
