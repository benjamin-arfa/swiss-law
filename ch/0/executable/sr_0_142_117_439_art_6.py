"""SR 0.142.117.439 Art. 6

Generated from: ch/0/de/0.142.117.439.md
"""

from enum import Enum
from openfisca_core.model_api import *

class EscortReason(Enum):
    SPECIAL_CARE = 'Special Care'
    SECURITY_MEASURES = 'Security Measures'

class ReturnApplicationStatus(Enum):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    DENIED = 'Denied'

class ReturnApplication(Variable):
    value_type = Enum
    possible_values = ReturnApplicationStatus
    entity = Person
    definition_period = DAY
    default_value = ReturnApplicationStatus.PENDING
    label = 'Return Application Status'

class ReturnEscortReason(Variable):
    value_type = Enum
    possible_values = EscortReason
    entity = Person
    definition_period = DAY
    default_value = EscortReason.SPECIAL_CARE
    label = 'Escort Reason'
