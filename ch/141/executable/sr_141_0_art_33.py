"""SR 141.0 Art. 33 - Aufenthalt

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class hat_aufenthaltsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat eine Aufenthalts- oder Niederlassungsbewilligung"
    reference = "SR 141.0 Art. 33 Abs. 1 lit. a"


class hat_vorlaeufige_aufnahme(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat eine vorlaeufige Aufnahme"
    reference = "SR 141.0 Art. 33 Abs. 1 lit. b"


class hat_legitimationskarte(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat eine Legitimationskarte des EDA oder vergleichbaren Aufenthaltstitel"
    reference = "SR 141.0 Art. 33 Abs. 1 lit. c"


class aufenthaltsdauer_vorlaeufig_monate(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthaltsdauer mit vorlaeufiger Aufnahme in Monaten"
    reference = "SR 141.0 Art. 33 Abs. 1 lit. b"


class abgemeldet_oder_ueber_6_monate_ausland(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person hat sich abgemeldet oder lebt seit mehr als 6 Monaten im Ausland"
    reference = "SR 141.0 Art. 33 Abs. 3"


# Computed variables

class aufenthalt_anrechenbar(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Aufenthalt ist anrechenbar fuer die Einbuergerung"
    reference = "SR 141.0 Art. 33 Abs. 1"

    def formula(self, period, parameters):
        bewilligung = self('hat_aufenthaltsbewilligung', period)
        vorlaeufig = self('hat_vorlaeufige_aufnahme', period)
        legitimation = self('hat_legitimationskarte', period)
        return bewilligung + vorlaeufig + legitimation > 0


class aufenthalt_gilt_als_aufgegeben(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Aufenthalt in der Schweiz gilt als aufgegeben"
    reference = "SR 141.0 Art. 33 Abs. 3"

    def formula(self, period, parameters):
        return self('abgemeldet_oder_ueber_6_monate_ausland', period)
