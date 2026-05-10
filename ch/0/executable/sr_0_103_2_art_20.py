"""SR 0.103.2 Art. 20

Generated from: ch/0/de/0.103.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class war_propaganda_ban(Variable):
    value_type = bool
    entity = Person
    label = "Ban on war propaganda (Art. 20 SR 0.103.2)"

    def formula(person, period, parameters):
        return False  # This ban is not applicable in OpenFisca


class hate_speech_ban(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Ban on hate speech (Art. 20 SR 0.103.2)"

    def formula(person, period, parameters):
        return False  # This ban is not applicable in OpenFisca
