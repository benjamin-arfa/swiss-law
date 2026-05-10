"""SR 744.211 Art. 1

Generated from: ch/744/de/744.211.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_744_211_art_1_applicable(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "SR 744.211 Art. 1 - Aufgehoben (abrogated since 1999-01-01)"
    reference = "SR 744.211 Art. 1"

    def formula(person, period, parameters):
        return False
