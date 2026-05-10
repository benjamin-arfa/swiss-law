"""SR 442.132.3 Art. 13

Generated from: ch/442/de/442.132.3.md

Lohnnachgenuss im Todesfall: 1/6 des Jahreslohnes an Hinterbliebene.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class lohnnachgenuss_todesfall(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Lohnnachgenuss im Todesfall (1/6 Jahreslohn)"
    reference = "SR 442.132.3 Art. 13 Abs. 1"

    def formula(person, period, parameters):
        jahreslohn = person('jahreslohn_pro_helvetia', period)
        return jahreslohn / 6


class anzahl_anspruchsberechtigte_hinterbliebene(Variable):
    value_type = int
    entity_key = 'person'
    definition_period = YEAR
    label = "Anzahl anspruchsberechtigter Hinterbliebener"
    reference = "SR 442.132.3 Art. 13 Abs. 2"


class lohnnachgenuss_pro_hinterbliebener(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Lohnnachgenuss pro anspruchsberechtigtem Hinterbliebenen"
    reference = "SR 442.132.3 Art. 13 Abs. 3"

    def formula(person, period, parameters):
        gesamt = person('lohnnachgenuss_todesfall', period)
        anzahl = person('anzahl_anspruchsberechtigte_hinterbliebene', period)
        import numpy as np
        return np.where(anzahl > 0, gesamt / anzahl, 0)
