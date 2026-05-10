"""SR 730.05 Art. 3

Generated from: ch/730/fr/730.05.md

Art. 3 - Calculation of fees:
1. Fees are calculated based on the tariff in the annex.
2. Where no fixed amount exists for a given service, the fee is calculated
   based on time invested: CHF 75-250/hour depending on the position
   of the person handling the case.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class oemol_en_heures_investies(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Number of hours invested for the service/decision"
    reference = "SR 730.05 Art. 3 Abs. 2"


class oemol_en_tarif_horaire_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Applicable hourly rate based on staff function (CHF/hour)"
    reference = "SR 730.05 Art. 3 Abs. 2"


class oemol_en_montant_fixe_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Fixed fee amount from tariff annex (CHF, 0 if no fixed amount)"
    reference = "SR 730.05 Art. 3 Abs. 1"
    default_value = 0


class oemol_en_emolument_base_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Base fee amount (CHF) - either fixed or time-based"
    reference = "SR 730.05 Art. 3"

    def formula(person, period, parameters):
        montant_fixe = person('oemol_en_montant_fixe_chf', period)
        heures = person('oemol_en_heures_investies', period)
        tarif = person('oemol_en_tarif_horaire_chf', period)
        p = parameters(period).sr_730_05

        # Clamp hourly rate to legal bounds
        tarif_min = p.tarif_horaire_min_chf
        tarif_max = p.tarif_horaire_max_chf
        tarif_borne = min_(max_(tarif, tarif_min), tarif_max)

        # Use fixed amount if available, otherwise time-based
        return where(
            montant_fixe > 0,
            montant_fixe,
            heures * tarif_borne
        )
