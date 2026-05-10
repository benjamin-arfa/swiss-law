"""SR 0.142.116.909 Art. 15

Generated from: ch/0/de/0.142.116.909.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class onward_transportation_permitted(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Onward transportation permission for foreign national (Art. 15 SR 0.142.116.909)"

    def formula(person, period, parameters):
        return not (
            # risk of persecution
            (person("race", period) == "at_risk")
            | (person("religion", period) == "at_risk")
            | (person("nationality", period) == "at_risk")
            | (person("social_group", period) == "at_risk")
            | (person("political_views", period) == "at_risk")
            
            # risk of prosecution
            | (person("committed_crime", period) & ~person("already_prosecuted", period))
            
            # risk of prosecution in another country
            | person("committed_crime_other_country", period) & ~person("already_prosecuted_other_country", period)
        )
