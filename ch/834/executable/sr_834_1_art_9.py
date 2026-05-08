"""SR 834.1 Art. 9

Generated from: ch/834/de/834.1.md

Grundentschaedigung waehrend Rekrutenschule und gleichgestellten Dienstzeiten:
- Abs. 1: Taegl. Grundentschaedigung = 25% des Hoechstbetrags der Gesamtentschaedigung.
- Abs. 2: Bei Kinderzulagen-Anspruch wird nach Art. 10 bemessen.
- Abs. 3: Zivildienstleistende ohne RS: gleichgestellt fuer entsprechende Anzahl Tage.
- Abs. 4: Grundausbildung Zivilschutz: 25% des Hoechstbetrags.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import DAY, MONTH


class eo_in_rekrutenschule(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person befindet sich in Rekrutenschule, Rekrutierung oder Durchdiener-Grundausbildung"
    reference = "SR 834.1 Art. 9 Abs. 1"


class eo_in_grundausbildung_zivilschutz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person befindet sich in Grundausbildung im Zivilschutz"
    reference = "SR 834.1 Art. 9 Abs. 4"


class eo_hat_kinderzulagen_anspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person hat Anspruch auf Kinderzulagen nach Art. 6 EOG"
    reference = "SR 834.1 Art. 9 Abs. 2"


class eo_grundentschaedigung_rs(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Taegl. Grundentschaedigung waehrend RS und gleichgestellter Dienstzeit (CHF)"
    reference = "SR 834.1 Art. 9"

    def formula_2005(person, period, parameters):
        import numpy as np

        in_rs = person('eo_in_rekrutenschule', period)
        in_zs = person('eo_in_grundausbildung_zivilschutz', period)
        hat_kinder = person('eo_hat_kinderzulagen_anspruch', period)

        p = parameters(period).sr834_1
        hoechstbetrag = p.hoechstbetrag_gesamtentschaedigung

        # Abs. 1 & 4: 25% des Hoechstbetrags
        grundentschaedigung_rs = hoechstbetrag * p.anteil_grundentschaedigung_rs

        # Abs. 2: mit Kindern -> nach Art. 10 bemessen (hoeher)
        grundentschaedigung_art10 = person('eo_grundentschaedigung_andere_dienste', period)

        in_rs_oder_zs = (in_rs + in_zs) > 0

        return np.where(
            in_rs_oder_zs,
            np.where(hat_kinder, grundentschaedigung_art10, grundentschaedigung_rs),
            0.0
        )
