"""SR 934.21 Art. 5b

Generated from: ch/934/de/934.21.md

Art. 5b Nachtraegliche Erhoehung des Deckungskapitals:
1. If the statutorily required coverage capital of the armament enterprises
   increases due to the dossier review at the federal pension fund, the
   Confederation assumes this additional coverage. DDPS provides a guarantee
   with Federal Council authorization.
2. In case of capital increase under para. 1, the Confederation ensures adequate
   equity. Current accounting standards at the time of dossier completion apply.
3. The burden is capitalized in the Confederation's balance sheet and depreciated
   over several years through the income statement.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class bgrb_deckungskapital_erhoeht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob sich das Deckungskapital durch Dossierbereinigung erhoeht hat"
    reference = "SR 934.21 Art. 5b Abs. 1"


class bgrb_deckungskapital_erhoehung_betrag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der Deckungskapital-Erhoehung in CHF"
    reference = "SR 934.21 Art. 5b Abs. 1"


class bgrb_bund_uebernimmt_deckung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund die zusaetzliche Deckung uebernimmt"
    reference = "SR 934.21 Art. 5b Abs. 1"

    def formula(person, period, parameters):
        return person('bgrb_deckungskapital_erhoeht', period)


class bgrb_eigenkapitalausstattung_angemessen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Bund fuer angemessene Eigenkapitalausstattung sorgt"
    reference = "SR 934.21 Art. 5b Abs. 2"

    def formula(person, period, parameters):
        return person('bgrb_deckungskapital_erhoeht', period)
