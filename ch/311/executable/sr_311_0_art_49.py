"""SR 311.0 Art. 49

Generated from: ch/fr/311/311.0.md

Art. 49: Concours (Konkurrenz / Concurrent offences)
- Abs. 1: When multiple acts fulfill conditions for multiple penalties of the same kind,
  the court sentences based on the most serious offence and increases appropriately.
  Must not exceed 1.5x the maximum for that offence. Bound by legal maximum per type.
- Abs. 2: For offences committed before a previous conviction, complementary penalty
  so the offender is not punished more severely than if judged together.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class stgb_schwerste_einzelstrafe_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Strafe fuer die schwerste Einzeltat in Monaten"
    reference = "SR 311.0 Art. 49 Abs. 1"


class stgb_anzahl_konkurrierender_taten(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Anzahl der in Konkurrenz stehenden Straftaten"
    reference = "SR 311.0 Art. 49 Abs. 1"


class stgb_hoechststrafe_schwerste_tat_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Gesetzliche Hoechststrafe fuer die schwerste Tat in Monaten"
    reference = "SR 311.0 Art. 49 Abs. 1"


class stgb_gesamtstrafe_obergrenze_monate(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Obergrenze der Gesamtstrafe bei Konkurrenz in Monaten"
    reference = "SR 311.0 Art. 49 Abs. 1"

    def formula(person, period, parameters):
        hoechststrafe = person('stgb_hoechststrafe_schwerste_tat_monate', period)
        # Maximum: 1.5x the maximum for the most serious offence
        obergrenze = hoechststrafe * 1.5
        # But never exceeding 20 years (240 months) for non-life sentences
        return min_(obergrenze, 240)
