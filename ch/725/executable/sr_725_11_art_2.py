"""SR 725.11 Art. 2

Generated from: ch/725/de/725.11.md

Nationalstrassen erster Klasse: Ausschliesslich fuer Motorfahrzeuge,
nur an besonderen Anschlussstellen zugaenglich, getrennte Fahrbahnen,
keine hoehengleichen Kreuzungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class nur_motorfahrzeuge_zugelassen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse ausschliesslich fuer Motorfahrzeuge bestimmt ist"
    reference = "SR 725.11 Art. 2"


class hat_getrennte_fahrbahnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse fuer beide Richtungen getrennte Fahrbahnen aufweist"
    reference = "SR 725.11 Art. 2"


class keine_hoehengleiche_kreuzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse nicht hoehengleich gekreuzt wird"
    reference = "SR 725.11 Art. 2"


class ist_nationalstrasse_erste_klasse(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Strasse eine Nationalstrasse erster Klasse ist"
    reference = "SR 725.11 Art. 2"

    def formula(person, period, parameters):
        ist_ns = person('ist_nationalstrasse', period)
        nur_motor = person('nur_motorfahrzeuge_zugelassen', period)
        getrennt = person('hat_getrennte_fahrbahnen', period)
        kein_kreuz = person('keine_hoehengleiche_kreuzung', period)

        return ist_ns * nur_motor * getrennt * kein_kreuz
