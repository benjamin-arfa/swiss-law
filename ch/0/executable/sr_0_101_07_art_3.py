"""SR 0.101.07 Art. 3

Generated from: ch/0/de/0.101.07.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_templates import Variable


class compensation_owed(Variable):
    value_type = bool
    _set_input = 'permanent',
    label = 'Compensation Owed'
    entity = Person
    definition_period = YEAR
    reference = 'https://www.admin.ch/opc/en/classified-compilation/20060632/index.html#art_3'

    def formula_2006_12_01(people, period, parameters):
        return compensation_owed.formula(people, period, parameters)

    def formula_2012_01_01(people, period, parameters):
        # Update formula to reflect changes in the law
        return compensation_owed.formula(people, period, parameters)
