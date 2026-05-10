"""SR 170.32 Art. 11

Generated from: ch/170/de/170.32.md

Haftung des Bundes als Subjekt des Zivilrechts.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bund_handelt_als_zivilrechtssubjekt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund tritt als Subjekt des Zivilrechts auf (Art. 11 Abs. 1 VG)"
    reference = "SR 170.32, Art. 11 Abs. 1"


class bund_haftet_nach_zivilrecht(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund haftet nach zivilrechtlichen Bestimmungen (Art. 11 Abs. 1 VG)"
    reference = "SR 170.32, Art. 11 Abs. 1"

    def formula(person, period, parameters):
        return person('bund_handelt_als_zivilrechtssubjekt', period)
