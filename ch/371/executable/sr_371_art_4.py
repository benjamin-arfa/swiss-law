"""SR 371 Art. 4 - Rehabilitierung (Rehabilitation)

Generated from: ch/de/371.md
All refugee helpers per Art. 1 and 2 are fully rehabilitated.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class vollstaendig_rehabilitiert(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Fluechtlingshelfer ist vollstaendig rehabilitiert"
    reference = "SR 371 Art. 4"

    def formula(person, period, parameters):
        return person('gilt_als_fluechtlingshelfer', period)
