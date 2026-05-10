"""SR 120.4 Art. 29

Generated from: ch/120/de/120.4.md

Archivierung: Document retention for max 10 years then offered to Federal Archives.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class psp_unterlagen_aufbewahrungsdauer_max_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Aufbewahrungsdauer der PSP-Unterlagen in Jahren"
    reference = "SR 120.4 Art. 29 Abs. 1"

    def formula(person, period, parameters):
        return 10  # hoechstens 10 Jahre
