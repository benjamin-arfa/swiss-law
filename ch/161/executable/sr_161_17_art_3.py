"""SR 161.17 Art. 3

Generated from: ch/161/de/161.17.md

Einholen der Stimmrechtsbescheinigung: Schwellen von 50'000 (Referendum)
und 100'000 (Initiative) gueltige Unterschriften.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_referendum(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob es sich um ein Referendum handelt"
    reference = "SR 161.17 Art. 3 Abs. 3 Bst. a"


class anzahl_gueltige_unterschriften(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl gueltige eingereichte Unterschriften"
    reference = "SR 161.17 Art. 3 Abs. 3"


class zustandekommen_ohne_weitere_bescheinigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Zustandekommen ohne weitere Stimmrechtsbescheinigung festgestellt werden kann"
    reference = "SR 161.17 Art. 3 Abs. 3 Bst. a"

    def formula(person, period, parameters):
        referendum = person('ist_referendum', period)
        unterschriften = person('anzahl_gueltige_unterschriften', period)
        # Referendum: 50'000, Initiative: 100'000
        schwelle = referendum * 50000 + (1 - referendum) * 100000
        return unterschriften >= schwelle
