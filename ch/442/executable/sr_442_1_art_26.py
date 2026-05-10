"""SR 442.1 Art. 26

Generated from: ch/442/de/442.1.md

Verfahrensrechtliche Bestimmungen: Bei Finanzhilfen ueber 100'000 CHF gelten
allgemeine Bestimmungen. Bei Beschwerden bis 100'000 CHF gilt ein vereinfachtes
Verfahren. Ruege der Unangemessenheit ist unzulaessig.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class betrag_finanzhilfe_kulturfoerderung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Betrag der Finanzhilfe (CHF)"
    reference = "SR 442.1 Art. 26"


class vereinfachtes_verfahren_anwendbar(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob das vereinfachte und verkuerzte Verfahren fuer Beschwerden anwendbar ist"
    reference = "SR 442.1 Art. 26 Abs. 1"

    def formula(person, period, parameters):
        betrag = person('betrag_finanzhilfe_kulturfoerderung', period)
        return betrag <= 100000


class ruege_unangemessenheit_zulaessig(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob die Ruege der Unangemessenheit zulaessig ist (immer False bei Kulturfoerderung)"
    reference = "SR 442.1 Art. 26 Abs. 2"
    default_value = False
