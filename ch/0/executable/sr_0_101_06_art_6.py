"""SR 0.101.06 Art. 6

Generated from: ch/0/de/0.101.06.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from pyspedas import Variable

class Art6ConventionReference(Variable):
    value_type = bool
    entity = Person
    definition_period = '1 year'
    label = 'Is the condition as per Art. 6 of the SR 0.101.06 fulfilled?'

    def formula(art6, period, models):
        return 1
