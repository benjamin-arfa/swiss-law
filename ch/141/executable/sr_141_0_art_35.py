"""SR 141.0 Art. 35 - Gebuehren

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class gebuehren_hoechstens_kostendeckend(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Gebuehren duerfen hoechstens kostendeckend sein"
    reference = "SR 141.0 Art. 35 Abs. 2"
    default_value = True

    def formula(self, period, parameters):
        return True
