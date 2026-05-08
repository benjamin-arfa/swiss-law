"""SR 918.1 Art. 2 - Umfang und Hoehe des Beitrags

Generated from: ch/918/de/918.1.md

Der Beitrag entspricht 30 Prozent der jaehrlichen Versicherungspraemie
fuer Ertragsausfaelle infolge von Trockenheit und Frost.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


# Input variables

class versicherungspraemie_trockenheit_frost(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Jaehrliche Versicherungspraemie fuer Ertragsausfaelle infolge Trockenheit und Frost (CHF)"
    reference = "SR 918.1 Art. 2 Abs. 2"


class bewilligte_kredite_ernteversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Bewilligte Kredite fuer Praemienverbilligung Ernteversicherung (CHF)"
    reference = "SR 918.1 Art. 2 Abs. 1"


class gesamtsumme_beitraege_alle_versicherten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gesamtsumme aller zu zahlenden Beitraege an alle Versicherten (CHF)"
    reference = "SR 918.1 Art. 2 Abs. 3"


# Computed variables

class beitrag_ernteversicherung_ungekuerzt(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Ungekuerzter Beitrag zur Verbilligung der Ernteversicherungspraemie (CHF)"
    reference = "SR 918.1 Art. 2 Abs. 2"

    def formula(self, period, parameters):
        praemie = self('versicherungspraemie_trockenheit_frost', period)
        return praemie * 0.30


class kuerzungsfaktor_ernteversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kuerzungsfaktor bei unzureichenden Mitteln (0.0 - 1.0)"
    reference = "SR 918.1 Art. 2 Abs. 3"
    default_value = 1.0

    def formula(self, period, parameters):
        kredite = self('bewilligte_kredite_ernteversicherung', period)
        gesamtsumme = self('gesamtsumme_beitraege_alle_versicherten', period)
        # Wenn genuegend Mittel, kein Kuerzungsfaktor
        return where(gesamtsumme > 0, min_(kredite / gesamtsumme, 1.0), 1.0)


class beitrag_ernteversicherung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Effektiver Beitrag zur Verbilligung der Ernteversicherungspraemie (CHF)"
    reference = "SR 918.1 Art. 2"

    def formula(self, period, parameters):
        ungekuerzt = self('beitrag_ernteversicherung_ungekuerzt', period)
        faktor = self('kuerzungsfaktor_ernteversicherung', period)
        return ungekuerzt * faktor
