"""SR 981.1 Art. 6 - Entschaedigungsvorschlag

Generated from: ch/981/de/981.1.md

Stimmt der Anspruchsberechtigte innert 30 Tagen zu, wird der
Entschaedigungsvorschlag rechtskraeftig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class entschaedigungsvorschlag_zugestimmt(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Anspruchsberechtigte hat dem Entschaedigungsvorschlag innert 30 Tagen zugestimmt"
    reference = "SR 981.1 Art. 6"


class entschaedigungsvorschlag_rechtskraeftig(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Der Entschaedigungsvorschlag ist rechtskraeftig"
    reference = "SR 981.1 Art. 6"

    def formula(self, period, parameters):
        return self('entschaedigungsvorschlag_zugestimmt', period)
