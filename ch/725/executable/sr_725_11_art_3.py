"""SR 725.11 Art. 3

Generated from: ch/725/de/725.11.md

Nationalstrassen zweiter Klasse: Ausschliesslich dem Verkehr der
Motorfahrzeuge offen, nur an besonderen Anschlussstellen zugaenglich,
in der Regel nicht hoehengleich gekreuzt.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_nationalstrasse_zweite_klasse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse eine Nationalstrasse zweiter Klasse ist"
    reference = "SR 725.11 Art. 3"

    def formula(person, period, parameters):
        ist_ns = person('ist_nationalstrasse', period)
        nur_motor = person('nur_motorfahrzeuge_zugelassen', period)
        getrennt = person('hat_getrennte_fahrbahnen', period)

        # Zweite Klasse: Motorfahrzeuge, aber ohne zwingende
        # getrennte Fahrbahnen (Unterschied zu erster Klasse)
        return ist_ns * nur_motor * (1 - getrennt)
