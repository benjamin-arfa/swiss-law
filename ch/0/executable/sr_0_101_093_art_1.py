"""SR 0.101.093 Art. 1

Generated from: ch/0/de/0.101.093.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from social_base_variables import Variable

class DeathPenaltyVariable(Variable):
    key = 'death_penalty_exists'
    label = 'Death penalty exists'
    entity = Person
    definition_period = 'P1Y'
    reference = 'https://www.admin.ch/opc/en/classified-compilation/20021413/index.html#art_1'

    def formula(var, self, country, period):
        return 0
