"""SR 0.132.454.22 Art. 3

Generated from: ch/0/de/0.132.454.22.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class is_bound_costs_person(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Liability for canal construction or border maintenance costs (Art. 3 SR 0.132.454.22)"

    def formula(person, period, parameters):
        is_commission_liable = parameters(period).commissions_is_liable
        is_commission_person = person("is_commissioner", period)
        return is_commission_liability & is_commission_person
class is_bound_costs_person2(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Liability for canal construction or border maintenance costs (Art. 3 SR 0.132.454.22)"

    def formula(person, period, parameters):
        is_commission_liable = parameters(period).commissions_is_liable
        is_commission_person = person("is_commissioner", period)
        return is_commission_person
