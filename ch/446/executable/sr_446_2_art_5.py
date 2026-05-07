"""SR 446.2 Art. 5

Generated from: ch/446/de/446.2.md

Skipped: Begriffsbestimmungen - rein definitorisch, keine berechenbare Regel.
Definiert: Akteurin, Anbieterin, Veranstalterin, Abrufdienst, Plattformdienst, Inhaltsdeskriptor.
"""
from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Skipped: Begriffsbestimmungen - keine berechenbare Regel
