"""SR 0.106 Art. 4

Generated from: ch/0/de/0.106.md
"""

from openfisca_core.model_api import *

committee_status = ExternVariable(
    'committee_status',
    value_type=bool,
    label='Status of the SR 0.106 committee\'s composition and availability'
)
