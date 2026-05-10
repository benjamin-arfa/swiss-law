"""SR 0.101.094 Art. 20

Generated from: ch/0/de/0.101.094.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_country_templates import settings


class Article_20_Var(Variable):
    value_type = int
    entity = person
    label = u"Art. 20 Var."
    definition_period = ETERNITY

    def formula(person, period, parameters):
        protocol_entry_year = parameters(period).protocol_entry_year
        case_year = person('reference_year', period)
        return np.where(case_year > protocol_entry_year, 1, 0)
