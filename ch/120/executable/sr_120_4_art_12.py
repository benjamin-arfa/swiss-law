"""SR 120.4 Art. 12

Generated from: ch/120/de/120.4.md

Erweiterte Personensicherheitspruefung mit Befragung: Highest level check
for persons with extensive insight into government activities or security.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class weitreichender_einblick_regierungstaetigkeit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessiger weitreichender Einblick in Regierungstaetigkeit oder sicherheitspolitische Geschaefte"
    reference = "SR 120.4 Art. 12 Abs. 1 lit. a"


class zugang_geheimnisse_sicherheit(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Regelmaessiger Zugang zu Geheimnissen der inneren/aeusseren Sicherheit"
    reference = "SR 120.4 Art. 12 Abs. 1 lit. b"


class vom_bundesrat_ernannt(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Person vom Bundesrat ernannt wird"
    reference = "SR 120.4 Art. 12 Abs. 2 lit. a"


class erweiterte_psp_mit_befragung_erforderlich(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob eine erweiterte PSP mit Befragung erforderlich ist"
    reference = "SR 120.4 Art. 12"

    def formula(person, period, parameters):
        # Abs. 1: PSP VBS zustaendig
        einblick = person('weitreichender_einblick_regierungstaetigkeit', period)
        geheimnisse = person('zugang_geheimnisse_sicherheit', period)

        # Abs. 2: PSP BK zustaendig - Vom Bundesrat ernannte Personen
        bundesrat_ernannt = person('vom_bundesrat_ernannt', period)

        return (einblick + geheimnisse + bundesrat_ernannt) > 0
