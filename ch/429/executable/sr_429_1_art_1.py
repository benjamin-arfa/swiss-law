"""SR 429.1 Art. 1

Generated from: ch/429/de/429.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


# Art. 1 - Bundesaufgaben
# Listet die Aufgaben des Bundes im Bereich Meteorologie und Klimatologie auf.
# Rein deklarativ/enumerativ - modelliert als Flags fuer die einzelnen Aufgabenbereiche.

class bund_erfasst_meteorologische_daten(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund erfasst dauernd und flaechendeckend meteorologische und klimatologische Daten (Art. 1 lit. a MetG)"
    reference = "SR 429.1 Art. 1 lit. a"

    def formula(self, period, parameters):
        # Staendige gesetzliche Pflicht
        return True


class bund_warnt_vor_wettergefahren(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund warnt vor Gefahren des Wetters (Art. 1 lit. c MetG)"
    reference = "SR 429.1 Art. 1 lit. c"

    def formula(self, period, parameters):
        return True


class bund_stellt_fluginformationen_bereit(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund stellt meteorologische Informationen fuer den Flugbetrieb bereit (Art. 1 lit. d MetG)"
    reference = "SR 429.1 Art. 1 lit. d"

    def formula(self, period, parameters):
        return True


class bund_ueberwacht_radioaktivitaet_atmosphaere(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Der Bund stellt die Ueberwachung der Radioaktivitaet in der Atmosphaere sicher (Art. 1 lit. f MetG)"
    reference = "SR 429.1 Art. 1 lit. f"

    def formula(self, period, parameters):
        return True
