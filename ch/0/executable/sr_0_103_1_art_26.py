"""SR 0.103.1 Art. 26

Generated from: ch/0/de/0.103.1.md
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

# (Not suitable for OpenFisca)
# The text is a treaty provision that deals with accession and notification of ratification/deposit but does not have specific numerical parameters applicable to individuals or businesses
