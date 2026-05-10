"""SR 0.101.094 Art. 9

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_module import Variable

class decision_admissibility_Separately(Variable):
    value_type = bool
    title = "Decision On Admissibility Is Made Separately"
    label = "Separate Admissibility Decision"
    entity = Person
    definition_period = YEAR
    display = False

    # We'll apply the rule here - a decision admissibility is made separately if 
    # benefit_applies_articles_27_28 is True.
    def formula(person, period, parameters):
        return not person('benefit_applies_articles_27_28', period)
