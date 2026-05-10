"""SR 981.1 Art. 9 - Kosten

Generated from: ch/981/de/981.1.md

Gebuehr fuer Verwaltungskosten: 1-5 % des Entschaedigungsbetrags.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class gebuehr_verwaltungskosten_satz(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehrensatz fuer Verwaltungskosten (0.01 - 0.05)"
    reference = "SR 981.1 Art. 9 Abs. 1"


class gebuehr_verwaltungskosten(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gebuehr fuer Verwaltungskosten der Kommission (CHF)"
    reference = "SR 981.1 Art. 9 Abs. 1"

    def formula(self, period, parameters):
        betrag = self('entschaedigungsbetrag_effektiv', period)
        satz = self('gebuehr_verwaltungskosten_satz', period)
        # Satz muss zwischen 1 % und 5 % liegen
        satz_begrenzt = max_(min_(satz, 0.05), 0.01)
        return betrag * satz_begrenzt


class entschaedigung_nach_abzug_gebuehr(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Entschaedigungsbetrag nach Abzug der Verwaltungskostengebuehr (CHF)"
    reference = "SR 981.1 Art. 9"

    def formula(self, period, parameters):
        betrag = self('entschaedigungsbetrag_effektiv', period)
        gebuehr = self('gebuehr_verwaltungskosten', period)
        return betrag - gebuehr
