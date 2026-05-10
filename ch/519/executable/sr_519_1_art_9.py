"""SR 519.1 Art. 9

Generated from: ch/519/de/519.1.md

Art. 9 Lohn (Salary):
1. Federal employees retain their contractually agreed salary.
2. For new hires, salary is determined based on the function, education,
   professional/life experience, and labor market conditions.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class pvspa_ist_bundesangestellter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the person is an existing federal employee (Angestellte des Bundes)"
    reference = "SR 519.1 Art. 9 Abs. 1"


class pvspa_lohn_beibehalten(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Whether the person retains their existing contractual salary during deployment"
    reference = "SR 519.1 Art. 9 Abs. 1"

    def formula(person, period, parameters):
        return person('pvspa_ist_bundesangestellter', period)
