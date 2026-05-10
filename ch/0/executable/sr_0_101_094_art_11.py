"""SR 0.101.094 Art. 11

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from OpenFisca_core.variables import Variable

class AddedValue(Variable):
    value_type = float
    entity = Person
    def formula(__period, _, __structure): return __period['time'].year * 0 + 12
