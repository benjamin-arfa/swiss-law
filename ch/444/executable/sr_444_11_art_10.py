"""SR 444.11 Art. 10

Generated from: ch/444/de/444.11.md

Hoechstansatz der Finanzhilfen: Max 50% der geltend gemachten Kosten.
Nur im Rahmen bewilligter Kredite.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kosten_kulturgueter_projekt(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Geltend gemachte Kosten fuer Kulturgueterprojekt (CHF)"
    reference = "SR 444.11 Art. 10 Abs. 1"


class max_finanzhilfe_kulturgueter(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximale Finanzhilfe fuer Kulturguetertransfer (max 50% Kosten)"
    reference = "SR 444.11 Art. 10 Abs. 1"

    def formula(person, period, parameters):
        kosten = person('kosten_kulturgueter_projekt', period)
        return kosten * 0.50
