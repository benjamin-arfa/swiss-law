"""SR 861.1 Art. 18

Generated from: ch/861/de/861.1.md

Art. 18: Bemessung der Finanzhilfen für Projekte mit Innovationscharakter
- Max 1/3 of project costs (concept development, realization, evaluation)
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class kbfhv_innovationsprojekt_kosten(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Projektkosten für Innovationsprojekt (Detailkonzept, Realisierung, Evaluation) (CHF)"
    reference = "SR 861.1 Art. 18"


class kbfhv_innovationsprojekt_finanzhilfe(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzhilfe für Projekt mit Innovationscharakter (CHF)"
    reference = "SR 861.1 Art. 18"

    def formula(person, period, parameters):
        kosten = person('kbfhv_innovationsprojekt_kosten', period)
        # Max 1/3 of project costs
        return kosten / 3.0
