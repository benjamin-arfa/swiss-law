"""SR 221.213.2 Art. 41

Generated from: ch/221/de/221.213.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class vereinbarte_fortsetzungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Vereinbarte Fortsetzungsdauer in Jahren"
    reference = "SR 221.213.2 Art. 41"


class gesetzliche_fortsetzungsdauer_jahre(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Gesetzliche Fortsetzungsdauer in Jahren (6 Jahre gemäss Art. 8)"
    reference = "SR 221.213.2 Art. 41"

    def formula(person, period, parameters):
        return person.filled_array(6)


class zuschlag_laengere_pachtdauer_zulaessig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Zuschlag von 15% zum Pachtzins wegen längerer Pachtdauer ist zulässig"
    reference = "SR 221.213.2 Art. 41"

    def formula(person, period, parameters):
        vereinbart = person('vereinbarte_fortsetzungsdauer_jahre', period)
        gesetzlich = person('gesetzliche_fortsetzungsdauer_jahre', period)
        # Mindestens 3 Jahre über gesetzliche Fortsetzungsdauer
        return vereinbart >= (gesetzlich + 3)


class zuschlag_laengere_pachtdauer_prozent(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Zulässiger Zuschlag zum Pachtzins in Prozent"
    reference = "SR 221.213.2 Art. 41"

    def formula(person, period, parameters):
        zulaessig = person('zuschlag_laengere_pachtdauer_zulaessig', period)
        return where(zulaessig, 0.15, 0.0)
