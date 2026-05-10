"""SR 0.103.2 Art. 23

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class family_income(Variable):
    value_type = float
    entity = Family
    definition_period = MONTH
    label = "Aggregate family income"

    def formula(family, period, parameters):
        adult_income = sum(
            (person("income", period) for person in family.members if person("is_adult", period))
        )
        child_support = sum(
            (parameters(period).family.child_support for person in family.members if person("is Minor", period))
        )
        return adult_income + child_support
