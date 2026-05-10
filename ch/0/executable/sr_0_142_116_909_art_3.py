"""SR 0.142.116.909 Art. 3

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca.switzerland.taxbenefitsperiod import Period


class repatriation_transportation_costs(Variable):
    value_type = with_tax_benefit_parameters = money
    entity = Person
    definition_period = PerMonth
    label = "Transport costs for the repatriation of the person's home country (Art. 3 of SR 0.142.116.909)"

    def formula(person, period, parameters):
        transports_required = person("resident_abroad", period) == True
        transportation_rate = parameters(period).international_repatriation.transp_rate
        # If the person is in the country in question then no transport costs occur

        if person("swiss_resident", period) == True:
            transports_required = False
        if person("expat", period) == False:
            transports_required = False
        return (transports_required * transportation_rate).ceil()
