"""SR 0.142.116.907 Art. 9

Generated from: ch/0/de/0.142.116.907.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Custom variable for treaty termination rules

from openfisca_country import entities

class bilateral_treaty_termination(Variable):
    value_type = bool
    entity = entities.Country
    definition_period = DAY
    label = "Bilateral Treaty Termination (SR 0.142.116.907 Art. 9)"

    def formula(country, period, parameters):
        end_date = parameters(period).bilateral_treaty.sr_0_142_116_907.end_date
        current_date = period.date
        return (current_date >= end_date) | country('treaty_terminated_by_other_country', period)

# Abstracting the termination rule to account for multiple countries involved in terminating
# For example, France and Germany could both terminate the treaty
class bilateral_treaty_termination_abstraction(Variable):
    value_type = bool
    entity = entities.Country
    definition_period = DAY
    label = "Bilateral Treaty Termination (Abstraction)"

    def formula(country, period, parameters):
        partner_country = country('treaty_partner', period)
        termination_by_me = country('treaty_terminated_by_me', period)
        termination_by_partner = partner_country('treaty_terminated_by_me', period)
        own_partner_country = country['SR_0_142_116_907_end_date']
        partner_country_date = partner_country['SR_142_116_907_end_date']
        return (termination_by_me | termination_by_partner) & ((current_date >= own_partner_country_date) | (current_date >= partner_country_date))
