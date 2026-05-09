"""SR 143.1 Art. 5 - Antrag auf Ausstellung (Application for Issuance)

Generated from: ch/143/de/143.1.md

Applicants must appear in person at the designated cantonal office or
Swiss representation abroad. Minors and persons under comprehensive
guardianship need written consent of their legal representative.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class ist_minderjaehrig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person minderjaehrig ist"
    reference = "SR 143.1 Art. 5 Abs. 1"


class steht_unter_umfassender_beistandschaft(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person unter umfassender Beistandschaft steht"
    reference = "SR 143.1 Art. 5 Abs. 1"


class benoetigt_einwilligung_gesetzlicher_vertreter(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die schriftliche Einwilligung des gesetzlichen Vertreters benoetigt wird"
    reference = "SR 143.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        minderjaehrig = person('ist_minderjaehrig', period)
        beistandschaft = person('steht_unter_umfassender_beistandschaft', period)
        return minderjaehrig + beistandschaft > 0


class persoenliche_vorsprache_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob persoenliche Vorsprache bei der Behoerde erforderlich ist"
    reference = "SR 143.1 Art. 5 Abs. 1"

    def formula(person, period, parameters):
        # Grundsaetzlich muss jeder persoenlich vorsprechen
        # Ausnahmen kann der Bundesrat vorsehen (Abs. 3)
        return True
