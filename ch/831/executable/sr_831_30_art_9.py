"""SR 831.30 Art. 9

Generated from: ch/831/de/831.30.md

Art. 9: Berechnung und Hoehe der jaehrlichen Ergaenzungsleistung -
The annual supplementary benefit equals the amount by which recognized
expenses exceed countable income, but at least the higher of:
a. the highest premium reduction the canton sets for persons receiving
   neither EL nor social welfare
b. 60% of the lump-sum amount for mandatory health insurance (Art. 10(3)(d))

Abs. 2: Expenses and income of spouses and persons with pension-entitled
orphans or children are aggregated.
Abs. 3: For couples where one/both live in a home/hospital, EL is
calculated separately per spouse.
Abs. 4: Children whose income exceeds expenses are excluded.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_anerkannte_ausgaben(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anerkannte Ausgaben total (Art. 10 ELG)"
    reference = "SR 831.30 Art. 9 Abs. 1"


class el_anrechenbare_einnahmen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Anrechenbare Einnahmen total (Art. 11 ELG)"
    reference = "SR 831.30 Art. 9 Abs. 1"


class el_kantonale_praemienverbilligung_max(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechste kantonale Praemienverbilligung fuer Nicht-EL/Sozialhilfe-Bezueger (Art. 9 Abs. 1 Bst. a ELG)"
    reference = "SR 831.30 Art. 9 Abs. 1 Bst. a"


class el_pauschale_krankenpflege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalbetrag obligatorische Krankenpflegeversicherung (Art. 10 Abs. 3 Bst. d ELG)"
    reference = "SR 831.30 Art. 10 Abs. 3 Bst. d"


class el_jaehrliche_el_berechnet(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Berechnete jaehrliche Ergaenzungsleistung (Art. 9 ELG)"
    reference = "SR 831.30 Art. 9"

    def formula(person, period, parameters):
        ausgaben = person('el_anerkannte_ausgaben', period)
        einnahmen = person('el_anrechenbare_einnahmen', period)

        # EL = recognized expenses - countable income
        ausgabenueberschuss = max_(ausgaben - einnahmen, 0)

        # Minimum EL: higher of (a) cantonal premium reduction or (b) 60% of health insurance lump sum
        praemienverbilligung = person('el_kantonale_praemienverbilligung_max', period)
        pauschale_kv = person('el_pauschale_krankenpflege', period)
        mindest_el_b = pauschale_kv * 0.60

        mindest_el = max_(praemienverbilligung, mindest_el_b)

        return max_(ausgabenueberschuss, mindest_el)
