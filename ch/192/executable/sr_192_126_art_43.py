"""SR 192.126 Art. 43

Generated from: ch/192/de/192.126.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class nettolohn_bar_chf(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Monatlicher Nettolohn in bar in CHF"
    reference = "SR 192.126 Art. 43"

class nettolohn_minimum_chf(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Mindestlohn fuer private Hausangestellte in CHF pro Monat (Art. 43 Abs. 2)"
    reference = "SR 192.126 Art. 43"

    def formula(person, period, parameters):
        # Art. 43 Abs. 2: Mindestens CHF 1'200 netto pro Monat bei Vollzeitbeschaeftigung
        # (Wert gemaess Verordnungstext zum Zeitpunkt der Erfassung)
        return person('arbeitet_vollzeit', period.this_year) * 1200

class nettolohn_genuegend(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Nettolohn erreicht den Mindestlohn (Art. 43)"
    reference = "SR 192.126 Art. 43"

    def formula(person, period, parameters):
        lohn = person('nettolohn_bar_chf', period)
        minimum = person('nettolohn_minimum_chf', period)
        return lohn >= minimum
