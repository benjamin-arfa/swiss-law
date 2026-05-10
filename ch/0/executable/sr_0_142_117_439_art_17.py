"""SR 0.142.117.439 Art. 17

Generated from: ch/0/de/0.142.117.439.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_treaty_ratification_date(Variable):
    value_type = date
    entity = Person
    label = "Date of AHV/IV/EO treaty ratification"

    def formula(person, period, parameters):
        # This would probably be a parameter to be filled in
        ratification_year = parameters(period).treaty_ratification_year
        return date(ratification_year, 1, 1)

class ahv_treaty_effective_date(Variable):
    value_type = date
    entity = Person
    label = "Date of AHV/IV/EO treaty effective entry"

    def formula(person, period, parameters):
        # This would probably be a parameter to be filled in
        # based on art. 17 para. 1
        ratification_period = (ahv_treaty_ratification_date(person, period) - period.initial_date).days // 30
        return ahv_treaty_ratification_date(person, period) + relativedelta(months=ratification_period)
