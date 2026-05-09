"""SR 831.30 Art. 5

Generated from: ch/831/de/831.30.md

Art. 5: Zusaetzliche Voraussetzungen fuer Auslaenderinnen und Auslaender -
Additional requirements for foreign nationals:
- Abs. 1: Lawful residence + 10 years continuous residence (waiting period)
- Abs. 2: Refugees and stateless persons: 5 years waiting period
- Abs. 3: Persons entitled to extraordinary AHV/IV pensions via social
  security agreements: 5 or 10 years depending on pension type
- Abs. 5: Waiting period restarts if abroad >3 months continuously or
  >3 months total in a calendar year
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_ist_auslaender(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Auslaenderin oder Auslaender"
    reference = "SR 831.30 Art. 5"


class el_ist_fluechtling_oder_staatenlos(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Fluechtling oder staatenlos (Art. 5 Abs. 2 ELG)"
    reference = "SR 831.30 Art. 5 Abs. 2"


class el_aufenthaltsdauer_schweiz_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Ununterbrochene Aufenthaltsdauer in der Schweiz in Jahren"
    reference = "SR 831.30 Art. 5 Abs. 1"


class el_rechtmaessiger_aufenthalt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Rechtmaessiger Aufenthalt in der Schweiz"
    reference = "SR 831.30 Art. 5 Abs. 1"


class el_karenzfrist_jahre(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Karenzfrist in Jahren fuer EL-Anspruch (Art. 5 ELG)"
    reference = "SR 831.30 Art. 5"

    def formula(person, period, parameters):
        ist_auslaender = person('el_ist_auslaender', period.first_month)
        ist_fluechtling = person('el_ist_fluechtling_oder_staatenlos', period.first_month)

        # Abs. 2: Refugees/stateless: 5 years
        # Abs. 1: Other foreigners: 10 years
        # Swiss citizens: 0 years (no waiting period)
        karenzfrist = select(
            [
                not_(ist_auslaender),
                ist_fluechtling,
                ist_auslaender,
            ],
            [0, 5, 10],
        )
        return karenzfrist


class el_karenzfrist_erfuellt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Karenzfrist fuer EL-Anspruch ist erfuellt (Art. 5 ELG)"
    reference = "SR 831.30 Art. 5"

    def formula(person, period, parameters):
        karenzfrist = person('el_karenzfrist_jahre', period)
        aufenthalt = person('el_aufenthaltsdauer_schweiz_jahre', period)
        return aufenthalt >= karenzfrist
