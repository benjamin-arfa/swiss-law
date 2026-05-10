"""SR 0.142.117.149 Art. 14

Generated from: ch/0/de/0.142.117.149.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class notice_period(Variable):
    value_type = int
    label = "Notice period (one month) for abrogation (Art. 3, SR 0.142.117.149)"
    entity = Any
    definition_period = MONTH
    unit = 'month'
    reference = 'https://www.admin.ch/opc/fr/classified-compilation/20021042/index.html#Art_3'

    def formula(person, period, parameters):
        return 1

class actual_entry_into_force_date(Variable):
    value_type = Date
    label = "Date of entry into force (Art. 1, SR 0.142.117.149)" 
    entity = Any
    definition_period = MONTH
    unit = 'date'

    def formula(person, period, parameters):
        return 2002-12-10  # The Swiss Federal Charter's actual entry into force
