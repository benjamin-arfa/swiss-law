"""SR 0.672.916.311 Art. 1 - Withholding taxes covered

CH-Austria arrangement on tax relief for dividends, interest, and royalties.
Art. 1: Defines the withholding taxes subject to the arrangement:
- Austria: capital yield tax and income tax on royalties
- Switzerland: anticipatory tax (impot anticipe)
Relief is granted by refund (dividends/interest) or at source (royalties).

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import YEAR
from openfisca_switzerland.entities import Person


class revenu_dividendes_ch_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Dividend income subject to CH-AT double taxation arrangement (Art. 1)"
    default_value = 0


class revenu_interets_ch_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Interest income subject to CH-AT double taxation arrangement (Art. 1)"
    default_value = 0


class revenu_redevances_licences_ch_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Royalty income subject to CH-AT double taxation arrangement (Art. 1)"
    default_value = 0


class degrevemement_par_remboursement(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Tax relief granted by refund - for dividends and interest (Art. 1 par. 2)"

    def formula(person, period, parameters):
        has_dividends = person("revenu_dividendes_ch_at", period) > 0
        has_interest = person("revenu_interets_ch_at", period) > 0
        return has_dividends + has_interest


class montants_remboursables_sans_interet(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Refundable tax amounts bear no interest (Art. 1 par. 4)"
    default_value = True
