"""SR 0.142.117.587 Art. 7

Generated from: ch/0/de/0.142.117.587.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# The variables above describe the immigration regime
# This text is about describing the tax to be applied in this situation.
# An explicit tax is not described; it is implied to be part of migration administration
# fees.
