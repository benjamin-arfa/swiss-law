"""SR 446.2 Art. 32

Generated from: ch/446/de/446.2.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_vollzug_jsfvg(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten fuer den Vollzug des JSFVG im jeweiligen Zustaendigkeitsbereich"
    reference = "SR 446.2 Art. 32 Abs. 1"


class kosten_erarbeitung_jugendschutzregelung(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Kosten der Branchenorganisation fuer Erarbeitung und Umsetzung der Jugendschutzregelung"
    reference = "SR 446.2 Art. 32 Abs. 2"


class kostenbeteiligung_nicht_mitglieder(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Nicht-Mitglieder muessen sich an Kosten der Jugendschutzregelung beteiligen"
    reference = "SR 446.2 Art. 32 Abs. 2"

    def formula(person, period, parameters):
        mitglied = person('ist_mitglied_branchenorganisation', period)
        return not_(mitglied)
