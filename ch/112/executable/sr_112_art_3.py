"""SR 112 Art. 3

Generated from: ch/de/112.md

Option for the Confederation to acquire land on the Kleine Schanze
for a new administrative building at CHF 10 per square foot.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bauplatz_preis_pro_quadratfuss(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Preis pro Quadratfuss fuer den Bauplatz (CHF)"
    reference = "SR 112 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return 10.0


class bauplatz_tiefe_fuss(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tiefe des Bauplatzes in Fuss"
    reference = "SR 112 Art. 3 Abs. 1"

    def formula(person, period, parameters):
        return 120.0


class trottoir_pflicht_eidgenossenschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Eidgenossenschaft zur Erstellung der Trottoirs verpflichtet ist"
    reference = "SR 112 Art. 3 Abs. 2"
