"""SR 360.2 Art. 29i

Generated from: ch/360/de/360.2.md

Protokollierung der Abfragen auf Auswertungsplattformen: 1 Jahr Aufbewahrung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_plattform_protokoll_aufbewahrung_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Aufbewahrungsdauer der Protokolle der Auswertungsplattformen in Jahren"
    reference = "SR 360.2 Art. 29i Abs. 2"

    def formula(person, period, parameters):
        return person('nes_plattform_protokoll_aufbewahrung_jahre', period) * 0 + 1
