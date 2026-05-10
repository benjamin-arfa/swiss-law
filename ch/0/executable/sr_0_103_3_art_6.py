"""SR 0.103.3 Art. 6

Generated from: ch/0/de/0.103.3.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ahv_disappearance_leaders_responsibility(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Responsibility of disappearance insurance leaders for enforced disappearance (Article 6 of the International Convention)"

    def formula(person, period, parameters):
        leads_disappearance = parameters(period).law.disappearance_leaders.category.lead
        in_charge_of_disappearance = parameters(period).law.disappearance_leaders.category.in_charge
        responsible_for_disappearance = parameters(period).law.disappearance_leaders.category.responsible
        disappearance_leaders_responsible = person("has_disappearance_mandatory_insurance_leaders", period)

        return leads_disappearance | in_charge_of_disappearance | responsible_for_disappearance | disappearance_leaders_responsible
