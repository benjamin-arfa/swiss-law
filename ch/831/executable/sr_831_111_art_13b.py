"""SR 831.111 Art. 13b

Generated from: ch/831/de/831.111.md

Art. 13b: Beitragssatz fuer die AHV/IV - Contribution rate for AHV/IV.

Abs. 1: Contributions of employed insured persons amount to 10.1% of
the relevant income. Minimum contribution: CHF 1,010 per year.

Abs. 2: Non-employed insured persons pay contributions based on their
wealth and pension income, between CHF 1,010 and CHF 25,250 per year.
Scale (2025):
- up to CHF 600,000: CHF 1,010
- from CHF 600,000: CHF 1,111 + CHF 101 per additional CHF 50,000
- from CHF 1,750,000: CHF 3,434 + CHF 151.50 per additional CHF 50,000
- from CHF 8,950,000: CHF 25,250 (maximum)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vfv_massgebendes_einkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Massgebendes Erwerbseinkommen fuer Beitragsberechnung"
    reference = "SR 831.111 Art. 13b Abs. 1"


class vfv_vermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegen der nichterwerbstaetigen Person"
    reference = "SR 831.111 Art. 13b Abs. 2"


class vfv_renteneinkommen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliches Renteneinkommen der nichterwerbstaetigen Person"
    reference = "SR 831.111 Art. 13b Abs. 2"


class vfv_beitrag_erwerbstaetig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "AHV/IV-Beitrag fuer erwerbstaetige freiwillig Versicherte (Art. 13b Abs. 1 VFV)"
    reference = "SR 831.111 Art. 13b Abs. 1"

    def formula(person, period, parameters):
        einkommen = person('vfv_massgebendes_einkommen', period)
        beitrag = einkommen * 0.101
        mindestbeitrag = 1010
        return max_(beitrag, mindestbeitrag)


class vfv_beitrag_nichterwerbstaetig(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "AHV/IV-Beitrag fuer nichterwerbstaetige freiwillig Versicherte (Art. 13b Abs. 2 VFV)"
    reference = "SR 831.111 Art. 13b Abs. 2"

    def formula(person, period, parameters):
        vermoegen = person('vfv_vermoegen', period)
        renteneinkommen = person('vfv_renteneinkommen', period)

        # Basis: wealth + 20x annual pension income
        bemessungsgrundlage = vermoegen + renteneinkommen * 20

        # Tiered scale (2025 values)
        # Up to 600,000: CHF 1,010
        beitrag = where(bemessungsgrundlage <= 600000, 1010, 0)

        # 600,000 - 1,750,000: 1,111 + 101 per 50,000 above 600,000
        stufe2 = (bemessungsgrundlage > 600000) * (bemessungsgrundlage <= 1750000)
        zusatz_stufe2 = max_(bemessungsgrundlage - 600000, 0) / 50000
        beitrag = beitrag + stufe2 * (1111 + zusatz_stufe2 * 101)

        # 1,750,000 - 8,950,000: 3,434 + 151.50 per 50,000 above 1,750,000
        stufe3 = (bemessungsgrundlage > 1750000) * (bemessungsgrundlage <= 8950000)
        zusatz_stufe3 = max_(bemessungsgrundlage - 1750000, 0) / 50000
        beitrag = beitrag + stufe3 * (3434 + zusatz_stufe3 * 151.50)

        # Above 8,950,000: maximum CHF 25,250
        beitrag = beitrag + (bemessungsgrundlage > 8950000) * 25250

        return beitrag


class vfv_beitrag_ahv_iv(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrlicher AHV/IV-Beitrag in der freiwilligen Versicherung (Art. 13b VFV)"
    reference = "SR 831.111 Art. 13b"

    def formula(person, period, parameters):
        erwerbstaetig = person('vfv_ist_erwerbstaetig', period)
        beitrag_erw = person('vfv_beitrag_erwerbstaetig', period)
        beitrag_nerw = person('vfv_beitrag_nichterwerbstaetig', period)
        return where(erwerbstaetig, beitrag_erw, beitrag_nerw)
