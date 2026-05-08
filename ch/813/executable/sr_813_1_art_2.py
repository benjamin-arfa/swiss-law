"""SR 813.1 Art. 2

Generated from: ch/813/de/813.1.md

Geltungsbereich: Anwendbar auf den Umgang mit Stoffen und Zubereitungen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_umgang_mit_stoffen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person mit Stoffen oder Zubereitungen umgeht"
    reference = "SR 813.1 Art. 2 Abs. 1"


class ist_umgang_mit_mikroorganismen_biozid(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person mit Mikroorganismen in Biozidprodukten oder Pflanzenschutzmitteln umgeht"
    reference = "SR 813.1 Art. 2 Abs. 2"


class ist_ausnahme_geltungsbereich_chemg(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob eine Ausnahme vom Geltungsbereich des ChemG vorliegt (z.B. andere Erlasse, Durchfuhr, Gesamtverteidigung)"
    reference = "SR 813.1 Art. 2 Abs. 4"


class chemg_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das Chemikaliengesetz auf die Person anwendbar ist"
    reference = "SR 813.1 Art. 2"

    def formula(person, period, parameters):
        umgang_stoffe = person('ist_umgang_mit_stoffen', period)
        umgang_mikroorg = person('ist_umgang_mit_mikroorganismen_biozid', period)
        ausnahme = person('ist_ausnahme_geltungsbereich_chemg', period)
        return (umgang_stoffe + umgang_mikroorg > 0) * (1 - ausnahme)
