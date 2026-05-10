"""SR 836.21 Art. 10b - Income determination for multiple employments

Art. 10b: If a person is employed by multiple employers or is simultaneously
self-employed and employed, the incomes are aggregated to determine total income.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class einkommen_unselbststaendig(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Income from employment (Art. 10b FamZV)"
    default_value = 0


class einkommen_selbststaendig(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Income from self-employment (Art. 10b FamZV)"
    default_value = 0


class gesamteinkommen_famz(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Total income for family allowance determination (Art. 10b FamZV)"

    def formula(person, period, parameters):
        unselbst = person("einkommen_unselbststaendig", period)
        selbst = person("einkommen_selbststaendig", period)
        return unselbst + selbst
