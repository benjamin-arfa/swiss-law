"""SR 451.1 Art. 28-30

Generated from: ch/451/de/451.1.md

Skipped: Art. 28 - Aufhebung bisherigen Rechts.
Art. 29 - Uebergangsbestimmung.
Art. 30 - Inkrafttreten.
Rein prozedural / Schlussbestimmungen.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Schlussbestimmungen
