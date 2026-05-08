"""SR 371 Art. 12 - Verfahrenskosten (Procedural Costs)

Generated from: ch/de/371.md
Proceedings before the Commission are free of charge.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class rehabilitierungsverfahren_kostenlos(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Das Verfahren vor der Rehabilitierungskommission ist kostenlos"
    reference = "SR 371 Art. 12"

    def formula(person, period, parameters):
        return True
