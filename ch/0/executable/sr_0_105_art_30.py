"""SR 0.105 Art. 30

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_countries import countries



class art30_opt_out(Variable):
    value_type = bool
    entity = countries
    definition_period = YEAR
    label = "Countries exempt from Art. 30, Para. 1 arbitration procedure"

    def formula(countries, period, parameters):
        opt_out_status = countries('art30_opt_out_status', period)

        return opt_out_status
