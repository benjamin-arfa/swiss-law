"""SR 0.103.3 Art. 29

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_model_societies import *



class reporting_obligation(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Obligation to submit an annual report to the UN (Art. 29 SR 0.103.3)"

    def formula(countries, period, parameters):
        num_years = (period.now().year - countries('reporting_start_date', period) + 1)  # Since we're on year X, it's X-1 years since start date
        reporting_deadline_surpassed = countries('reporting_start_date', period) + num_years > period.now().year - 2
        measures_implemented = countries('measures_taken', period)
        received_request = countries('request_from_aus', period)

        return (reporting_deadline_surpassed | measures_implemented | received_request)
