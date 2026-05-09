"""SR 831.30 Art. 10

Generated from: ch/831/de/831.30.md

Art. 10: Anerkannte Ausgaben - Recognized expenses for EL calculation.

Abs. 1: For persons living at home:
a. General living expenses per year (2025 amounts):
   1. Single persons: CHF 20,670
   2. Couples: CHF 31,005
   3. Orphans/children age 11+: CHF 10,815
      (first 2 full, next 2 at 2/3, rest at 1/3)
   4. Orphans/children under 11: CHF 7,590
      (first child full, each subsequent reduced by 1/6)
b. Rent (max amounts by region, 2025):
   Region 1 single: CHF 18,900; Region 2: CHF 18,300; Region 3: CHF 16,680
   Additional persons: varying supplements
   Wheelchair-accessible: +CHF 6,900

Abs. 2: For persons in homes/hospitals:
a. Daily rate charged by institution (cantons may cap)
b. Canton-determined amount for personal expenses

Abs. 3: For all persons:
a. Income acquisition costs up to gross employment income
b. Building maintenance costs and mortgage interest up to gross property income
c. Social insurance contributions (excl. health insurance premiums)
d. Mandatory health insurance premium (cantonal/regional average, max actual premium)
e. Maintenance obligations paid
f. Net childcare costs for children under 11
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_lebt_im_heim(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person lebt dauernd oder laenger als 3 Monate in einem Heim oder Spital"
    reference = "SR 831.30 Art. 10 Abs. 2"


class el_region(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mietregion der Wohngemeinde (1, 2 oder 3)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"


class el_anzahl_personen_haushalt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Personen im gleichen Haushalt"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"


class el_rollstuhlgaengige_wohnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Notwendigkeit einer rollstuhlgaengigen Wohnung"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b Ziff. 3"


class el_lebensbedarf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag fuer allgemeinen Lebensbedarf (Art. 10 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        alleinstehend = person('el_ist_alleinstehend', period.first_month)
        ehepaar = person('el_ist_ehepaar', period.first_month)

        bedarf = select(
            [ehepaar, alleinstehend],
            [31005, 20670],
            default=20670,
        )
        return bedarf


class el_mietzins_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstbetrag anerkannter Mietzins (Art. 10 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        region = person('el_region', period)
        rollstuhl = person('el_rollstuhlgaengige_wohnung', period)

        # Base amounts for single person (2025)
        basis = select(
            [region == 1, region == 2, region == 3],
            [18900, 18300, 16680],
            default=16680,
        )

        # Additional for wheelchair-accessible housing
        rollstuhl_zuschlag = where(rollstuhl, 6900, 0)

        return basis + rollstuhl_zuschlag


class el_mietzins_effektiv(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Effektiver Mietzins inkl. Nebenkosten"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"


class el_tagestaxe_heim(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Tagestaxe des Heims oder Spitals (Art. 10 Abs. 2 Bst. a ELG)"
    reference = "SR 831.30 Art. 10 Abs. 2 Bst. a"


class el_persoenliche_auslagen_heim(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag fuer persoenliche Auslagen im Heim (Art. 10 Abs. 2 Bst. b ELG)"
    reference = "SR 831.30 Art. 10 Abs. 2 Bst. b"


class el_sozialversicherungsbeitraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Beitraege an Sozialversicherungen des Bundes ohne KV-Praemien (Art. 10 Abs. 3 Bst. c ELG)"
    reference = "SR 831.30 Art. 10 Abs. 3 Bst. c"


class el_unterhaltsbeitraege_geleistet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geleistete familienrechtliche Unterhaltsbeitraege (Art. 10 Abs. 3 Bst. e ELG)"
    reference = "SR 831.30 Art. 10 Abs. 3 Bst. e"


class el_ausgaben_zuhause(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Ausgaben fuer zu Hause lebende Personen (Art. 10 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        lebensbedarf = person('el_lebensbedarf', period)
        mietzins_max = person('el_mietzins_max', period)
        mietzins_eff = person('el_mietzins_effektiv', period)
        mietzins = min_(mietzins_max, mietzins_eff)
        sv_beitraege = person('el_sozialversicherungsbeitraege', period)
        kv_pauschale = person('el_pauschale_krankenpflege', period)
        unterhalt = person('el_unterhaltsbeitraege_geleistet', period)

        return lebensbedarf + mietzins + sv_beitraege + kv_pauschale + unterhalt


class el_ausgaben_heim(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Ausgaben fuer in Heimen/Spitaelern lebende Personen (Art. 10 Abs. 2 ELG)"
    reference = "SR 831.30 Art. 10 Abs. 2"

    def formula(person, period, parameters):
        tagestaxe = person('el_tagestaxe_heim', period)
        persoenlich = person('el_persoenliche_auslagen_heim', period)
        sv_beitraege = person('el_sozialversicherungsbeitraege', period)
        kv_pauschale = person('el_pauschale_krankenpflege', period)
        unterhalt = person('el_unterhaltsbeitraege_geleistet', period)

        return tagestaxe + persoenlich + sv_beitraege + kv_pauschale + unterhalt
