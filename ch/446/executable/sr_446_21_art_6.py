"""SR 446.21 Art. 6

Generated from: ch/446/de/446.21.md

Skipped: Prozedural - Regelmaessige Ueberpruefung der Jugendschutzregelungen durch BSV.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Prozedural - Ueberpruefung, Mitteilung, Anpassungsfrist
