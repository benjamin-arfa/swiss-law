"""SR 836.21 Art. 17 - Income measurement for non-employed persons

Art. 17: For measuring the income of non-employed persons, the taxable income
under the Federal Direct Tax Act (DBG, SR 642.11) is decisive.

Generated from: ch/836/de/836.21.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class steuerbares_einkommen_dbg(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Taxable income under Federal Direct Tax Act (Art. 17 FamZV)"
    default_value = 0


class einkommen_nichterwerbstaetig_famz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Income of non-employed person for family allowance purposes (Art. 17 FamZV)"

    def formula(person, period, parameters):
        return person("steuerbares_einkommen_dbg", period)
