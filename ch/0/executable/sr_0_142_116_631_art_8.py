"""SR 0.142.116.631 Art. 8

Generated from: ch/0/de/0.142.116.631.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class dta_reduction(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Double Taxation Agreement (DTA) benefits (Art. 8, SR 0.142.116.631)"

    def formula(person, period, parameters):
        dta_benefits = parameters(period).taxation.dta_reduction
        return dta_benefits
