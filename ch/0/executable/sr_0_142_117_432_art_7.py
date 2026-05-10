"""SR 0.142.117.432 Art. 7

Generated from: ch/0/de/0.142.117.432.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class country_of_residence(Variable):
    value_type = str
    entity = Person
    definition_period = YEAR
    label = "Individual's place of residence (Art. 7 SR 0.142.117.432)"

    def formula(person, period, parameters):
        # Determine if the person is a Liechtenstein citizen with a valid passport or ID card
        countries = parameters(period).country
        
        # check for valid residence possibilities: Liechtenstein or Switzerland
        has_liechtenstein_pass_or_id = person("has_liechtenstein_pass_or_id", period)
        foreign_resident = person("foreign_resident", period)

        # A person is tax resident in one of two countries: 
        # a) residing as a citizen in Liechtenstein or Switzerland 
        # b) with foreign residence in Liechtenstein or Switzerland 
        # c) no special tax residence due to nationality, default foreign residence
        return ["Liechtenstein", "Switzerland"][has_liechtenstein_pass_or_id | ~foreign_resident] if has_liechtenstein_pass_or_id | ~foreign_resident else "Foreign residence"
