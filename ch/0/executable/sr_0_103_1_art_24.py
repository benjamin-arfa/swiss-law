"""SR 0.103.1 Art. 24

Generated from: ch/0/de/0.103.1.md
"""

# Given the challenge of translating Art. 24 directly into concrete OpenFisca code variables,
# the most suitable example under the constraints given is this simplistic OpenFisca parameter snippet.
from openfisca_core.model_api import *

class international_commitment_threshold(Variable):
    value_type = float
    default_value = 1.0
    label = 'International commitment threshold.'
    entity = None
    definition_period = None
