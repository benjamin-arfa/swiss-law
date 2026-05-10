"""SR 730.05 Art. 5

Generated from: ch/730/fr/730.05.md

Art. 5 - Fee surcharges:
1. A surcharge up to 100% of the base fee may be charged for:
   a. Urgent decisions/services requested by the applicant, or exceptional effort
   b. Work on Sundays, holidays, and at night
2. If work is outsourced to third parties, an administrative surcharge of 20%
   of the base fee may be charged on top of disbursements.
3. Surcharges must be justified and shown separately.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class oemol_en_urgence_ou_exceptionnel(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether the service was urgent or required exceptional effort"
    reference = "SR 730.05 Art. 5 Abs. 1"
    default_value = False


class oemol_en_travail_hors_heures(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether work was performed on Sundays, holidays, or at night"
    reference = "SR 730.05 Art. 5 Abs. 1"
    default_value = False


class oemol_en_taux_supplement_pct(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Applied surcharge rate as percentage of base fee (0-100%)"
    reference = "SR 730.05 Art. 5 Abs. 1"
    default_value = 0


class oemol_en_travaux_tiers(Variable):
    value_type = bool
    entity_key = 'person'
    definition_period = YEAR
    label = "Whether work was outsourced to third parties"
    reference = "SR 730.05 Art. 5 Abs. 2"
    default_value = False


class oemol_en_debours_tiers_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Disbursements for outsourced third-party work (CHF)"
    reference = "SR 730.05 Art. 5 Abs. 2"
    default_value = 0


class oemol_en_supplement_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total surcharge amount (CHF)"
    reference = "SR 730.05 Art. 5"

    def formula(person, period, parameters):
        base = person('oemol_en_emolument_base_chf', period)
        taux = person('oemol_en_taux_supplement_pct', period)
        travaux_tiers = person('oemol_en_travaux_tiers', period)
        debours = person('oemol_en_debours_tiers_chf', period)
        p = parameters(period).sr_730_05

        # Surcharge capped at 100% of base fee
        taux_borne = min_(taux, p.supplement_max_pct)
        supplement_base = base * taux_borne / 100

        # Administrative surcharge for outsourced work: 20% of base fee
        supplement_admin = where(
            travaux_tiers,
            base * p.supplement_administratif_tiers_pct / 100,
            0
        )

        return supplement_base + supplement_admin


class oemol_en_emolument_total_chf(Variable):
    value_type = float
    entity_key = 'person'
    definition_period = YEAR
    label = "Total fee including base fee, surcharges, and third-party disbursements (CHF)"
    reference = "SR 730.05 Art. 3, 5"

    def formula(person, period, parameters):
        base = person('oemol_en_emolument_base_chf', period)
        supplement = person('oemol_en_supplement_chf', period)
        debours = person('oemol_en_debours_tiers_chf', period)

        return base + supplement + debours
