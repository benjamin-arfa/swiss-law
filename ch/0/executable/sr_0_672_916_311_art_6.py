"""SR 0.672.916.311 Art. 6 - Processing of Austrian refund requests

Art. 6: Austrian tax office processes refund requests:
- Par. 1: Federal Ministry of Finance forwards to competent tax office
- Par. 2: Tax office verifies and decides on refund
- Par. 3: Decision notified in writing; payment made to address on request
- Par. 4: Rejections notified with reasons and appeal information
- Par. 5: Decision may be appealed within 1 month of notification

Generated from: ch/0/fr/0.672.916.311.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH
from openfisca_switzerland.entities import Person


class delai_recours_decision_at_jours(Variable):
    value_type = int
    entity = Person
    definition_period = MONTH
    label = "Appeal deadline: 1 month after notification of decision (Art. 6 par. 5)"
    default_value = 30


class demande_remboursement_at_acceptee(Variable):
    value_type = bool
    entity = Person
    definition_period = MONTH
    label = "Austrian tax refund request accepted (Art. 6 par. 2)"
    default_value = False


class montant_remboursement_at(Variable):
    value_type = float
    entity = Person
    definition_period = MONTH
    label = "Amount of Austrian tax refunded (Art. 6 par. 3)"
    default_value = 0
