"""SR 654.1 Art. 27 - Procedure (dispositions penales)

Generated from: ch/654/de/654.1.md

The VStrR (Federal Act on Administrative Criminal Law) applies to
prosecution and adjudication of offences. The ESTV is the prosecuting
and adjudicating authority.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)

# Skipped: Art. 27 is a procedural provision designating the applicable
# procedural law (VStrR) and the competent authority (ESTV).
# No computable rule can be derived.
