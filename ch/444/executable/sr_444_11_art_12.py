"""SR 444.11 Art. 12

Generated from: ch/444/de/444.11.md

Finanzhilfen an Projekte: Einmaliger Pauschalbeitrag max 100'000 CHF.
In Ausnahmefaellen max 1 Mio CHF (durch Bundesrat).
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_ausnahmefall_bundesrat(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Ob ein Ausnahmefall vorliegt (Antrag EDI an Bundesrat)"
    reference = "SR 444.11 Art. 12 Abs. 2"


class max_finanzhilfe_projekt_kulturerbe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Finanzhilfe an Projekte zur Erhaltung des kulturellen Erbes"
    reference = "SR 444.11 Art. 12"

    def formula(person, period, parameters):
        ausnahme = person('ist_ausnahmefall_bundesrat', period)
        return ausnahme * 1000000 + (1 - ausnahme) * 100000
