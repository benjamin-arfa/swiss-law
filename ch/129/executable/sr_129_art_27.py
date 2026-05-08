"""SR 129 Art. 27 - Organisation

Generated from: ch/de/129.md
fedpol operates the PIU. The PIU is organizationally and staffwise
independent from investigation and prosecution units.
In force since 1 January 2026.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(
    key='person', plural='persons', label='An individual', is_person=True
)


class piu_organisatorisch_unabhaengig(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "PIU ist organisatorisch und personell von Ermittlungs- und Strafverfolgungseinheiten unabhaengig"
    reference = "SR 129 Art. 27 Abs. 2"

    def formula(person, period, parameters):
        return True
