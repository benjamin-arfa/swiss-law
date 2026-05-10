"""SR 745.21 Art. 1

Generated from: ch/745/de/745.21.md

Verordnung ueber die Sicherheitsorgane der Transportunternehmen im
oeffentlichen Verkehr (VST) - Gegenstand.
"""

from openfisca_core.model_api import *
from openfisca_core.periods import MONTH, YEAR
from openfisca_core.entities import build_entity

Person = build_entity(key='person', plural='persons', label='An individual', is_person=True)

class unterliegt_vst(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    label = "Unternehmen unterliegt der Verordnung ueber die Sicherheitsorgane (VST, SR 745.21)"
    reference = "SR 745.21 Art. 1"

    def formula(person, period, parameters):
        return person('unterliegt_bgst', period)
