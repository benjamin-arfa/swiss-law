"""SR 0.142.117.632 Art. 7

Generated from: ch/0/de/0.142.117.632.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class citizens_non_discrimination(Variable):
    value_type = bool
    entity = Person, ForeignCitizen
    definition_period = YEAR
    label = "Non-discrimination in taxation for citizens (Art. 7, SR 0.142.117.632)"

    def formula(person, period, parameters):
        is_native_citizen = (person.country_of_residence == "CH")
        is_foreign_citizen = (person.country_of_residence != "CH")

        return is_foreign_citizen & (parameters(period).taxation.rules.apply_to_foreigners == is_native_citizen)
