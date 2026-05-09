"""SR 654.11 Art. 6 - Organisation und Fuehrung des Informationssystems

Generated from: ch/654/de/654.11.md

The ESTV information system is operated as an independent system on the
BIT platform. Systems may be networked for master data exchange.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 6 is an organisational provision on the ESTV information
# system infrastructure. No computable rule for individual entities.
