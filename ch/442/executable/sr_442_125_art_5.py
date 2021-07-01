"""SR 442.125 Art. 5

Generated from: ch/442/de/442.125.md

Bemessung spartenspezifischer Finanzhilfen: Massgebend ist die Zahl der Aktiven.
Max 50% der Kosten fuer Dienstleistungen nach Art. 3 Abs. 2.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class kosten_dienstleistungen_laienorganisation(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Kosten fuer die Erbringung der Dienstleistungen (CHF)"
    reference = "SR 442.125 Art. 5 Abs. 2"


class max_spartenspezifische_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale spartenspezifische Finanzhilfe (max 50% der Dienstleistungskosten)"
    reference = "SR 442.125 Art. 5 Abs. 2"

    def formula(person, period, parameters):
        kosten = person('kosten_dienstleistungen_laienorganisation', period)
        return kosten * 0.50
