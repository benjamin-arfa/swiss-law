"""SR 195.1 Art. 1

Generated from: ch/195/de/195.1.md

Gegenstand: Dieses Gesetz regelt Massnahmen fuer Auslandschweizer,
konsularischen Schutz und Dienstleistungen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 1 defines the subject matter.
# Declaratory provision, no computable rule.
