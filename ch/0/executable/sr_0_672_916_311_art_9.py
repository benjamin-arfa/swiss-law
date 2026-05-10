"""SR 0.672.916.311 Art. 9 - Refund of Swiss anticipatory tax

Art. 9: Austrian residents request refund of Swiss anticipatory tax
using form R-Sch 2 R 84.
- Par. 2: Request within 3 years after end of calendar year of payment.
- Par. 3: Multiple claims may be combined; up to 3 years in one request.

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class revenu_dividendes_ch_vers_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Swiss-source dividend income payable to Austrian resident (Art. 9)"
    default_value = 0


class revenu_interets_ch_vers_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Swiss-source interest income payable to Austrian resident (Art. 9)"
    default_value = 0


class impot_anticipe_ch_preleve(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Swiss anticipatory tax (Verrechnungssteuer) withheld (Art. 9)"

    def formula(person, period, parameters):
        dividendes = person("revenu_dividendes_ch_vers_at", period)
        interets = person("revenu_interets_ch_vers_at", period)
        # Swiss anticipatory tax rate is 35%
        taux_impot_anticipe = 0.35
        return (dividendes + interets) * taux_impot_anticipe


class delai_remboursement_impot_anticipe_ans(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Deadline for Swiss anticipatory tax refund: 3 years (Art. 9 par. 2)"
    default_value = 3
