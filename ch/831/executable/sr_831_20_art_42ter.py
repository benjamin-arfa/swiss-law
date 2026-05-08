"""SR 831.20 Art. 42ter

Generated from: ch/831/de/831.20.md

Art. 42ter: Hoehe der Hilflosenentschaedigung
The monthly helplessness allowance amounts to:
- severe helplessness: 80% of maximum AHV pension
- moderate helplessness: 50% of maximum AHV pension
- mild helplessness: 20% of maximum AHV pension

For minors in a care institution: 25% of the respective amount (Abs. 2).
Intensive care supplement for minors at home (Abs. 3):
- at least 8h/day: 100% of max AHV pension
- at least 6h/day: 70% of max AHV pension
- at least 4h/day: 40% of max AHV pension
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_grad_hilflosigkeit(Variable):
    """0 = keine, 1 = leicht, 2 = mittelschwer, 3 = schwer"""
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Hilflosigkeit (0=keine, 1=leicht, 2=mittelschwer, 3=schwer)"
    reference = "SR 831.20 Art. 42ter Abs. 1"


class iv_ist_minderjaehrig_im_heim(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Minderjaehrige Person lebt in einem Heim"
    reference = "SR 831.20 Art. 42ter Abs. 2"


class iv_intensivpflege_stunden_pro_tag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Stunden Intensivpflege pro Tag (fuer minderjaehrige zu Hause)"
    reference = "SR 831.20 Art. 42ter Abs. 3"


class iv_hoechstbetrag_altersrente(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Hoechstbetrag der monatlichen Altersrente nach Art. 34 Abs. 3 und 5 AHVG"
    reference = "SR 831.20 Art. 42ter Abs. 1"


class iv_hilflosenentschaedigung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Monatliche Hilflosenentschaedigung der IV"
    reference = "SR 831.20 Art. 42ter"

    def formula(person, period, parameters):
        grad = person('iv_grad_hilflosigkeit', period)
        max_rente = person('iv_hoechstbetrag_altersrente', period)
        im_heim = person('iv_ist_minderjaehrig_im_heim', period)

        # Abs. 1: Prozentsatz nach Schweregrad
        anteil = select(
            [grad == 3, grad == 2, grad == 1],
            [0.80, 0.50, 0.20],
            default=0.0,
        )

        entschaedigung = max_rente * anteil

        # Abs. 2: Minderjaehrige im Heim erhalten nur 25%
        entschaedigung = where(im_heim, entschaedigung * 0.25, entschaedigung)

        return entschaedigung


class iv_intensivpflegezuschlag(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = MONTH
    label = "Intensivpflegezuschlag fuer minderjaehrige IV-Versicherte zu Hause"
    reference = "SR 831.20 Art. 42ter Abs. 3"

    def formula(person, period, parameters):
        stunden = person('iv_intensivpflege_stunden_pro_tag', period)
        max_rente = person('iv_hoechstbetrag_altersrente', period)

        zuschlag = select(
            [stunden >= 8, stunden >= 6, stunden >= 4],
            [1.00, 0.70, 0.40],
            default=0.0,
        )

        return max_rente * zuschlag
