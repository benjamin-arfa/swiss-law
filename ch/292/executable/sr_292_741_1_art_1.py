"""SR 292.741.1 Art. 1

Generated from: ch/292/de/292.741.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class frist_arresturkunde_zustellung_tage(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Frist in Tagen für Zustellung der Arresturkunde an das EDA durch das Betreibungsamt"
    reference = "SR 292.741.1 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        return 3
