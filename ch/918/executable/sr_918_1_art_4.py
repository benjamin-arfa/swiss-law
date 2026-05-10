"""SR 918.1 Art. 4 - Anforderungen an die Ernteversicherung

Generated from: ch/918/de/918.1.md

Versicherer muss FINMA-Bewilligung fuer Zweig B9 haben.
Selbstbehalt von mindestens 15 % der Versicherungssumme.
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

class versicherer_hat_finma_bewilligung_b9(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Versicherer verfuegt ueber eine FINMA-Bewilligung fuer den Zweig B9"
    reference = "SR 918.1 Art. 4 Abs. 1"


class selbstbehalt_anteil(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Selbstbehalt der Ernteversicherung als Anteil der Versicherungssumme (0-1)"
    reference = "SR 918.1 Art. 4 Abs. 2"


# Computed variable

class ernteversicherung_erfuellt_anforderungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Ernteversicherung erfuellt die Anforderungen nach Art. 4"
    reference = "SR 918.1 Art. 4"

    def formula(self, period, parameters):
        finma = self('versicherer_hat_finma_bewilligung_b9', period)
        selbstbehalt = self('selbstbehalt_anteil', period)
        return finma * (selbstbehalt >= 0.15)
