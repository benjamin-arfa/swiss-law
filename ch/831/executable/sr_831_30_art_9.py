"""SR 831.30 Art. 9

Generated from: ch/831/de/831.30.md

Art. 9: Berechnung und Hoehe der jaehrlichen Ergaenzungsleistung

Abs. 1: The annual supplementary benefit equals the amount by which
recognized expenses exceed countable income, but at least the higher of:
  a. The highest premium reduction the canton sets for persons receiving
     neither EL nor social assistance
  b. 60% of the flat-rate amount for mandatory health insurance (Art. 10(3)(d))
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_kantonale_praemienverbilligung_maximum(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Hoechste kantonale Praemienverbilligung fuer Personen ohne EL/Sozialhilfe"
    reference = "SR 831.30 Art. 9 Abs. 1 Bst. a"


class el_pauschalbetrag_krankenpflege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Pauschalbetrag fuer obligatorische Krankenpflegeversicherung (Art. 10 Abs. 3 Bst. d)"
    reference = "SR 831.30 Art. 9 Abs. 1 Bst. b"


class el_jaehrliche_ergaenzungsleistung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Ergaenzungsleistung in CHF (Art. 9 ELG)"
    reference = "SR 831.30 Art. 9"

    def formula(person, period, parameters):
        import numpy as np
        ausgaben = person('el_anerkannte_ausgaben', period)
        einnahmen = person('el_anrechenbare_einnahmen', period)
        pv_max = person('el_kantonale_praemienverbilligung_maximum', period)
        pauschale_kv = person('el_pauschalbetrag_krankenpflege', period)

        # Difference between recognized expenses and countable income
        differenz = np.maximum(ausgaben - einnahmen, 0.0)

        # Minimum amount: higher of (a) cantonal premium reduction max or
        # (b) 60% of health insurance flat rate
        mindestbetrag = np.maximum(pv_max, pauschale_kv * 0.60)

        # EL is at least the minimum amount (if entitled)
        return np.maximum(differenz, mindestbetrag)
