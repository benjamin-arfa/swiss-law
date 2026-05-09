"""SR 654.1 Art. 21 - Statistiques

Generated from: ch/654/de/654.1.md

The ESTV may compile and publish anonymised statistics based on CbC reports.
No right of access to information beyond what is published.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 21 authorises the ESTV to publish anonymised statistics.
# This is an organisational power with no computable rule for individuals.
