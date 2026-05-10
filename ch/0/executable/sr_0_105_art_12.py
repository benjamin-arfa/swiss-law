"""SR 0.105 Art. 12

Generated from: ch/0/de/0.105.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class torture_investigation(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Torture investigation by competent authorities (SR 0.105 Art. 12)"

    def formula(person, period, parameters):
        investigation_launched = person("investigation_launched_by_authority", period)
        authority = parameters(period).social_security.investigation_authority
        return investigation_launched[authority]
