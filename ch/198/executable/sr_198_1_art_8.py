"""SR 198.1 Art. 8

Generated from: ch/198/de/198.1.md

Ausfuehrungsbestimmungen: The Federal Council may issue implementing
provisions for this law and for the implementation of the Protocol.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# No computable logic - this article delegates regulatory authority to the
# Federal Council. Included as a stub for completeness.
