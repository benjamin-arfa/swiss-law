"""SR 0.131.13 Art. 9

Generated from: ch/0/de/0.131.13.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class association_liability(Variable):
    value_type = float
    label = "Association liability (Art. 9 of the Federal Act on the Associations)":
    entity = Association
    definition_period = YEAR

    def formula(association, period, parameters):
        max_individual_liability = parameters(period).association.maximum_individual_liability
        return max_individual_liability * association.member_count
