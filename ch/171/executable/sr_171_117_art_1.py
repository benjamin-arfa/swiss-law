"""SR 171.117 Art. 1

Generated from: ch/171/de/171.117.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class apk_zustaendig_fuer_parlamentsbeziehungen(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Die Aussenpolitischen Kommissionen sind zuständig für die Pflege der Beziehungen zu Parlamenten anderer Staaten"
    reference = "SR 171.117 Art. 1 Abs. 1"

    def formula(person, period, parameters):
        staendige_delegation_eingesetzt = person('staendige_delegation_eingesetzt', period)
        nicht_staendige_delegation_eingesetzt = person('nicht_staendige_delegation_eingesetzt', period)
        return not_(staendige_delegation_eingesetzt) * not_(nicht_staendige_delegation_eingesetzt)


class staendige_delegation_eingesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine ständige Delegation nach Art. 4 ist eingesetzt"
    reference = "SR 171.117 Art. 1 Abs. 1"


class nicht_staendige_delegation_eingesetzt(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Eine nicht ständige Delegation nach Art. 5 ist eingesetzt"
    reference = "SR 171.117 Art. 1 Abs. 1"


class max_mitglieder_apk_delegation_nationalrat(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Kommissionsmitglieder in nicht ständigen Delegationen der APK des Nationalrates"
    reference = "SR 171.117 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return 8


class max_mitglieder_apk_delegation_staenderat(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Kommissionsmitglieder in nicht ständigen Delegationen der APK des Ständerates"
    reference = "SR 171.117 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return 6


class max_mitglieder_gemeinsame_apk_delegation(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Maximale Anzahl Kommissionsmitglieder in gemeinsamen nicht ständigen APK-Delegationen"
    reference = "SR 171.117 Art. 1 Abs. 3"

    def formula(person, period, parameters):
        return 8
