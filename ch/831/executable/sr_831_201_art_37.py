"""SR 831.201 Art. 37

Generated from: ch/831/de/831.201.md

Hilflosigkeit: Bemessung (Assessment of helplessness)
- Abs. 1: Severe (schwer) = fully helpless: needs help in ALL daily activities
  AND needs permanent care or personal supervision
- Abs. 2: Moderate (mittelschwer) = one of three alternatives:
  a. needs help in MOST daily activities, or
  b. needs help in >= 2 activities AND permanent personal supervision, or
  c. needs help in >= 2 activities AND permanent life-skills assistance (Art. 38)
- Abs. 3: Mild (leicht) = one of five alternatives:
  a. needs help in >= 2 daily activities, or
  b. needs permanent personal supervision, or
  c. needs permanent, especially costly care due to disability, or
  d. can only maintain social contacts with regular substantial third-party help, or
  e. needs permanent life-skills assistance (Art. 38)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class iv_anzahl_betroffene_lebensverrichtungen(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl alltaeglicher Lebensverrichtungen, bei denen regelmaessig erhebliche Hilfe Dritter benoetigt wird"
    reference = "SR 831.201 Art. 37"


class iv_anzahl_alltaegliche_lebensverrichtungen_total(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesamtzahl der alltaeglichen Lebensverrichtungen (in der Regel 6)"
    reference = "SR 831.201 Art. 37"
    default_value = 6


class iv_benoetigt_dauerpflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person der dauernden Pflege bedarf"
    reference = "SR 831.201 Art. 37 Abs. 1"


class iv_benoetigt_persoenliche_ueberwachung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person der dauernden persoenlichen Ueberwachung bedarf"
    reference = "SR 831.201 Art. 37 Abs. 1-3"


class iv_benoetigt_lebenspraktische_begleitung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person dauernd auf lebenspraktische Begleitung (Art. 38) angewiesen ist"
    reference = "SR 831.201 Art. 37 Abs. 2-3 / Art. 38"


class iv_benoetigt_aufwendige_pflege(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person einer durch Gebrechen bedingten staendig besonders aufwendigen Pflege bedarf"
    reference = "SR 831.201 Art. 37 Abs. 3 Bst. c"


class iv_benoetigt_hilfe_soziale_kontakte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person nur dank erheblicher Dienstleistungen Dritter gesellschaftliche Kontakte pflegen kann"
    reference = "SR 831.201 Art. 37 Abs. 3 Bst. d"


class iv_hilflosigkeit_grad(Variable):
    value_type = str
    entity_key = 'person'
    definition_period = MONTH
    label = "Grad der Hilflosigkeit: schwer, mittelschwer, leicht, oder keine"
    reference = "SR 831.201 Art. 37"

    def formula(person, period, parameters):
        import numpy as np
        n_betroffen = person('iv_anzahl_betroffene_lebensverrichtungen', period)
        n_total = person('iv_anzahl_alltaegliche_lebensverrichtungen_total', period)
        dauerpflege = person('iv_benoetigt_dauerpflege', period)
        ueberwachung = person('iv_benoetigt_persoenliche_ueberwachung', period)
        begleitung = person('iv_benoetigt_lebenspraktische_begleitung', period)
        aufwendige_pflege = person('iv_benoetigt_aufwendige_pflege', period)
        hilfe_kontakte = person('iv_benoetigt_hilfe_soziale_kontakte', period)

        # Abs. 1: Severe - all activities affected AND (permanent care OR supervision)
        schwer = (n_betroffen >= n_total) & (dauerpflege | ueberwachung)

        # Abs. 2: Moderate - one of three alternatives
        mittelschwer_a = n_betroffen >= (n_total - 1)  # "most" daily activities
        mittelschwer_b = (n_betroffen >= 2) & ueberwachung
        mittelschwer_c = (n_betroffen >= 2) & begleitung
        mittelschwer = ~schwer & (mittelschwer_a | mittelschwer_b | mittelschwer_c)

        # Abs. 3: Mild - one of five alternatives
        leicht_a = n_betroffen >= 2
        leicht_b = ueberwachung
        leicht_c = aufwendige_pflege
        leicht_d = hilfe_kontakte
        leicht_e = begleitung
        leicht = ~schwer & ~mittelschwer & (leicht_a | leicht_b | leicht_c | leicht_d | leicht_e)

        return np.where(
            schwer, 'schwer',
            np.where(
                mittelschwer, 'mittelschwer',
                np.where(leicht, 'leicht', 'keine')
            )
        )
