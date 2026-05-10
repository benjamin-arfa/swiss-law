"""SR 514.544.1 Art. 6

Generated from: ch/514/de/514.544.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pruefungsunterlagen_aufbewahrungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufbewahrungsdauer fuer Pruefungsunterlagen und -resultate in Jahren (Art. 6 SR 514.544.1)"
    reference = "SR 514.544.1 Art. 6"

    def formula(person, period, parameters):
        # Zehn Jahre aufzubewahren
        return 10
