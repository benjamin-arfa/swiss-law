"""SR 251.5 Art. 5

Generated from: ch/251/de/251.5.md

Erschwerende Umstaende: Erhoehung des Betrags bei wiederholten Verstoessen,
besonders hohem Gewinn, Behinderung der Zusammenarbeit, Anstiftung oder
Vergeltungsmassnahmen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class wiederholter_verstoss(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen wiederholt gegen das Kartellgesetz verstossen hat"
    reference = "SR 251.5 Art. 5 Abs. 1 Bst. a"


class besonders_hoher_gewinn(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob mit dem Verstoss ein besonders hoher Gewinn erzielt wurde"
    reference = "SR 251.5 Art. 5 Abs. 1 Bst. b"


class zusammenarbeit_verweigert(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Zusammenarbeit mit den Behoerden verweigert oder die Untersuchung behindert wurde"
    reference = "SR 251.5 Art. 5 Abs. 1 Bst. c"


class anstiftende_oder_fuehrende_rolle(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das Unternehmen zur Wettbewerbsbeschraenkung angestiftet oder eine fuehrende Rolle gespielt hat"
    reference = "SR 251.5 Art. 5 Abs. 2 Bst. a"


class vergeltungsmassnahmen_durchgefuehrt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob Vergeltungsmassnahmen zur Durchsetzung der Abrede angeordnet oder durchgefuehrt wurden"
    reference = "SR 251.5 Art. 5 Abs. 2 Bst. b"


class erschwerende_umstaende_zuschlag_prozent(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Prozentualer Zuschlag wegen erschwerender Umstaende"
    reference = "SR 251.5 Art. 5"


class sanktion_nach_erschwerend(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Sanktionsbetrag nach Beruecksichtigung erschwerender Umstaende"
    reference = "SR 251.5 Art. 5"

    def formula(person, period, parameters):
        betrag = person('sanktion_nach_dauer', period)
        zuschlag = person('erschwerende_umstaende_zuschlag_prozent', period)
        return betrag * (1 + zuschlag / 100)
