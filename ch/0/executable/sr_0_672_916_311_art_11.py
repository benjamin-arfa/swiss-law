"""SR 0.672.916.311 Art. 11 - Swiss tax administration processes refund

Art. 11: Federal Tax Administration (AFC) processes Swiss anticipatory
tax refund requests:
- Par. 2: Decision notified in writing; payment to address on form
- Par. 3: Rejections sent by registered mail with reasons
- Par. 4: Appeal within 30 days to AFC (objection), then 30 days to
  Federal Supreme Court (administrative appeal)

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class delai_reclamation_afc_jours(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Deadline for objection to AFC decision: 30 days (Art. 11 par. 4)"
    default_value = 30


class delai_recours_tribunal_federal_jours(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Deadline for administrative appeal to Federal Supreme Court: 30 days (Art. 11 par. 4)"
    default_value = 30


class decision_remboursement_impot_anticipe(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "AFC decision on Swiss anticipatory tax refund (Art. 11 par. 1)"
    default_value = False


class montant_remboursement_impot_anticipe(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Amount of Swiss anticipatory tax refunded to Austrian resident (Art. 11 par. 2)"
    default_value = 0
