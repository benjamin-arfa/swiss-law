"""SR 918.1 Art. 3 - Anforderungen an die Bewirtschafterinnen und Bewirtschafter

Generated from: ch/918/de/918.1.md

Direktzahlungsberechtigung im Vorjahr und versicherte Flaechen
im Territorialgebiet der Schweiz.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# Input variables

class direktzahlungsberechtigt_vorjahr(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Bewirtschafterin/der Bewirtschafter hat im Vorjahr die Direktzahlungsvoraussetzungen erfuellt"
    reference = "SR 918.1 Art. 3"


class versicherte_flaechen_in_schweiz(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die versicherten Flaechen liegen im Territorialgebiet der Schweiz"
    reference = "SR 918.1 Art. 3"


# Computed variable

class anspruch_praemienverbilligung_ernteversicherung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Anspruch auf Praemienverbilligung der Ernteversicherung"
    reference = "SR 918.1 Art. 3"

    def formula(self, period, parameters):
        dz = self('direktzahlungsberechtigt_vorjahr', period)
        flaechen = self('versicherte_flaechen_in_schweiz', period)
        return dz * flaechen
