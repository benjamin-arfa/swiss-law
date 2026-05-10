"""SR 831.461.3 Art. 2

Generated from: ch/831/de/831.461.3.md

Beneficiaries of pillar 3a in case of death, in order of priority:
1. Surviving spouse or registered partner
2. Direct descendants, persons substantially supported by the deceased,
   persons who lived with the deceased for at least 5 years, or persons
   who must support common children
3. Parents
4. Siblings
5. Other heirs
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class bvv3_beguenstigter_ehegatte(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein ueberlebender Ehegatte oder eingetragener Partner als Beguenstigter der Saeule 3a vorhanden ist"
    reference = "SR 831.461.3 Art. 2 Abs. 1 Bst. b Ziff. 1"


class bvv3_beguenstigter_nachkommen(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob direkte Nachkommen oder unterstuetzte Personen als Beguenstigte vorhanden sind"
    reference = "SR 831.461.3 Art. 2 Abs. 1 Bst. b Ziff. 2"


class bvv3_beguenstigter_eltern(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Eltern als Beguenstigte vorhanden sind"
    reference = "SR 831.461.3 Art. 2 Abs. 1 Bst. b Ziff. 3"


class bvv3_beguenstigter_geschwister(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Geschwister als Beguenstigte vorhanden sind"
    reference = "SR 831.461.3 Art. 2 Abs. 1 Bst. b Ziff. 4"


class bvv3_beguenstigungsrang(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Rang der Beguenstigung bei Tod des Vorsorgenehmers (1=hoechste Prioritaet, 5=niedrigste)"
    reference = "SR 831.461.3 Art. 2 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        ehegatte = person('bvv3_beguenstigter_ehegatte', period)
        nachkommen = person('bvv3_beguenstigter_nachkommen', period)
        eltern = person('bvv3_beguenstigter_eltern', period)
        geschwister = person('bvv3_beguenstigter_geschwister', period)

        return select(
            [ehegatte, nachkommen, eltern, geschwister],
            [1, 2, 3, 4],
            default=5,
        )
