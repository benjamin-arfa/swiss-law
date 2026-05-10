"""SR 831.30 Art. 5

Generated from: ch/831/de/831.30.md

Art. 5: Zusaetzliche Voraussetzungen fuer Auslaenderinnen und Auslaender
(Additional requirements for foreign nationals)

Abs. 1: Foreign nationals must have resided legally and continuously
in Switzerland for 10 years (waiting period / Karenzfrist).
Abs. 2: For refugees and stateless persons, the waiting period is 5 years.
Abs. 3: Reduced waiting periods for certain social security agreement cases.
Abs. 5: Waiting period restarts if abroad > 3 months continuously or
> 3 months total in a calendar year.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class el_ist_schweizer_staatsangehoeriger(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist Schweizer Staatsangehoerige/r"
    reference = "SR 831.30 Art. 5"


class el_ist_fluechtling_oder_staatenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person ist anerkannter Fluechtling oder staatenlos"
    reference = "SR 831.30 Art. 5 Abs. 2"


class el_hat_sozialversicherungsabkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person faellt unter ein Sozialversicherungsabkommen (Art. 5 Abs. 3)"
    reference = "SR 831.30 Art. 5 Abs. 3"


class el_bezieht_altersrente_ohne_abloesung(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Person bezieht Altersrente AHV ohne Abloesung einer Hinterlassenen- oder IV-Rente"
    reference = "SR 831.30 Art. 5 Abs. 3 Bst. d"


class el_aufenthaltsdauer_schweiz_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ununterbrochene Aufenthaltsdauer in der Schweiz in Jahren"
    reference = "SR 831.30 Art. 5 Abs. 1"


class el_auslandaufenthalt_ueber_3_monate(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Auslandaufenthalt von mehr als 3 Monaten (ununterbrochen oder kumuliert)"
    reference = "SR 831.30 Art. 5 Abs. 5"


class el_karenzfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anwendbare Karenzfrist in Jahren (Art. 5 ELG)"
    reference = "SR 831.30 Art. 5"

    def formula(person, period, parameters):
        import numpy as np
        ist_schweizer = person('el_ist_schweizer_staatsangehoeriger', period)
        ist_fluechtling = person('el_ist_fluechtling_oder_staatenlos', period)
        hat_abkommen = person('el_hat_sozialversicherungsabkommen', period)
        altersrente_ohne_abloesung = person('el_bezieht_altersrente_ohne_abloesung', period)

        # Swiss nationals: no waiting period
        # Refugees/stateless: 5 years
        # Social security agreement (Art. 5 Abs. 3 a-c): 5 years
        # Social security agreement (Art. 5 Abs. 3 d): 10 years
        # All other foreigners: 10 years
        return np.where(
            ist_schweizer, 0,
            np.where(
                ist_fluechtling, 5,
                np.where(
                    hat_abkommen * not_(altersrente_ohne_abloesung), 5,
                    10
                )
            )
        )


class el_karenzfrist_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Karenzfrist fuer Ergaenzungsleistungen ist erfuellt (Art. 5 ELG)"
    reference = "SR 831.30 Art. 5"

    def formula(person, period, parameters):
        ist_schweizer = person('el_ist_schweizer_staatsangehoeriger', period)
        aufenthalt = person('el_aufenthaltsdauer_schweiz_jahre', period)
        karenzfrist = person('el_karenzfrist_jahre', period)
        ausland_unterbruch = person('el_auslandaufenthalt_ueber_3_monate', period)

        # Swiss nationals always qualify (no waiting period)
        # Others: residence >= waiting period AND no interruption
        return ist_schweizer + (not_(ist_schweizer) * (aufenthalt >= karenzfrist) * not_(ausland_unterbruch))
