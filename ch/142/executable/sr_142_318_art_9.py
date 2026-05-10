"""SR 142.318 Art. 9

Generated from: ch/142/de/142.318.md

Ausreisefristen: Im beschleunigten Verfahren 7-30 Tage.
Dublin-Verfahren richtet sich nach Art. 45 Abs. 3 AsylG,
Frist kann bis 30 Tage verlaengert werden. Ausserordentliche
Lage wegen Coronavirus erfordert laengere Fristen.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ist_beschleunigtes_verfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob das beschleunigte Asylverfahren anwendbar ist"
    reference = "SR 142.318 Art. 9 Abs. 1"


class ist_dublin_verfahren(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die Person aufgrund der Dublin-Assoziierungsabkommen weggewiesen wird"
    reference = "SR 142.318 Art. 9 Abs. 2"


class ausserordentliche_lage_coronavirus(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = MONTH
    label = "Ob die ausserordentliche Lage aufgrund des Coronavirus eine Fristverlaengerung erfordert"
    reference = "SR 142.318 Art. 9 Abs. 3"


class ausreisefrist_min_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Minimale Ausreisefrist in Tagen"
    reference = "SR 142.318 Art. 9 Abs. 1"

    def formula_2020_04(person, period, parameters):
        return where(
            person('ist_beschleunigtes_verfahren', period),
            parameters(period).ausreisefrist_beschleunigt_min_tage,
            0
        )


class ausreisefrist_max_tage(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = MONTH
    label = "Maximale Ausreisefrist in Tagen"
    reference = "SR 142.318 Art. 9 Abs. 1-2"

    def formula_2020_04(person, period, parameters):
        return parameters(period).ausreisefrist_max_tage
