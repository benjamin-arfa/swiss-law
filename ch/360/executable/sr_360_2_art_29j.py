"""SR 360.2 Art. 29j

Generated from: ch/360/de/360.2.md

Aufbewahrungsdauer und Datenloeschung auf Auswertungsplattformen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nes_plattform_daten_in_strafverfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten wurden zu den Akten eines Strafverfahrens genommen"
    reference = "SR 360.2 Art. 29j Abs. 2"


class nes_plattform_daten_in_rechtshilfe(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Daten wurden zu den Akten eines internationalen Rechtshilfeverfahrens genommen"
    reference = "SR 360.2 Art. 29j Abs. 3"


class nes_plattform_rechtshilfe_loeschfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Automatische Loeschfrist nach Rechtskraft der Schlussverfuegung in Jahren"
    reference = "SR 360.2 Art. 29j Abs. 3"

    def formula(person, period, parameters):
        return person('nes_plattform_rechtshilfe_loeschfrist_jahre', period) * 0 + 5
