"""SR 451.51 Art. 4

Generated from: ch/451/de/451.51.md
Finanzhilfe zur Erhaltung naturnaher Kulturlandschaften - bis 80%, ausnahmsweise 100%.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class anrechenbare_kosten_kulturlandschaft(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Anrechenbare Kosten fuer Massnahme zur Erhaltung naturnaher Kulturlandschaft in CHF"
    reference = "SR 451.51 Art. 4"


class massnahme_ausserordentliche_bedeutung(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Massnahme ist von ausserordentlicher Bedeutung (Ausnahmefall bis 100%)"
    reference = "SR 451.51 Art. 4"


class finanzhilfe_kulturlandschaft_max(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Maximaler Finanzhilfebetrag fuer Kulturlandschaftsmassnahme in CHF"
    reference = "SR 451.51 Art. 4"

    def formula(person, period, parameters):
        kosten = person('anrechenbare_kosten_kulturlandschaft', period)
        ausnahme = person('massnahme_ausserordentliche_bedeutung', period)
        prozent = where(ausnahme, 100.0, 80.0)
        return kosten * prozent / 100.0
