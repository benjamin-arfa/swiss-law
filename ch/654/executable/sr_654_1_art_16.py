"""SR 654.1 Art. 16 - Taches de l'AFC

Generated from: ch/654/de/654.1.md

Note: Art. 16 sets out the general duties of the ESTV (AFC) to ensure
proper application of the agreement and the law. This is organisational
and procedural with limited computable content.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class formulaire_electronique_obligatoire(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "L'AFC exige que certains formulaires soient deposes exclusivement sous forme electronique"
    reference = "SR 654.1 Art. 16 al. 3"
