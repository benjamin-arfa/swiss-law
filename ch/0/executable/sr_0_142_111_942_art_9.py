"""SR 0.142.111.942 Art. 9

Generated from: ch/0/de/0.142.111.942.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class prior_international_obligation(Variable):
    value_type = bool
    entity = Person
    label = "Prior international obligations (Art. 9 AHVG)"

    def formula(person, period, parameters):
        return False  # Art. 9 does not specify a calculation; it only references international obligations
