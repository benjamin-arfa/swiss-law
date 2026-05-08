"""SR 745.11 Art. 1

Generated from: ch/745/de/745.11.md

Verordnung ueber die Personenbefoerderung (VPB) - Gegenstand.
Diese Verordnung regelt die Personenbefoerderung.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)


class unterliegt_vpb(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Taetigkeit unterliegt der Verordnung ueber die Personenbefoerderung (VPB, SR 745.11)"
    reference = "SR 745.11 Art. 1"

    def formula(person, period, parameters):
        return person('unterliegt_personenbefoerderungsgesetz', period)
