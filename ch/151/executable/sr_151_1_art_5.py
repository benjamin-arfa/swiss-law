"""SR 151.1 Art. 5

Generated from: ch/151/de/151.1.md

Rechtsansprueche bei Diskriminierung: Entschaedigungsberechnung und
Hoechstgrenzen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class monatslohn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Voraussichtlicher oder tatsaechlicher Monatslohn"
    reference = "SR 151.1 Art. 5 Abs. 2"


class schweizerischer_durchschnittslohn(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Schweizerischer Durchschnittslohn (Basis fuer Entschaedigung bei sexueller Belaestigung)"
    reference = "SR 151.1 Art. 5 Abs. 3"


class diskriminierung_bei_anstellung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Diskriminierung in der Ablehnung einer Anstellung liegt"
    reference = "SR 151.1 Art. 5 Abs. 2"


class diskriminierung_bei_kuendigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Diskriminierung in der Kuendigung liegt"
    reference = "SR 151.1 Art. 5 Abs. 2"


class arbeitgeber_massnahmen_gegen_belaestigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Arbeitgeber beweist, angemessene Massnahmen gegen sexuelle Belaestigung getroffen zu haben"
    reference = "SR 151.1 Art. 5 Abs. 3"


class max_entschaedigung_ablehnung_anstellung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Entschaedigung bei diskriminierender Ablehnung einer Anstellung (3 Monatsloehne)"
    reference = "SR 151.1 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        lohn = person('monatslohn', period)
        return lohn * 3


class max_entschaedigung_kuendigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Entschaedigung bei diskriminierender Kuendigung oder sexueller Belaestigung (6 Monatsloehne)"
    reference = "SR 151.1 Art. 5 Abs. 4"

    def formula(person, period, parameters):
        lohn = person('monatslohn', period)
        return lohn * 6


class entschaedigung_sexuelle_belaestigung_moeglich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine Entschaedigung wegen sexueller Belaestigung moeglich ist"
    reference = "SR 151.1 Art. 5 Abs. 3"

    def formula(person, period, parameters):
        belaestigung = person('sexuelle_belaestigung_am_arbeitsplatz', period)
        massnahmen = person('arbeitgeber_massnahmen_gegen_belaestigung', period)
        return belaestigung * (1 - massnahmen)
