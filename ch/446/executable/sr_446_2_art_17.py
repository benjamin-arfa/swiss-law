"""SR 446.2 Art. 17

Generated from: ch/446/de/446.2.md

Skipped: Prozedural - Verbindlicherklaerung und Veroeffentlichung durch Bundesrat.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Prozedural - Verbindlicherklaerung, Veroeffentlichung Bundesblatt
