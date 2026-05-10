"""SR 0.105.1 Art. 6

Generated from: ch/0/de/0.105.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class contract_state_nominations(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Number of nominations by contract state (Art. 6 SR 0.105.1)"

    def formula(person, period, parameters):
        is_contract_state_citizen = person("is_contract_state_citizen", period)
        is_nominee_state_citizen = person("is_nominee_state_citizen", period)
        candidate1_is_contract_state_citizen = person("candidate1_is_contract_state_citizen", period)
        candidate2_is_contract_state_citizen = person("candidate2_is_contract_state_citizen", period)

        is_multiple_contract_state_nominations = (candidate1_is_contract_state_citizen & is_contract_state_citizen) | (candidate2_is_contract_state_citizen & is_contract_state_citizen)

        return 2 - is_multiple_contract_state_nominations

class is_contract_state_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is candidate a contract state citizen (Art. 6 SR 0.105.1)"

    def formula(person, period, parameters):
        contract_state_citizens = ['CH']  # Replace with actual contract state citizens
        birth_country = person("birth_country", period)
        return birth_country in contract_state_citizens

class is_nominee_state_citizen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Is candidate a nominee state citizen (Art. 6 SR 0.105.1)"

    def formula(person, period, parameters):
        return (person("birth_country", period) == 'CH') | (person("has_nominee_state_citizenship", period))

class has_nominee_state_citizenship(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Has nominee state citizenship (Art. 6 SR 0.105.1)"

    def formula(person, period, parameters):
        countries = ['Country1', 'Country2']  # Replace with actual countries with which a nominee state has a special relationship
        citizenship_holder = person("has_citizenship_of", period)
        return any(country in countries for country in citizenship_holder)
