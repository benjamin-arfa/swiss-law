"""SR 651.1 Art. 19 - Procedure de recours

Generated from: ch/651/fr/651.1.md

Appeal procedure: decisions preceding the final decision are
immediately enforceable; appeals have suspensive effect.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class decision_finale_rendue(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La decision finale a ete rendue"
    reference = "SR 651.1 Art. 19 al. 1"


class recours_depose(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Un recours a ete depose contre la decision finale"
    reference = "SR 651.1 Art. 19 al. 3"


class effet_suspensif_recours(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le recours a un effet suspensif"
    reference = "SR 651.1 Art. 19 al. 3"

    def formula(self, period, parameters):
        return self('recours_depose', period)
