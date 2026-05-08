"""SR 918.1 Art. 9 - Auszahlung der Beitraege an den Versicherer

Generated from: ch/918/de/918.1.md

Akontozahlung bis 31. August (max. 75 %); Restbetrag bis 30. November.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class beitrag_total_an_versicherer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtbeitrag an den Versicherer im Beitragsjahr (CHF)"
    reference = "SR 918.1 Art. 9"


class akontozahlung_ernteversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Akontozahlung an Versicherer bis 31. August (max. 75 % des Beitrags, CHF)"
    reference = "SR 918.1 Art. 9 Bst. a"

    def formula(self, period, parameters):
        total = self('beitrag_total_an_versicherer', period)
        return total * 0.75


class restbetrag_ernteversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Restbetrag an Versicherer bis 30. November (CHF)"
    reference = "SR 918.1 Art. 9 Bst. b"

    def formula(self, period, parameters):
        total = self('beitrag_total_an_versicherer', period)
        akonto = self('akontozahlung_ernteversicherung', period)
        return total - akonto
