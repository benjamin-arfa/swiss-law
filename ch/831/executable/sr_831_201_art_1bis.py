"""SR 831.201 Art. 1bis

Generated from: ch/831/de/831.201.md

Beitragssatz: Sliding-scale contribution rates for the disability insurance
(IV) for self-employed persons with low income. The rate depends on annual
earned income brackets ranging from CHF 10,100 to CHF 60,500+.
Non-employed persons pay CHF 70-3,500 per year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class iv_jaehrliches_erwerbseinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Erwerbseinkommen in Franken (fuer IV-Beitrag sinkende Skala)"
    reference = "SR 831.201 Art. 1bis Abs. 1"


class iv_ist_nichterwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person nichterwerbstaetig ist (fuer IV-Beitrag)"
    reference = "SR 831.201 Art. 1bis Abs. 2"


class iv_beitragssatz_sinkende_skala(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Beitragssatz in Prozent des Erwerbseinkommens (sinkende Skala)"
    reference = "SR 831.201 Art. 1bis Abs. 1"

    def formula(person, period, parameters):
        import numpy as np
        einkommen = person('iv_jaehrliches_erwerbseinkommen', period)

        # Sliding scale brackets: (min_income, max_income, rate_percent)
        brackets = [
            (10_100, 17_600, 0.752),
            (17_600, 23_000, 0.769),
            (23_000, 25_500, 0.786),
            (25_500, 28_000, 0.804),
            (28_000, 30_500, 0.821),
            (30_500, 33_000, 0.838),
            (33_000, 35_500, 0.873),
            (35_500, 38_000, 0.907),
            (38_000, 40_500, 0.942),
            (40_500, 43_000, 0.977),
            (43_000, 45_500, 1.011),
            (45_500, 48_000, 1.046),
            (48_000, 50_500, 1.098),
            (50_500, 53_000, 1.149),
            (53_000, 55_500, 1.201),
            (55_500, 58_000, 1.253),
            (58_000, 60_500, 1.305),
        ]

        # Default: full rate of 1.4% for income >= 60,500
        result = np.where(einkommen >= 60_500, 1.4, 0.0)

        for low, high, rate in brackets:
            result = np.where(
                (einkommen >= low) & (einkommen < high),
                rate,
                result
            )

        # Below minimum threshold: no contribution via sliding scale
        result = np.where(einkommen < 10_100, 0.0, result)

        return result


class iv_beitrag_sinkende_skala(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "IV-Beitrag in Franken (sinkende Skala oder Nichterwerbstaetige)"
    reference = "SR 831.201 Art. 1bis"

    def formula(person, period, parameters):
        import numpy as np
        ist_nichterwerbstaetig = person('iv_ist_nichterwerbstaetig', period)
        einkommen = person('iv_jaehrliches_erwerbseinkommen', period)
        satz = person('iv_beitragssatz_sinkende_skala', period)

        beitrag_erwerbstaetig = einkommen * satz / 100.0

        # Non-employed: CHF 70-3500 (capped)
        beitrag_nichterwerbstaetig = np.clip(einkommen * 0.01, 70.0, 3500.0)

        return np.where(
            ist_nichterwerbstaetig,
            beitrag_nichterwerbstaetig,
            beitrag_erwerbstaetig
        )
