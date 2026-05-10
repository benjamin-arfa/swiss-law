"""SR 831.111 Art. 13a

Generated from: ch/831/de/831.111.md

Art. 13a: Beitragspflichtige Personen - Persons liable to pay contributions.

Abs. 1: Liable to pay contributions are:
a. employed insured persons from 1 January after completing age 17
b. non-employed insured persons from 1 January after completing age 20

Abs. 2: Contribution obligation ends at the end of the month in which
the reference age under Art. 21 Abs. 1 AHVG is reached.

Abs. 3: Own contributions are deemed paid if the spouse pays at least
double the minimum contribution of Art. 13b, for:
a. non-employed spouses of employed insured persons
b. insured persons working in spouse's business without cash wages
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class vfv_alter(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Alter der versicherten Person"
    reference = "SR 831.111 Art. 13a"


class vfv_ist_erwerbstaetig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist erwerbstaetig"
    reference = "SR 831.111 Art. 13a Abs. 1"


class vfv_referenzalter_erreicht(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Referenzalter nach Art. 21 Abs. 1 AHVG erreicht"
    reference = "SR 831.111 Art. 13a Abs. 2"


class vfv_beitragspflichtig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist beitragspflichtig in der freiwilligen Versicherung (Art. 13a VFV)"
    reference = "SR 831.111 Art. 13a"

    def formula(person, period, parameters):
        alter = person('vfv_alter', period)
        erwerbstaetig = person('vfv_ist_erwerbstaetig', period)
        referenzalter = person('vfv_referenzalter_erreicht', period.first_month)

        # Employed: from age 18 (1 Jan after completing 17)
        # Non-employed: from age 21 (1 Jan after completing 20)
        alt_genug_erwerbstaetig = erwerbstaetig * (alter >= 18)
        alt_genug_nichterwerbstaetig = not_(erwerbstaetig) * (alter >= 21)

        return (alt_genug_erwerbstaetig + alt_genug_nichterwerbstaetig) * not_(referenzalter)
