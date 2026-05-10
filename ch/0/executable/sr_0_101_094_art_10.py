"""SR 0.101.094 Art. 10

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class gerichtshof_beschluss_entstehung(Variable):
    value_type = bool
    label = u"Lässt gerichtshof_beschluss zu?"
    entity = Person
    definition_period = MONTH
    reference = "SR 0.101.094 Art. 10"

    def formula(person, period):
        bundesbeitrag = person('bundesbeitrag', period)
        gerichtshof_beschluss = person('gerichtshof_beschluss', period)
        condition_1 = gerichtshof_beschluss > bundesbeitrag
        return condition_1

    parameters = {
        "bundesbeitrag": [0.0, ...],  # to be replaced with actual value
        "gerichtshof_beschluss": [...]  # to be replaced with actual condition
    }
