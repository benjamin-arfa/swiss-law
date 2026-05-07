"""SR 0.142.116.367 Art. 11

Generated from: ch/0/de/0.142.116.367.md
"""

1. Since the variable needs to reflect the entity and purpose of this agreement, 
   we need to define it more broadly and abstractly.

2. One way to implement this would be to use a concept variable in OpenFisca, which 
   can encapsulate complex or dynamic information and is often used for things like 
   international agreements or other external factors that can't be directly calculated.

from openfisca_core.model_api import *
from openfisca_core.variables import Concept


class international_agreement_concept(Concept):
    value_type = str
    label = "International agreement on Stagiaires"


class agreement_name(Variable):
    value_type = str
    entity = international_agreement_concept
    definition_period = None
    label = "Name of the agreement"


class agreement_status(Variable):
    value_type = str
    entity = international_agreement_concept
    definition_period = None
    label = "Status of the agreement"
