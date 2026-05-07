"""SR 651.1 Art. 22k - Infractions a l'interdiction d'informer

Generated from: ch/651/fr/651.1.md

Penalty for intentional or negligent breach of the prohibition on
informing (Art. 21a al. 3): fine up to CHF 10,000.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons',
    label='An individual', is_person=True,
)


class violation_interdiction_informer(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "La personne a enfreint intentionnellement ou par negligence l'interdiction d'informer (art. 21a al. 3)"
    reference = "SR 651.1 Art. 22k"


class amende_violation_interdiction_informer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende pour infraction a l'interdiction d'informer (CHF, max 10'000)"
    reference = "SR 651.1 Art. 22k"
    default_value = 0.0


class amende_maximale_interdiction_informer(Variable):
    value_type = float
    entity = Person
    definition_period = YEAR
    label = "Amende maximale pour infraction a l'interdiction d'informer (CHF)"
    reference = "SR 651.1 Art. 22k"
    default_value = 10_000.0
