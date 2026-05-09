"""SR 654.11 Art. 7 - Kategorien der bearbeiteten Personendaten

Generated from: ch/654/de/654.11.md

The ESTV may process the personal data transmitted to it under the
applicable agreement and the ALBAG.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 7 authorises the ESTV to process personal data received
# under the agreement. This is a data protection provision with no
# computable rule for reporting entities.
