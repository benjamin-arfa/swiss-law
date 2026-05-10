"""SR 0.191.2 Art. 50

Generated from: ch/0/de/0.191.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class treaty_signature_deadline(Variable):
    value_type = bool
    entity = Country
    definition_period = YEAR
    label = "Signature deadline for international treaty (Art. 50 SR 0.191.2)"

    def formula(country, period, parameters):
        treaty_deadline = 1970
        return country("year", period) == treaty_deadline
