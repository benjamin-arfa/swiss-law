"""SR 0.142.116.822 Art. 9

Generated from: ch/0/de/0.142.116.822.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class sr_exemption_for_serbian_citizens(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "Exemption for Serbian citizens under Article 9 of SR 0.142.116.822"

    def formula(person, period, parameters):
        return person("citizenship", period) == 'Serbien'
