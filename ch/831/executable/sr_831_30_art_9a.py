"""SR 831.30 Art. 9a

Generated from: ch/831/de/831.30.md

Art. 9a: Voraussetzungen hinsichtlich des Vermoegens - Asset thresholds
for EL eligibility (introduced by EL Reform 2021):
a. Single persons: net assets below CHF 100,000
b. Couples: net assets below CHF 200,000
c. Pension-entitled orphans/children: net assets below CHF 50,000

Abs. 2: Owner-occupied property is excluded from net assets.
Abs. 3: Assets voluntarily renounced (Art. 11a) count towards net assets.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR


class el_reinvermoegen(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Reinvermoegen der Person (Art. 9a ELG)"
    reference = "SR 831.30 Art. 9a Abs. 1"


class el_ist_alleinstehend(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist alleinstehend (nicht verheiratet)"
    reference = "SR 831.30 Art. 9a Abs. 1 Bst. a"


class el_ist_ehepaar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist Teil eines Ehepaares"
    reference = "SR 831.30 Art. 9a Abs. 1 Bst. b"


class el_ist_waise_oder_kind(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Person ist rentenberechtigte Waise oder Kind mit Kinderrentenanspruch"
    reference = "SR 831.30 Art. 9a Abs. 1 Bst. c"


class el_vermoegensschwelle(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Vermoegensschwelle fuer EL-Anspruch (Art. 9a ELG)"
    reference = "SR 831.30 Art. 9a Abs. 1"

    def formula(person, period, parameters):
        alleinstehend = person('el_ist_alleinstehend', period.first_month)
        ehepaar = person('el_ist_ehepaar', period.first_month)
        waise = person('el_ist_waise_oder_kind', period.first_month)

        schwelle = select(
            [waise, ehepaar, alleinstehend],
            [50000, 200000, 100000],
            default=100000,
        )
        return schwelle


class el_vermoegen_unter_schwelle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Reinvermoegen liegt unter Vermoegensschwelle (Art. 9a ELG)"
    reference = "SR 831.30 Art. 9a"

    def formula(person, period, parameters):
        vermoegen = person('el_reinvermoegen', period)
        schwelle = person('el_vermoegensschwelle', period)
        return vermoegen < schwelle
