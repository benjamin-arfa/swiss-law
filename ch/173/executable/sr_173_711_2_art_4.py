"""SR 173.711.2 Art. 4

Generated from: ch/173/de/173.711.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class richter_kuendigungsfrist_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Kuendigungsfrist fuer Richter in Monaten (Art. 4 Abs. 1)"
    reference = "SR 173.711.2 Art. 4"

    def formula(person, period, parameters):
        # Art. 4: Kuendigungsfrist betraegt 6 Monate
        return person('alter', period) * 0 + 6
