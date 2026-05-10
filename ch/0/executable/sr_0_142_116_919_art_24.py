"""SR 0.142.116.919 Art. 24

Generated from: ch/0/de/0.142.116.919.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

from openfisca_entities import Entity
from openfisca_entity_combinations import AllPeople


class suspend_convention(Assertion):
    value_type = bool
    entity = Entity("country")
    definition_period = MONTH
    label = "Suspension of the convention applied by the country (Art. 24 of the Annex to the Convention)"

    def formula(suspended_entity, period, parameters):
        suspended_entity_name = suspended_entity.entity_string()
        other_entity = Entity(suspended_entity_name, other=True)
        notification = parameters(period).suspension[suspended_entity_name].notification
        suspension_effective = next_month(period.first_date)
        return notification.has_been_sent[other_entity, suspended_entity, period] & notification.effectiveness[suspended_entity_name, period] & period.date >= suspension_effective


class AHV_Suspended(Entity):
    value_type = bool
    def __init__(self, **other_parameters):
        super(AHV_Suspended, self).__init__(*other_parameters)
        self.entity_string = self.entity_string.replace("Country", "Switzerland")

    suspend_variable = suspend_convention(entity = Person, period="Monthly", parameters="Parameters",
                                          label="Suspension of the convention applied by the Country")

    entity_combinations = AllPeople(suspended_variable=suspend_variable, entity_combinations=[])


class suspension(Variable):
    value_type = bool
    entity = AllPeople
    definition_period = MONTH
    label = "Suspension of the AHV Convention due to the conditions in paragraph 1 (Art. 24 SR 0.142.116.919)"

    def formula(all_people, period, parameters):
        suspend_variable = AHV_Suspended(entity=all_people.entity, period=period, parameters=parameters)
        suspend_status = suspend_variable.suspend_variable(all_people, period, parameters)
        return all_people(suspended_variable.suspend_variable) == suspend_status
