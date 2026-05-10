"""SR 642.11 Art. 33a

Generated from: ch/642/fr/642.11.md

Art. 33a Dons (Donations):
Cash donations and other assets to non-profit legal entities based in
Switzerland (Art. 56 let. g) are deductible up to 20% of income after
deductions (Art. 26-33), provided donations amount to at least CHF 100
per tax year. Donations to the Confederation, cantons, communes and
their establishments (Art. 56 let. a-c) are deductible on the same terms.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class ifd_dons_utilite_publique(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Donations to tax-exempt public-benefit entities (CHF)"
    reference = "SR 642.11 Art. 33a"


class ifd_revenu_apres_deductions_26_33(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Income after deductions under Art. 26-33 (CHF)"
    reference = "SR 642.11 Art. 33a"


class ifd_deduction_dons(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Deduction for public-benefit donations (CHF)"
    reference = "SR 642.11 Art. 33a"

    def formula(person, period, parameters):
        dons = person('ifd_dons_utilite_publique', period)
        revenu_net = person('ifd_revenu_apres_deductions_26_33', period)

        # Max 20% of net income after deductions
        plafond = revenu_net * 0.20

        # Minimum CHF 100 per year to qualify
        dons_deductibles = where(dons >= 100, min_(dons, plafond), 0)

        return dons_deductibles
