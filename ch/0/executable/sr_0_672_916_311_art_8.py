"""SR 0.672.916.311 Art. 8 - Austrian withholding tax on royalties: reduced rate

Art. 8: Swiss-resident royalty beneficiaries may request reduction of
Austrian withholding tax to 5%.
- Par. 3: Refund of excess over 5% may be requested within 3 years
  after end of year when royalties became due.

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class taux_retenue_at_redevances_normal(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Normal Austrian withholding tax rate on royalties"
    default_value = 0.20


class taux_retenue_at_redevances_reduit(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Reduced Austrian withholding rate on royalties: 5% (Art. 8 par. 1)"
    default_value = 0.05


class montant_redevances_licences_at(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Gross royalty income from Austria (Art. 8)"
    default_value = 0


class retenue_at_redevances_excedentaire(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Excess Austrian withholding tax on royalties to be refunded (Art. 8 par. 3)"

    def formula(person, period, parameters):
        montant = person("montant_redevances_licences_at", period)
        taux_normal = person("taux_retenue_at_redevances_normal", period)
        taux_reduit = person("taux_retenue_at_redevances_reduit", period)
        eligible = person("eligible_degrevement_ch_at", period)
        return max_(0, montant * (taux_normal - taux_reduit)) * eligible


class delai_remboursement_redevances_at_ans(Variable):
    value_type = int
    entity = Person
    definition_period = YEAR
    label = "Deadline for refund of excess royalty tax: 3 years (Art. 8 par. 3)"
    default_value = 3
