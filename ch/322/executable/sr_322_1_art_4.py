"""SR 322.1 Art. 4

Generated from: ch/322/de/322.1.md

Funktionen: Die Einteilung als Justizoffizier bei der Militaerjustiz ist
Voraussetzung zur Bekleidung bestimmter Funktionen (Oberauditor,
Stellvertreter, Praesident des Militaerkassationsgerichts, etc.).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_justizoffizier(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person als Justizoffizier eingeteilt ist"
    reference = "SR 322.1 Art. 4 Abs. 1"


class funktion_militaerjustiz(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = YEAR
    label = "Funktion in der Militaerjustiz"
    reference = "SR 322.1 Art. 4 Abs. 1"
    # Moegliche Werte: oberauditor, stellvertreter, praesident_kassationsgericht,
    # praesident_appellationsgericht, praesident_militaergericht, auditor,
    # untersuchungsrichter, gerichtsschreiber, keine


class erfuellt_funktionsvoraussetzung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person die Voraussetzung fuer die Funktion in der Militaerjustiz erfuellt"
    reference = "SR 322.1 Art. 4"

    def formula_2018(person, period, parameters):
        """Fassung gemaess BG vom 18. Maerz 2016, in Kraft seit 1. Jan. 2018."""
        ist_jo = person('ist_justizoffizier', period)
        # Die Einteilung als Justizoffizier ist Voraussetzung fuer die Funktionen
        # nach Art. 4 Abs. 1 lit. a-g
        return ist_jo
