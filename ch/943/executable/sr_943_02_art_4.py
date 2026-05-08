"""SR 943.02 Art. 4

Generated from: ch/943/de/943.02.md

Anerkennung von Fähigkeitsausweisen:
- Kantonale Fähigkeitsausweise gelten gesamtschweizerisch
- Bei nur teilweiser Erfüllung: Nachweis anderweitig erworbener Kenntnisse möglich
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class hat_kantonalen_faehigkeitsausweis(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person einen kantonalen oder kantonal anerkannten Fähigkeitsausweis besitzt"
    reference = "SR 943.02 Art. 4 Abs. 1"


class faehigkeitsausweis_erfuellt_teilweise(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Fähigkeitsausweis die Anforderungen des Bestimmungsortes nur teilweise erfüllt"
    reference = "SR 943.02 Art. 4 Abs. 3"


class hat_anderweitige_kenntnisse_nachgewiesen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob fehlende Kenntnisse durch Ausbildung oder praktische Tätigkeit nachgewiesen wurden"
    reference = "SR 943.02 Art. 4 Abs. 3"


class faehigkeitsausweis_anerkannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob der Fähigkeitsausweis gesamtschweizerisch anerkannt ist"
    reference = "SR 943.02 Art. 4"

    def formula(person, period, parameters):
        import numpy as np
        hat_ausweis = person('hat_kantonalen_faehigkeitsausweis', period)
        teilweise = person('faehigkeitsausweis_erfuellt_teilweise', period)
        anderweitig = person('hat_anderweitige_kenntnisse_nachgewiesen', period)

        # Full recognition if not partial, or partial + supplementary proof
        voll_erfuellt = hat_ausweis * (1 - teilweise)
        teil_ergaenzt = hat_ausweis * teilweise * anderweitig

        return np.maximum(voll_erfuellt, teil_ergaenzt)
