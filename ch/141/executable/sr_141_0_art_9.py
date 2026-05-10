"""SR 141.0 Art. 9 - Formelle Voraussetzungen (ordentliche Einbuergerung)

Generated from: ch/141/de/141.0.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# Input variables

class besitzt_niederlassungsbewilligung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Person besitzt eine Niederlassungsbewilligung bei der Gesuchstellung"
    reference = "SR 141.0 Art. 9 Abs. 1 lit. a"


class aufenthaltsdauer_schweiz_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesamte Aufenthaltsdauer in der Schweiz in Jahren"
    reference = "SR 141.0 Art. 9 Abs. 1 lit. b"


class aufenthalt_letzte_5_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthaltsdauer in den letzten fuenf Jahren vor Gesuchstellung in Jahren"
    reference = "SR 141.0 Art. 9 Abs. 1 lit. b"


class aufenthalt_zwischen_8_und_18(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Aufenthaltsjahre in der Schweiz zwischen dem 8. und 18. Lebensjahr"
    reference = "SR 141.0 Art. 9 Abs. 2"


class tatsaechlicher_aufenthalt_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Tatsaechlicher Aufenthalt in der Schweiz in Jahren"
    reference = "SR 141.0 Art. 9 Abs. 2"


# Computed variables

class anrechenbare_aufenthaltsdauer(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Aufenthaltsdauer (mit Doppelzaehlung fuer 8-18-Jaehrige)"
    reference = "SR 141.0 Art. 9 Abs. 2"

    def formula(self, period, parameters):
        normal = self('aufenthaltsdauer_schweiz_jahre', period)
        jugend = self('aufenthalt_zwischen_8_und_18', period)
        # Zeit zwischen 8 und 18 wird doppelt gerechnet (einmal normal + einmal extra)
        return normal + jugend


class formelle_voraussetzungen_ordentliche_einbuergerung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die formellen Voraussetzungen fuer die ordentliche Einbuergerung sind erfuellt"
    reference = "SR 141.0 Art. 9"

    def formula(self, period, parameters):
        niederlassung = self('besitzt_niederlassungsbewilligung', period)
        anrechenbar = self('anrechenbare_aufenthaltsdauer', period)
        letzte_5 = self('aufenthalt_letzte_5_jahre', period)
        tatsaechlich = self('tatsaechlicher_aufenthalt_jahre', period)

        # Abs. 1 lit. b: insgesamt 10 Jahre, davon 3 in letzten 5 Jahren
        aufenthalt_genuegend = (anrechenbar >= 10) * (letzte_5 >= 3)

        # Abs. 2: tatsaechlicher Aufenthalt mindestens 6 Jahre
        tatsaechlich_genuegend = tatsaechlich >= 6

        return niederlassung * aufenthalt_genuegend * tatsaechlich_genuegend
