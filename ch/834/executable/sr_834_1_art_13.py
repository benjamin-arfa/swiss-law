"""SR 834.1 Art. 13

Generated from: ch/834/de/834.1.md

Kinderzulage: 8 Prozent des Hoechstbetrages der Gesamtentschaedigung pro Kind.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH


class eo_kinderzulage_taeglich(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegl. Kinderzulage (CHF)"
    reference = "SR 834.1 Art. 13"

    def formula_2005(person, period, parameters):
        anzahl_kinder = person('eo_anzahl_kinder', period)
        p = parameters(period).sr834_1
        hoechstbetrag = p.hoechstbetrag_gesamtentschaedigung
        satz = p.kinderzulage_anteil  # 0.08

        return anzahl_kinder * hoechstbetrag * satz
