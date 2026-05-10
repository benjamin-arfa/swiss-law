"""SR 0.142.116.907 Art. 6

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class annual_stagiaires_limit(Variable):
    value_type = int
    entity = None
    definition_period = YEAR
    label = "Annual Stagiaires Limit (Article 6 SR 0.142.116.907)"

    def formula(_variables, period, parameters):
        return 100
