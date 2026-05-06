"""SR 196.1 Art. 23

Generated from: ch/196/de/196.1.md

Datenbearbeitung: Die zustaendigen Behoerden duerfen Personendaten bearbeiten,
soweit fuer den Vollzug erforderlich.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Art. 23 regulates data processing permissions.
# Procedural provision, no computable rule.
