"""SR 0.142.116.659 Art. 23

Generated from: ch/0/de/0.142.116.659.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class agreement_effective_date(Variable):
    value_type = date
    entity = Country
    reference_values = "2009-09-21"
    definition_period = DAY
    label = "Date of entry into force of the agreement (Art. 23)"

    def formula(country, period, parameters):
        return country("last_date_of_notification", period)




class phase_in_start_date(Variable):
    value_type = date
    entity = Country
    reference_values = "2009-09-21"
    definition_period = DAY
    label = "Date of start of phase-in period (Art. 23 para. 2)"

    def formula(country, period, parameters):
        agreement_effective_date = country("agreement_effective_date", period)
        period_elapsed = (period.end_date - agreement_effective_date).days
        return agreement_effective_date + timedelta(days=period_elapsed)
