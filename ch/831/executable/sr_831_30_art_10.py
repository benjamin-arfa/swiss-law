"""SR 831.30 Art. 10

Generated from: ch/831/de/831.30.md

Art. 10: Anerkannte Ausgaben (Recognized expenses)

Abs. 1: For persons living at home:
  a. General living costs per year (2025 values):
     1. Single persons: CHF 20,670
     2. Married couples: CHF 31,005
     3. Children >= 11 years: CHF 10,815 (first 2 full, next 2 at 2/3, rest at 1/3)
     4. Children < 11 years: CHF 7,590 (first full, each next reduced by 1/6)
  b. Maximum recognized rent per year by region:
     1. Single person: Region 1: 18,900 / Region 2: 18,300 / Region 3: 16,680
     2. Additional for 2nd person: R1: 3,420 / R2: 3,420 / R3: 3,480
        Additional for 3rd person: R1: 2,460 / R2: 2,040 / R3: 2,040
        Additional for 4th person: R1: 2,280 / R2: 2,160 / R3: 1,800
     3. Wheelchair-accessible housing supplement: CHF 6,900

Abs. 2: For persons living in a home/hospital:
  a. Daily rate charged by the institution
  b. A cantonal amount for personal expenses
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_lebt_im_heim(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person lebt dauernd oder laenger als 3 Monate in einem Heim oder Spital"
    reference = "SR 831.30 Art. 10 Abs. 2"


class el_anzahl_kinder_ab_11(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl rentenberechtigter Kinder ab 11 Jahren"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a Ziff. 3"


class el_anzahl_kinder_unter_11(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl rentenberechtigter Kinder unter 11 Jahren"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a Ziff. 4"


class el_mietregion(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Mietregion (1, 2 oder 3) nach Art. 10 Abs. 1quater ELG"
    reference = "SR 831.30 Art. 10 Abs. 1quater"


class el_anzahl_personen_im_haushalt(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl Personen im gleichen Haushalt"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"


class el_rollstuhlgaengige_wohnung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Notwendige Miete einer rollstuhlgaengigen Wohnung"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b Ziff. 3"


class el_allgemeiner_lebensbedarf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag fuer den allgemeinen Lebensbedarf pro Jahr (Art. 10 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        import numpy as np
        ist_verheiratet = person('el_ist_verheiratet', period)

        # Base amounts (2025 values)
        betrag_alleinstehend = 20670.0
        betrag_ehepaar = 31005.0

        return np.where(ist_verheiratet, betrag_ehepaar, betrag_alleinstehend)


class el_kinderbedarf_ab_11(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Lebensbedarf fuer Kinder ab 11 Jahren (Art. 10 Abs. 1 Bst. a Ziff. 3)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a Ziff. 3"

    def formula(person, period, parameters):
        import numpy as np
        anzahl = person('el_anzahl_kinder_ab_11', period)
        betrag_voll = 10815.0

        # First 2 children: full amount each
        # Next 2 children: 2/3 each
        # Remaining: 1/3 each
        erste_zwei = np.minimum(anzahl, 2) * betrag_voll
        naechste_zwei = np.minimum(np.maximum(anzahl - 2, 0), 2) * betrag_voll * (2.0 / 3.0)
        weitere = np.maximum(anzahl - 4, 0) * betrag_voll * (1.0 / 3.0)

        return erste_zwei + naechste_zwei + weitere


class el_kinderbedarf_unter_11(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Lebensbedarf fuer Kinder unter 11 Jahren (Art. 10 Abs. 1 Bst. a Ziff. 4)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. a Ziff. 4"

    def formula(person, period, parameters):
        import numpy as np
        anzahl = person('el_anzahl_kinder_unter_11', period)
        betrag_erstes = 7590.0

        # First child: full amount
        # Each subsequent: reduced by 1/6 of previous
        # Child 1: 7590, Child 2: 7590*5/6=6325, Child 3: 6325*5/6=5271
        # Child 4: 5271*5/6=4392, Child 5+: 4392*5/6=3660
        betraege = np.array([7590.0, 6325.0, 5271.0, 4392.0, 3660.0])

        total = np.zeros_like(anzahl, dtype=float)
        for i in range(5):
            total = total + np.where(anzahl > i, betraege[i], 0.0)
        # Children beyond 5th get same as 5th
        total = total + np.maximum(anzahl - 5, 0) * betraege[4]

        return total


class el_maximale_mietkosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechstbetrag der anerkannten Mietkosten pro Jahr (Art. 10 Abs. 1 Bst. b ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        import numpy as np
        region = person('el_mietregion', period)
        n_personen = person('el_anzahl_personen_im_haushalt', period)
        rollstuhl = person('el_rollstuhlgaengige_wohnung', period)

        # Base amount for single person by region
        basis_r1 = 18900.0
        basis_r2 = 18300.0
        basis_r3 = 16680.0

        basis = np.where(region == 1, basis_r1, np.where(region == 2, basis_r2, basis_r3))

        # Additional for 2nd person
        zusatz_2_r1, zusatz_2_r2, zusatz_2_r3 = 3420.0, 3420.0, 3480.0
        zusatz_2 = np.where(region == 1, zusatz_2_r1, np.where(region == 2, zusatz_2_r2, zusatz_2_r3))

        # Additional for 3rd person
        zusatz_3_r1, zusatz_3_r2, zusatz_3_r3 = 2460.0, 2040.0, 2040.0
        zusatz_3 = np.where(region == 1, zusatz_3_r1, np.where(region == 2, zusatz_3_r2, zusatz_3_r3))

        # Additional for 4th person
        zusatz_4_r1, zusatz_4_r2, zusatz_4_r3 = 2280.0, 2160.0, 1800.0
        zusatz_4 = np.where(region == 1, zusatz_4_r1, np.where(region == 2, zusatz_4_r2, zusatz_4_r3))

        miete = basis
        miete = miete + np.where(n_personen >= 2, zusatz_2, 0.0)
        miete = miete + np.where(n_personen >= 3, zusatz_3, 0.0)
        miete = miete + np.where(n_personen >= 4, zusatz_4, 0.0)

        # Wheelchair supplement
        miete = miete + np.where(rollstuhl, 6900.0, 0.0)

        return miete


class el_anerkannte_ausgaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total anerkannte Ausgaben fuer zu Hause lebende Personen (Art. 10 Abs. 1 ELG)"
    reference = "SR 831.30 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        lebensbedarf = person('el_allgemeiner_lebensbedarf', period)
        kinder_ab_11 = person('el_kinderbedarf_ab_11', period)
        kinder_unter_11 = person('el_kinderbedarf_unter_11', period)
        miete = person('el_maximale_mietkosten', period)

        return lebensbedarf + kinder_ab_11 + kinder_unter_11 + miete
