"""SR 152.1 Art. 23

Generated from: ch/152/de/152.1.md

Strafbestimmung: Busse bei Offenbarung von geschuetztem Archivgut.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class offenbarung_geschuetztes_archivgut(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Informationen aus geschuetztem Archivgut offenbart wurden"
    reference = "SR 152.1 Art. 23"


class strafbar_nach_bga(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Strafbarkeit nach Art. 23 BGA vorliegt (Busse)"
    reference = "SR 152.1 Art. 23"

    def formula(person, period, parameters):
        return person('offenbarung_geschuetztes_archivgut', period)
