"""SR 654.1 Art. 22a - Procedures electroniques

Generated from: ch/654/de/654.1.md

The Federal Council may prescribe electronic procedures. The ESTV
ensures authenticity and integrity of transmitted data.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class procedure_electronique_prescrite(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Le Conseil federal a prescrit la procedure electronique pour ce type de declaration"
    reference = "SR 654.1 Art. 22a al. 1"


class confirmation_electronique_admise(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC admet une confirmation electronique en lieu et place de la signature electronique qualifiee"
    reference = "SR 654.1 Art. 22a al. 3"
