"""SR 251 Art. 55

Generated from: ch/de/251.md

Other criminal violations: intentional non-compliance with
information duties, unnotified mergers, or merger-related orders
is punishable by fine up to CHF 20,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vorsaetzliche_auskunftspflicht_verletzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Auskunftspflicht vorsaetzlich verletzt wird"
    reference = "SR 251 Art. 55"


class strafbusse_art55_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Busse nach Art. 55 (CHF)"
    reference = "SR 251 Art. 55"

    def formula(person, period, parameters):
        return person('vorsaetzliche_auskunftspflicht_verletzung', period) * 20000.0
