"""SR 0.142.116.822 Art. 10

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class schengen_short_term_stay_maximum_days(Variable):
    value_type = int
    entity = Government
    default_value = 90
    definition_period = '180D'
    label = "Maximum duration of non-EU Schengen short-term stay (Art. 10 SR 0.142.116.822)"

    def formula(government, period, parameters):
        return parameters(period).country.regelamentation.diplomatic_short_stay_maximum_days
