"""SR 442.133 Art. 9

Generated from: ch/442/de/442.133.md

Verwendung der Finanzhilfen:
- Beitraege an Talente: min 50%
- Unterstuetzung Leistungserbringer: max 40% (max Kanton+Gemeinden-Anteil)
- Verwaltung: max 10%
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class finanzhilfe_junge_talente_musik(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Jaehrliche Finanzhilfe Junge Talente Musik (CHF)"
    reference = "SR 442.133 Art. 9"


class finanzierung_kanton_gemeinden_leistungserbringer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Finanzierungsanteil Kanton und Gemeinden an Leistungserbringer (CHF)"
    reference = "SR 442.133 Art. 9 Abs. 1 Bst. b"


class min_anteil_talent_beitraege(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Mindestanteil fuer Beitraege an Talente (min 50%)"
    reference = "SR 442.133 Art. 9 Abs. 1 Bst. a"

    def formula(person, period, parameters):
        hilfe = person('finanzhilfe_junge_talente_musik', period)
        return hilfe * 0.50


class max_anteil_leistungserbringer(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximalanteil fuer Leistungserbringer (max 40%, max Kanton+Gemeinden)"
    reference = "SR 442.133 Art. 9 Abs. 1 Bst. b"

    def formula(person, period, parameters):
        hilfe = person('finanzhilfe_junge_talente_musik', period)
        kg_anteil = person('finanzierung_kanton_gemeinden_leistungserbringer', period)
        import numpy as np
        return np.minimum(hilfe * 0.40, kg_anteil)


class max_anteil_verwaltung(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Maximalanteil fuer Verwaltungsaufgaben (max 10%)"
    reference = "SR 442.133 Art. 9 Abs. 1 Bst. c"

    def formula(person, period, parameters):
        hilfe = person('finanzhilfe_junge_talente_musik', period)
        return hilfe * 0.10
