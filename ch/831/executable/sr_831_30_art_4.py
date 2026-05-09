"""SR 831.30 Art. 4

Generated from: ch/831/de/831.30.md

Art. 4: Allgemeine Voraussetzungen - General eligibility conditions for
supplementary benefits. Persons domiciled in Switzerland with habitual
residence have a right to EL if they:
a. receive an AHV old-age pension
abis. are entitled to a widow/widower pension (before reference age)
ater. receive a widow/widower pension instead of old-age pension (Art. 24b AHVG)
aquater. are entitled to an AHV orphan pension
b. would be entitled to an AHV pension if meeting minimum contribution period
c. are entitled to an IV pension/helplessness allowance or receive IV daily
   allowance for at least 6 continuous months
d. would be entitled to an IV pension if meeting minimum contribution period

Abs. 2: Separated/divorced spouses receiving AHV/IV supplementary pension
Abs. 3: Habitual residence interrupted if >3 months abroad continuously
         or >3 months abroad in a calendar year
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wohnsitz und gewoehnlicher Aufenthalt in der Schweiz (Art. 4 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 4 Abs. 1"


class el_bezug_ahv_altersrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Bezug einer AHV-Altersrente (Art. 4 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 4 Abs. 1 Bst. a"


class el_anspruch_ahv_hinterlassenenrente(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf AHV-Hinterlassenenrente vor Referenzalter (Art. 4 Abs. 1 Bst. abis ELG)"
    reference = "SR 831.30 Art. 4 Abs. 1 Bst. abis"


class el_bezug_iv_rente_oder_hilflosenentschaedigung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Anspruch auf IV-Rente oder Hilflosenentschaedigung oder IV-Taggeld >= 6 Monate (Art. 4 Abs. 1 Bst. c ELG)"
    reference = "SR 831.30 Art. 4 Abs. 1 Bst. c"


class el_auslandaufenthalt_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Tage Auslandaufenthalt im Kalenderjahr"
    reference = "SR 831.30 Art. 4 Abs. 3"


class el_aufenthalt_unterbrochen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Gewoehnlicher Aufenthalt in der Schweiz ist unterbrochen (Art. 4 Abs. 3 ELG)"
    reference = "SR 831.30 Art. 4 Abs. 3"

    def formula(person, period, parameters):
        ausland_tage = person('el_auslandaufenthalt_tage', period.this_year)
        # Interrupted if >3 months (approx. 90 days) abroad in calendar year
        return ausland_tage > 90


class el_grundanspruch(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Grundanspruch auf Ergaenzungsleistungen (Art. 4 ELG)"
    reference = "SR 831.30 Art. 4"

    def formula(person, period, parameters):
        wohnsitz = person('el_wohnsitz_schweiz', period)
        aufenthalt_ok = not_(person('el_aufenthalt_unterbrochen', period))
        ahv_rente = person('el_bezug_ahv_altersrente', period)
        hinterlassene = person('el_anspruch_ahv_hinterlassenenrente', period)
        iv = person('el_bezug_iv_rente_oder_hilflosenentschaedigung', period)

        leistungsbezug = ahv_rente + hinterlassene + iv > 0
        return wohnsitz * aufenthalt_ok * leistungsbezug
