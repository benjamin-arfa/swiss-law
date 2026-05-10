"""SR 944.05 Art. 4-4a

Generated from: ch/944/de/944.05.md

Umfang der Finanzhilfen und Kuerzung: Financial aid up to 50% of eligible
costs. Reduction when equity exceeds 50% of annual expenditure.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class konsorg_anrechenbare_kosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Kosten der Organisation (CHF)"
    reference = "SR 944.05 Art. 3"
    default_value = 0.0


class konsorg_eigenkapital(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Eigenkapital einschliesslich Reserven (CHF)"
    reference = "SR 944.05 Art. 4a Abs. 1"
    default_value = 0.0


class konsorg_jahresaufwand_vorjahr(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jahresaufwand des Vorjahres (CHF)"
    reference = "SR 944.05 Art. 4a Abs. 1"
    default_value = 0.0


class konsorg_ist_konsumentenorg_art1(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Organisation eine Konsumentenorganisation nach Art. 1 Abs. 1 ist (ACSI, FRC, kf, SKS)"
    reference = "SR 944.05 Art. 1 Abs. 1"
    default_value = False


class konsorg_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe an Konsumentenorganisation (CHF)"
    reference = "SR 944.05 Art. 4-4a"

    def formula(person, period, parameters):
        import numpy as np
        kosten = person('konsorg_anrechenbare_kosten', period)
        eigenkapital = person('konsorg_eigenkapital', period)
        jahresaufwand = person('konsorg_jahresaufwand_vorjahr', period)
        ist_art1 = person('konsorg_ist_konsumentenorg_art1', period)

        max_anteil = parameters(period).sr_944_05.finanzhilfe_max_anteil
        finanzhilfe = kosten * max_anteil

        # Art. 4a: Kuerzung wenn Eigenkapital > 50% des Jahresaufwands
        hoechstgrenze = jahresaufwand * max_anteil
        ueberschreitung = np.maximum(eigenkapital - hoechstgrenze, 0)
        kuerzung = np.where(ist_art1, ueberschreitung, 0)

        return np.maximum(finanzhilfe - kuerzung, 0)
