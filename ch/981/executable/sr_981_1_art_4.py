"""SR 981.1 Art. 4 - Anspruchsberechtigung

Generated from: ch/981/de/981.1.md

Die Kommission prueft, ob ein Gesuchsteller die Voraussetzungen in
persoenlicher und sachlicher Hinsicht erfuellt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class voraussetzungen_persoenlich_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Persoenliche Voraussetzungen fuer Entschaedigung erfuellt"
    reference = "SR 981.1 Art. 4"


class voraussetzungen_sachlich_erfuellt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Sachliche Voraussetzungen fuer Entschaedigung erfuellt"
    reference = "SR 981.1 Art. 4"


class anspruchsberechtigung_entschaedigung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Gesuchsteller ist anspruchsberechtigt fuer eine Entschaedigung"
    reference = "SR 981.1 Art. 4"

    def formula(self, period, parameters):
        persoenlich = self('voraussetzungen_persoenlich_erfuellt', period)
        sachlich = self('voraussetzungen_sachlich_erfuellt', period)
        return persoenlich * sachlich
