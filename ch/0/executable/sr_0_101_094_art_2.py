"""SR 0.101.094 Art. 2

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core import periods
from openfisca_core.variables import Variable
from openfisca_core.parameters import ParameterTypeError
from openfisca_core.periods import ETERNITY

class is_judge(Variable):
    value_type = bool
    default_unit = 'yesno'
    entity = 'person'
    definition_period = ETERNITY
    label = 'Is the person a judge?'

class age(Variable):
    value_type = int
    default_unit = 'year'
    entity = 'person'
    definition_period = ETERNITY
    label = 'Age of the person'

class term_of_office(Variable):
    value_type = int
    default_unit = 'year'
    entity = 'person'
    definition_period = periods.year
    label = 'Term of office of the judge'

class end_of_term_age(Variable):
    value_type = int
    default_unit = 'year'
    entity = 'person'
    definition_period = ETERNITY
    label = 'End of term age of the judge'

is_judge.formula = "is_judge == True"

age.formula = "person('age', period)"

term_of_office.formula = "if(is_judge == True, 9, INF)"

end_of_term_age.formula = "70"
