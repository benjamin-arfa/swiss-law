"""SR 831.20 Art. 29

Generated from: ch/831/de/831.20.md

Art. 29: Beginn des Anspruchs und Auszahlung der Rente
- Abs. 1: Pension entitlement arises at earliest 6 months after claiming,
  but not before the month following the 18th birthday.
- Abs. 2: No entitlement while daily allowance (Art. 22) can be claimed.
- Abs. 3: Pension paid from beginning of month when entitlement arises.
- Abs. 4: Pensions for IV < 50% only paid to insured persons residing in
  Switzerland.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_leistungsanspruch_geltendgemacht_seit_monaten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl Monate seit Geltendmachung des IV-Leistungsanspruchs"
    reference = "SR 831.20 Art. 29 Abs. 1"


class iv_alter_vollendete_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Vollendetes Alter der versicherten Person in Jahren"
    reference = "SR 831.20 Art. 29 Abs. 1"


class iv_bezieht_taggeld(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Versicherte Person bezieht Taggeld nach Art. 22 IVG"
    reference = "SR 831.20 Art. 29 Abs. 2"


class iv_wohnsitz_schweiz(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Wohnsitz und gewoehnlicher Aufenthalt in der Schweiz"
    reference = "SR 831.20 Art. 29 Abs. 4"


class iv_rentenanspruch_begonnen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "IV-Rentenanspruch ist entstanden (Art. 29 IVG)"
    reference = "SR 831.20 Art. 29"

    def formula(person, period, parameters):
        monate_seit_anspruch = person('iv_leistungsanspruch_geltendgemacht_seit_monaten', period)
        alter = person('iv_alter_vollendete_jahre', period)
        bezieht_taggeld = person('iv_bezieht_taggeld', period)
        iv_grad = person('iv_invaliditaetsgrad_prozent', period.this_year)
        wohnsitz_ch = person('iv_wohnsitz_schweiz', period)
        rentenanspruch = person('iv_rentenanspruch', period)

        # Abs. 1: mindestens 6 Monate und mindestens 18 Jahre alt
        wartefrist_erfuellt = monate_seit_anspruch >= 6
        alter_erfuellt = alter >= 18

        # Abs. 2: kein Anspruch waehrend Taggeld
        kein_taggeld = not_(bezieht_taggeld)

        # Abs. 4: IV < 50% nur bei Wohnsitz Schweiz
        wohnsitz_ok = (iv_grad >= 50) + wohnsitz_ch > 0

        return (
            rentenanspruch
            * wartefrist_erfuellt
            * alter_erfuellt
            * kein_taggeld
            * wohnsitz_ok
        )
