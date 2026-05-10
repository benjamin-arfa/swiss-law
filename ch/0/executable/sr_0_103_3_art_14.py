"""SR 0.103.3 Art. 14

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class governmental_cooperation_for_extradition(Variable):
    value_type = bool
    entity = Government
    definition_period = YEAR
    label = "Gov. cooperation for extradition, disappear-related cases (Article 14 BGG)"

    def formula(government, period, parameters):
        cooperate_if_absent = parameters(period).international_cooperation.cooperate_if_absent
        return government('country_type', period) == 'vertragsstaat' and cooperate_if_absent
