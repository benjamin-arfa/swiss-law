"""SR 981 Art. 12

Generated from: ch/de/981.md

Amendment and repeal of existing law: repeal of the 1950 federal
decree on nationalization compensation commissions and Articles 7-8
of the 1957 federal decree on wartime aid.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bundesbeschluss_1950_aufgehoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bundesbeschluss vom 21. Dez. 1950 ueber die Kommission fuer Nationalisierungsentschaedigungen aufgehoben ist"
    reference = "SR 981 Art. 12 Abs. 2 Bst. a"

    def formula(person, period, parameters):
        return True


class bundesbeschluss_1957_art7_8_aufgehoben(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Art. 7 und 8 des Bundesbeschlusses vom 13. Juni 1957 ueber Hilfe an kriegsgeschaedigte Auslandschweizer aufgehoben sind"
    reference = "SR 981 Art. 12 Abs. 2 Bst. b"

    def formula(person, period, parameters):
        return True
